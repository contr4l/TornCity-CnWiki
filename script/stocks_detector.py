import requests
import json
import pandas as pd

global_key = ""

income_table_name = "income_table.csv"
employee_table_name = "employee_table.csv"

default_csv_list = [income_table_name, employee_table_name]

def set_key(key):
    global global_key
    global_key = key

def get_stocks_data_json(key : str = global_key) -> json:
    """
    {
        "stocks": {
            "1": {
                    "stock_id": 1,
                    "name": "Torn & Shanghai Banking",
                    "acronym": "TSB",
                    "current_price": 1036.87,
                    "market_cap": 13900914727992,
                    "total_shares": 13406612910,
                    "investors": 9637,
                    "benefit": {
                            "type": "active",
                            "frequency": 31,
                            "requirement": 3000000,
                            "description": "$50,000,000",
                    },
                }
        }
    }
    """

    url = "https://api.torn.com/torn/?selections=stocks&key={}".format(key)

    res = requests.get(url)
    if res.status_code != 200:
        print("api request gets negative response!")
        raise TimeoutError

    return json.loads(res.text)

import datetime
def get_ymd():
    now = datetime.datetime.now().date()
    tm = datetime.datetime.now()
    return "{}/{}/{}".format(now.year, now.month, now.day), "{}:{}:{}".format(tm.hour, tm.minute, tm.second)

stocks_data_name = "torn_stocks_data.csv"

import os
def store_stock_data(key = global_key):

    columns = ["时间","股票名","缩写","现价","保有量","投资者"]
    
    header = False
    if os.path.exists(stocks_data_name):
        df = pd.read_csv(stocks_data_name, names=columns)
    else:
        header = True
        df = pd.DataFrame(columns=columns)
    
    ymd, hms = get_ymd()

    loc = df.shape[0]

    data = get_stocks_data_json(key)
    for enum_ in data["stocks"]:
        record = data["stocks"][enum_]
        df.loc[loc, "时间"] = ymd + " " + hms
        df.loc[loc, "股票名"] = record["name"]
        df.loc[loc, "缩写"] = record["acronym"]
        df.loc[loc, "现价"] = record["current_price"]
        df.loc[loc, "保有量"] = record["market_cap"]
        df.loc[loc, "投资者"] = record["investors"]
        loc += 1
    
    df.to_csv(stocks_data_name, index=0, header=header)



import time
if __name__ == "__main__":
    while True:
        store_stock_data("在这里输入API_KEY")
        time.sleep(3)