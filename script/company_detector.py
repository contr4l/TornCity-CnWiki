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

import datetime
def get_ymd():
    now = datetime.datetime.now().date()
    return "{}/{}/{}".format(now.year, now.month, now.day)

def record_income_table(key = global_key):
    print("record income table...")
    df = pd.read_csv(income_table_name)
    loc = df.shape[0]

    ymd = get_ymd()
    
    if ymd in df["日期"].values:
        print("update...")
        loc = df[df["日期"] == ymd].index[0]
    else:
        print("creating...")
    
    data = get_detailed_info(key)

    df.loc[loc, "序号"] = df.loc[loc-1, "序号"] + 1
    df.loc[loc, "日期"] = ymd
    df.loc[loc, "Traning Contract"] = 
    

def merge_csv_files(csv_files : list = default_csv_list):
    writer = pd.ExcelWriter("company_data.xlsx")

    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        df.to_excel(writer, sheet_name=csv_file)

    writer.close()