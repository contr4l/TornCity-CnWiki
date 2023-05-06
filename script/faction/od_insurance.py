import json, requests
from datetime import datetime, timezone
from name_tid import get_name_tid, set_key

"""
1. 支持查询本月1号开始的所有log并保存成json文件
2. 支持读取本地json格式的log文件, 并执行热更新
3. 
"""

global_key = ""

def set_global_key(key):
    global global_key
    global_key = key

# https://api.torn.com/torn/?selections=logcategories&key={}, 得到的字段用于&cat=
# https://api.torn.com/torn/?selections=logtypes&key={}, 得到的字段用于&log=

log_types_map = {"Item receive" : "4103"}
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

def parse_xan_data(content : json):
    ody_list = {}
    odx_list = {}
    others_list = {}
    xan_id = items_id_map["xan"]
    for hash_ in content["log"]:
        data = content["log"][hash_]["data"]
        ppl = data["sender"]
        if xan_id in data["items"]:
            amount = data["items"][xan_id]
            if "ody" in data["message"]:
                ody_list[ppl] = ody_list.get(ppl, 0) + amount
            elif "odx" in data["message"]:
                odx_list[ppl] = ody_list.get(ppl, 0) + amount
            else:
                others_list[ppl] = others_list.get(ppl, "") + "--- " + data["message"] + ":" + str(amount)

    return list(odx_list.items()), list(ody_list.items()), list(others_list.items())

def save_odxy_data():
    tid_map = get_name_tid()
    data = get_receive_item_data_this_month()
    odx_list, ody_list, others_list = parse_xan_data(data)

    print(odx_list, ody_list, others_list)

    f = open("od_insurance.csv", "w")
    f.write("odx_name, odx_count, ody_name, ody_count, others_name, others_info\n")

    for i in range(max(len(odx_list), len(ody_list), len(others_list))):
        if i >= len(odx_list):
            kx,vx = "",""
        else:
            kx,vx = odx_list[i][0],odx_list[i][1].replace(",", ";")
        if i >= len(ody_list):
            ky,vy = "",""
        else:
            ky,vy = ody_list[i][0],ody_list[i][1].replace(",", ";")
        if i >= len(others_list):
            kz,vz = "",""
        else:
            kz,vz = others_list[i][0],others_list[i][1].replace(",", ";")
        
        f.write("{},{},{},{},{},{}\n".format(tid_map.get(str(kx), kx),vx,tid_map.get(str(ky), ky),vy,tid_map.get(str(kz), kz),vz))
    f.close()

set_global_key("9Za3NItePevzDvXu")
set_key("GkGCcSyK7Fa359MT")
save_odxy_data()
