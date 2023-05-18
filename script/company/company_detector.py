import requests
import json
import pandas as pd
import os

global_key = ""

current_dir = os.path.dirname(os.path.abspath(__file__)) + "/"
income_table_name = current_dir+"income_table.csv"
employee_table_name = current_dir+"employee_table.csv"

print("income file is {}\n employee file is {}\n".format(income_table_name, employee_table_name))

default_csv_list = [income_table_name, employee_table_name]

def set_key(key):
    global global_key
    print("set key to {}".format(key))
    global_key = key

def get_data_json(selections : str, key : str = global_key) -> json:
    url = "https://api.torn.com/company/?selections={}&key={}".format(
        selections, key
    )

    print("send requests {}".format(url))
    res = requests.get(url)
    if res.status_code != 200:
        print("api request gets negative response!")
        raise TimeoutError

    return json.loads(res.text)

def get_detailed_info():
    """
    "company_detailed": {
                "ID": 99636,
                "company_funds": 108461497,
                "company_bank": 108461497,
                "popularity": 2,
                "efficiency": 50,
                "environment": 100,
                "trains_available": 0,
                "advertising_budget": 515000,
                "upgrades": {
                        "company_size": 12,
                        "staffroom_size": "No staff room",
                        "storage_size": "No storage room",
                        "storage_space": 0,
                },
                "value": 1533911497,
        }
    """
    return get_data_json("detailed", global_key)

def get_profile():
    """
    "company": {
            "ID": 99636,
            "company_type": 37,
            "rating": 0,
            "name": "Welcome To Umbrella",
            "director": 2893026,
            "employees_hired": 12,
            "employees_capacity": 12,
            "daily_income": 6000000,
            "daily_customers": 1,
            "weekly_income": 9000000,
            "weekly_customers": 2,
            "days_old": 2,
            "employees": {
                    "1368994": {
                        "name": "---",
                        "position": "Disposal Engineer",
                        "days_in_company": 2,
                        "last_action": {
                                "status": "Offline",
                                "timestamp": 1681994451,
                                "relative": "40 minutes ago",
                        },
                        "status": {
                                "description": "In hospital for 20 mins ",
                                "details": "Suffering from an acute hemolytic transfusion reaction",
                                "state": "Hospital",
                                "color": "red",
                                "until": 1681998120,
                        },
                    }
                }
            }
    """
    return get_data_json("profile", global_key)

def get_employees():
    """
    {
        "company_employees": {
            "1368994": {
                    "name": "---",
                    "position": "Disposal Engineer",
                    "days_in_company": 2,
                    "wage": 1000000,
                    "manual_labor": 40018,
                    "intelligence": 191673,
                    "endurance": 121433,
                    "effectiveness": {
                            "working_stats": 102,
                            "settled_in": 1,
                            "merits": 10,
                            "management": 3,
                            "addiction": -12,
                            "total": 104,
                    },
                    "last_action": {
                            "status": "Offline",
                            "timestamp": 1681994451,
                            "relative": "44 minutes ago",
                    },
                    "status": {
                            "description": "In hospital for 16 mins ",
                            "details": "Suffering from an acute hemolytic transfusion reaction",
                            "state": "Hospital",
                            "color": "red",
                            "until": 1681998120,
                    },
            },
        }
    }
    """
    return get_data_json("employees", global_key)

def get_price():
    """
    {
        "company_stock": {
                "Training Contract": {
                        "cost": 0,
                        "rrp": 500000,
                        "price": 500000,
                        "in_stock": 0,
                        "on_order": 0,
                        "sold_amount": 0,
                        "sold_worth": 0,
                },
            }
    }
    """
    return get_data_json("stock", global_key)


detail = {}
price = {}
profile = {}
employees = {}
def get_all_data():
    global detail, price, profile, employees

    detail = get_detailed_info()
    price = get_price()
    profile = get_profile()
    employees = get_employees()

import datetime
def get_ymd():
    now = datetime.datetime.now().date()
    tm = datetime.datetime.now()
    return "{}/{}/{}".format(now.year, now.month, now.day), "{}:{}:{}".format(tm.hour, tm.minute, tm.second)

def get_loc(df: pd.DataFrame, ymd):
    loc = df.shape[0]
    if ymd in df["日期"].values:
        print("updating...")
        loc = df[df["日期"] == ymd].index[0]
    else:
        print("creating...")
    
    return loc



def record_income_table():
    print("record income table...")
    columns = ['序号', '日期', 'Training Contract', 'Protection Contract',
               'Engagement Contract', 'Military Contract', '生产日期', '收入', '工资', '广告费',
               '利润', '总效率', '产量', '销量', '库存', '单价', '成本', '记录时间']
    
    header = False
    if os.path.exists(income_table_name):
        df = pd.read_csv(income_table_name, names=columns, encoding="utf8")
    else:
        header = True
        df = pd.DataFrame(columns=columns)

    ymd, hms = get_ymd()
    
    loc = get_loc(df, ymd)

    detail = get_detailed_info()
    price = get_price()
    profile = get_profile()
    employees = get_employees()

    df.loc[loc, "序号"] = int(df.loc[loc-1, "序号"]) + 1 if loc > 1 else 1
    
    df.loc[loc, "日期"] = ymd
    df.loc[loc, "Training Contract"] = price["company_stock"]["Training Contract"]["price"]
    df.loc[loc, "Protection Contract"] = price["company_stock"]["Protection Contract"]["price"]
    df.loc[loc, "Engagement Contract"] = price["company_stock"]["Engagement Contract"]["price"]
    df.loc[loc, "Military Contract"] = price["company_stock"]["Military Contract"]["price"]
    
    df.loc[loc, "生产日期"] = ymd
    df.loc[loc, "收入"] = "$" + str(profile["company"]["daily_income"])
    
    total_wages = 0
    total_effe = 0
    for ppl in employees["company_employees"]:
        total_wages += employees["company_employees"][ppl]["wage"]
        total_effe += employees["company_employees"][ppl]["effectiveness"]["total"]

    df.loc[loc, "工资"] = "$" + str(total_wages)
    df.loc[loc, "广告费"] = "$" + str(detail["company_detailed"]["advertising_budget"])
    df.loc[loc, "利润"] = "$" + str(profile["company"]["daily_income"] - total_wages - detail["company_detailed"]["advertising_budget"])

    df.loc[loc, "总效率"] = total_effe

    df.loc[loc, "产量"] = profile["company"]["daily_customers"]
    df.loc[loc, "销量"] = profile["company"]["daily_customers"]
    df.loc[loc, "库存"] = 0

    df.loc[loc, "单价"] = "$" + str(profile["company"]["daily_income"] / profile["company"]["daily_customers"])
    df.loc[loc, "成本"] = 0

    df.loc[loc, "记录时间"] = ymd + " " + hms

    df.to_csv(income_table_name, index=0, header=header, encoding="utf8")

from math import ceil
def record_employee_table():
    columns = ["日期","岗位","天数","MAN","INT","END", "属", "估", "登", "名字", "天", "点", "课", "理", "药", "离", "总", "薪", "参"]

    header = False
    if os.path.exists(employee_table_name):
        df = pd.read_csv(employee_table_name, names=columns, encoding="utf8")
    else:
        header = True
        df = pd.DataFrame(columns=columns)

    ymd, hms = get_ymd()
    loc = get_loc(df, ymd)

    ppl_data = employees["company_employees"]
    for ppl in ppl_data:
        df.loc[loc, "日期"] = ymd
        df.loc[loc, "岗位"] = ppl_data[ppl]["position"]
        df.loc[loc, "天数"] = ppl_data[ppl]["days_in_company"]
        df.loc[loc, "MAN"] = ppl_data[ppl]["manual_labor"]
        df.loc[loc, "INT"] = ppl_data[ppl]["intelligence"]
        df.loc[loc, "END"] = ppl_data[ppl]["endurance"]
        df.loc[loc, "属"] = ppl_data[ppl]["effectiveness"].get("working_stats", 0)
        df.loc[loc, "估"] = "---"
        df.loc[loc, "登"] = ppl_data[ppl]["last_action"]["relative"]
        df.loc[loc, "名字"] = ppl_data[ppl]["name"]
        df.loc[loc, "天"] = ppl_data[ppl]["effectiveness"].get("settled_in", 0)
        df.loc[loc, "点"] = ppl_data[ppl]["effectiveness"].get("merits", 0)
        df.loc[loc, "课"] = ppl_data[ppl]["effectiveness"].get("director_education", 0)
        df.loc[loc, "理"] = ppl_data[ppl]["effectiveness"].get("management", 0)
        df.loc[loc, "药"] = ppl_data[ppl]["effectiveness"].get("addiction", 0)
        df.loc[loc, "离"] = ppl_data[ppl]["effectiveness"].get("inactivity", 0)
        df.loc[loc, "总"] = ppl_data[ppl]["effectiveness"]["total"]
        df.loc[loc, "薪"] = "$" + str(ppl_data[ppl]["wage"])
        df.loc[loc, "参"] = "---"
        loc += 1

    df.to_csv(employee_table_name, index=0, header=header, encoding="utf8")
    



def merge_csv_files(csv_files : list = default_csv_list):
    writer = pd.ExcelWriter("company_data.xlsx")

    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        df.to_excel(writer, sheet_name=csv_file)

    writer.close()


if __name__ == "__main__":
    set_key("GkGCcSyK7Fa359MT")
    get_all_data()
    record_income_table()
    record_employee_table()