import requests, json
import datetime

faction_dict = {
                "36134": "SH", 
                "16335": "NOV", 
                "27902": "CCRC",
                "9356": "PTA", 
                "20465": "Main", 
                "10741": "Tri", 
                "16424": "MHY"
                }

key = ""
def set_key(k):
    global key
    key = k

import time
def send_request(url):
    print("send requests {}".format(url))
    res = requests.get(url)
    if res.status_code != 200:
        print("api request gets negative response!")
        raise TimeoutError
    time.sleep(0.4)
    return json.loads(res.text)

def get_faction_data_json(faction_id) -> json:
    url = "https://api.torn.com/faction/{}?selections=basic&key={}".format(
        faction_id, key
    )
    return send_request(url)

def get_user_data_json(user : str, selections : str) -> json:
    url = "https://api.torn.com/user/{}?selections={}&key={}".format(
        user, selections, key
    )
    return send_request(url)

def get_user_list(faction_id) -> json:
    users = {
                #"torn_id" : "nickname"
            }
    
    data = get_faction_data_json(faction_id)
    
    ppl_list = data["members"]

    for ppl_id in ppl_list:
        users[ppl_id] = ppl_list[ppl_id]["name"]
    
    return users


def save_data():
    f = open("overdose_analyzer.csv", "a")
    # f.write("faction,name,ecs,lsd,xan,total,overdose,rate\n")
    flag = 0
    for faction_id in faction_dict:
        users = get_user_list(faction_id)
        for torn_id in users:
            print("Visit ", users[torn_id])
            if flag != 1:
                if users[torn_id] == "Salusse":
                    flag = 1
                    continue
                else:
                    continue

            user_data = get_user_data_json(torn_id, "personalstats")["personalstats"]
            if user_data["drugsused"] < 50:
                print("ignore newbies")
                continue

            elif user_data["overdosed"] == 0:
                print("lucky guys : {} taken {} drugs and overdosed {} times".format(users[torn_id], users.get("drugsused", 0), users.get("overdosed", 0)))    
                continue

            f.write("{},{},{},{},{},{},{},{}\n".format(
                faction_dict[faction_id],
                users[torn_id],
                user_data["exttaken"],
                user_data["lsdtaken"],
                user_data["xantaken"],
                user_data["drugsused"],
                user_data["overdosed"],
                int(user_data["drugsused"] / user_data["overdosed"])
            ))
    f.close()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm

def analyze_data():
    f = pd.read_csv("overdose_analyzer.csv")
    old_hands = f[f["xan"] >= 500]
    x = old_hands["rate"].to_list()
    x.sort()
    print(x, len(x))
    mu = np.mean(x)
    sigma = np.std(x)

    y = norm.pdf(x,mu,sigma)

    plt.hist(x, density=True, bins=20)
    plt.plot(x, y, "r--")
    plt.subplots_adjust(left=0.15)
    plt.show()


if __name__ == "__main__":
    # set_key("GkGCcSyK7Fa359MT")
    # save_data()
    analyze_data()