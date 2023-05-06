import json, requests
from datetime import datetime, timezone

start = datetime(2023,5,1)
timestamp = start.replace(tzinfo=timezone.utc).timestamp()

url = "https://api.torn.com/user/?selections=log&log=4103&from={}&key=4QKEFxUNZrJZ0QC8".format(timestamp)

res = requests.get(url)
content = json.loads(res.text)

ody_list = {}
odx_list = {}
others_list = {}
for item in content["log"]:
    data = content["log"][item]["data"]
    ppl = data["sender"]
    if "206" in data["items"]:
        amount = data["items"]["206"]
        if "ody" in data["message"]:
            ody_list[ppl] = ody_list.get(ppl, 0) + amount
        elif "odx" in data["message"]:
            odx_list[ppl] = ody_list.get(ppl, 0) + amount
        else:
            others_list[ppl] = others_list.get(ppl, "") + "--- " + data["message"] + ":" + str(amount)

print(odx_list.keys())
print(ody_list.keys())
print(others_list)