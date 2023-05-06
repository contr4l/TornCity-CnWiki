import json, requests

"""
1. 支持查询本月1号开始的所有log并保存成json文件
2. 支持读取本地json格式的log文件, 并筛选相关信息
3. 支持筛选


"""


global_key = ""

def set_global_key(key):
    global global_key
    global_key = key

# https://api.torn.com/torn/?selections=logcategories&key={}, 得到的字段用于&cat=
# https://api.torn.com/torn/?selections=logtypes&key={}, 得到的字段用于&log=

possible_log_types = {"xan" : "206"}

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



set_global_key("9Za3NItePevzDvXu")
res = get_log_data("log")
print(res)