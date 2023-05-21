import json, requests, os, time
from datetime import datetime, timezone

"""
1. 支持查询本月1号开始的所有log并保存成json文件
2. 支持读取本地json格式的log文件, 并执行热更新
"""

global_key = ""

def set_global_key(key):
    global global_key
    global_key = key

# https://api.torn.com/torn/?selections=logcategories&key={}, 得到的字段用于&cat=
# https://api.torn.com/torn/?selections=logtypes&key={}, 得到的字段用于&log=

def get_name_tid_from_file(filename):
    map_ = {}
    with open(filename, "r") as f:
        for line in f.readlines()[1:]:
            tid, name = line.split(",")
            map_[int(tid)] = name
    return map_

log_types_map = {
    "Item receive": "4103",
    "Item send": "4102"
}

log_cates_map = {}
items_id_map  = {"xan" : "206"}

def get_log_data(logtypes : str, from_ : str) -> json:
    url = "https://api.torn.com/user/?selections=log&log={}&from={}&key={}".format(
        logtypes, from_, global_key
    )

    print("send requests {}".format(url))
    res = requests.get(url)
    if res.status_code != 200:
        print("api request gets negative response!")
        raise TimeoutError
    
    content = json.loads(res.text)
    
    if "error" in content:
        print("errcode = {}, errmsg = {}".format(content["error"]["code"], content["error"]["error"]))
        raise PermissionError

    return content

# 获取本月1号0时的时间戳
def get_month_start_timestamp():
    now_ = datetime.now()
    start = datetime(now_.year, now_.month, 1)
    timestamp = start.replace(tzinfo=timezone.utc).timestamp()
    return timestamp

def get_receive_item_data_this_month():
    data = get_log_data(log_types_map["Item receive"], get_month_start_timestamp())
    return data

def get_send_item_data_this_month():
    data = get_log_data(log_types_map["Item send"], get_month_start_timestamp())
    return data

def parse_xan_data(content : json, in_or_out):
    """
    "HU2loEymCppeqMQE5dsy": {
                            "log": 4103,
                            "title": "Item receive",
                            "timestamp": 1683435437,
                            "category": "Item sending",
                            "data": {
                                    "sender": 2893242,
                                    "items": {
                                            "206": 4,
                                    },
                                    "message": "odx",
                            },
                            "params": {
                                    "italic": 1,
                                    "color": "green",
                            },
                        },
    """
    # ody_list = {}
    # odx_list = {}
    # others_list = {}

    return_data = []
    xan_id = items_id_map["xan"]

    for hash_ in content["log"]:
        data = content["log"][hash_]["data"]
        timestamp = content["log"][hash_]["timestamp"]
        uid = data[in_or_out]
        message = data["message"]
        if xan_id in data["items"]:
            amount = data["items"][xan_id]
            # 时间戳；发送姓名；uid；数量；留言
            return_data.append([timestamp, uid, amount, message])        
    
    return return_data
    # if "ody" in data["message"]:
    #     ody_list[ppl] = ody_list.get(ppl, 0) + amount
    # elif "odx" in data["message"]:
    #     odx_list[ppl] = ody_list.get(ppl, 0) + amount
    # else:
    #     others_list[ppl] = others_list.get(ppl, "") + "--- " + data["message"] + ":" + str(amount)
    # return list(odx_list.items()), list(ody_list.items()), list(others_list.items())

def write_data(filename, recv_list, tid_name_map):
    from_ = 0
    header = "index,timestamp,name,uid,amount,message\n"
    if os.path.exists(filename):
        from_ = get_file_from_timestamp(filename)
        header = ""
    
    f = open(filename, "a", encoding="utf8")
    f.write(header)

    for i, item in enumerate(recv_list[::-1]):
        timestamp, tid, amount, message = item
        if timestamp <= from_:
            continue

        f.write("{},{},{},{},{},{}".format(i+1,
                                             datetime.fromtimestamp(int(timestamp)).strftime(
                                                 '%Y-%m-%d %H:%M:%S'),
                                             str(tid_name_map.get(
                                                 tid, tid)).strip(),
                                             tid,
                                             amount,
                                             message.replace(",", ";"))
                )
        if i != len(recv_list) - 1:
            f.write("\n")
    f.close()

def get_file_from_timestamp(filename):
    unix_timestamp = 0
    with open(filename, "r") as f:
        line = f.readlines()[-1]
        try:
            _, timestamp, _, _, _, _ = line.split(",")
            dateTime = datetime.strptime(timestamp,"%Y-%m-%d %H:%M:%S")
            unix_timestamp = time.mktime(dateTime.timetuple())
        except Exception as e:
            print(e)
    print("filename is {}, most timestamp is {}".format(filename, unix_timestamp))
    return unix_timestamp

# 序号；时间戳；发送姓名；uid；数量；留言
def save_xan_incoming_data():
    data = get_receive_item_data_this_month()
    recv_list = parse_xan_data(data, "sender")
    tid_name_map = get_name_tid_from_file("name_tid.csv")

    write_data("od_insurance.csv", recv_list, tid_name_map)

def save_xan_outgoing_data():
    data = get_send_item_data_this_month()
    recv_list = parse_xan_data(data, "receiver")
    tid_name_map = get_name_tid_from_file("name_tid.csv")

    write_data("od_insurance_out.csv", recv_list, tid_name_map)
        

set_global_key("4QKEFxUNZrJZ0QC8")
save_xan_incoming_data()
save_xan_outgoing_data()