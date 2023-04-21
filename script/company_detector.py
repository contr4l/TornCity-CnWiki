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

def get_data_json(selections : str, key : str = global_key) -> json:
    url = "https://api.torn.com/company/?selections={}&key={}".format(
        selections, key
    )

    res = requests.get(url)
    if res.status_code != 200:
        print("api request gets negative response!")
        raise TimeoutError

    return json.loads(res.text)

def get_detailed_info(key = global_key):
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
    return get_data_json("detailed", key)

def get_profile(key = global_key):
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
    return get_data_json("profile", key)

def get_employees(key = global_key):
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
    return get_data_json("employees", key)

def get_price(key = global_key):
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
    return get_data_json("stock", key)

import datetime
def get_ymd():
    now = datetime.datetime.now().date()
    tm = datetime.datetime.now()
    return "{}/{}/{}".format(now.year, now.month, now.day), "{}:{}:{}".format(tm.hour, tm.minute, tm.second)

import os
def record_income_table(key = global_key):
    print("record income table...")
    columns = ['序号', '日期', 'Training Contract', 'Protection Contract',
               'Engagement Contract', 'Military Contract', '生产日期', '收入', '工资', '广告费',
               '利润', '总效率', '产量', '销量', '库存', '单价', '成本', '记录时间']
    
    header = False
    if os.path.exists(income_table_name):
        df = pd.read_csv(income_table_name, names=columns)
    else:
        header = True
        df = pd.DataFrame(columns=columns)
    
    loc = df.shape[0]

    ymd, hms = get_ymd()
    
    
    if ymd in df["日期"].values:
        print("update...")
        loc = df[df["日期"] == ymd].index[0]
    else:
        print("creating...")

    detail = get_detailed_info(key)
    price = get_price(key)
    profile = get_profile(key)
    employees = get_employees(key)

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

    df.to_csv(income_table_name, index=0, header=header)

def merge_csv_files(csv_files : list = default_csv_list):
    writer = pd.ExcelWriter("company_data.xlsx")

    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        df.to_excel(writer, sheet_name=csv_file)

    writer.close()


if __name__ == "__main__":
    record_income_table("Put your key here")