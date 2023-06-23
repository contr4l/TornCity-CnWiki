import requests
import inspect
import json

FEISHU_SHARE_DATA_FOLDER_TOKEN = ""
FEISHU_ENERGY_SPREADSHEET_TOKEN = "IVWwsAYmlh7cvetyQiZcmQlHnwh"

FEISHU_APP_ID = "cli_a30f04cbb0f9500c"
FEISHU_SECRET_TOKEN = "XxPIRsJ1TzAUe4Q8iz7J4dcmjS0vcAwP"

def load_cred_json():
    global FEISHU_APP_ID, FEISHU_SECRET_TOKEN, FEISHU_ENERGY_SPREADSHEET_TOKEN, FEISHU_SHARE_DATA_FOLDER_TOKEN
    with open("./feishu_cred.json", "r") as f:
        data = json.loads(f.read())
        FEISHU_APP_ID = data["FEISHU_APP_ID"]
        FEISHU_SECRET_TOKEN = data["FEISHU_SECRET_TOKEN"]
        FEISHU_ENERGY_SPREADSHEET_TOKEN = data["FEISHU_ENERGY_SPREADSHEET_TOKEN"]
        FEISHU_SHARE_DATA_FOLDER_TOKEN = data["FEISHU_SHARE_DATA_FOLDER_TOKEN"]


def column_index(column_string):
    index = 0
    for i, c in enumerate(reversed(column_string)):
        index += (ord(c) - ord('A') + 1) * (26 ** i)
    return index


def column_name(column_index):
    name = ''
    while column_index > 0:
        remainder = (column_index - 1) % 26
        name = chr(ord('A') + remainder) + name
        column_index = (column_index - 1) // 26
    return name


def increase_col_name(column_string, step: int):
    k = column_index(column_string) + step
    return column_name(k)


class FeishuAgent:
    def __init__(self, appid=FEISHU_APP_ID, token=FEISHU_SECRET_TOKEN) -> None:
        self.appid = appid
        self.token = token
        self.tenant_token = None
        self.header = None

    def get_request_header(self):
        if not self.header:
            self.header = self.build_spreadsheet_api_header(
                self.get_tenant_token())
        return self.header

    def get_tenant_token(self):
        if self.tenant_token:
            return self.tenant_token

        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"

        header = {"Content-Type": "application/json; charset=utf-8"}

        data = {"app_id": self.appid, "app_secret": self.token}

        res = requests.post(url, json=data, headers=header).json()
        if res["code"] != 0:
            return None
        else:
            print("Get tenant token successfully, it's {}".format(
                res["tenant_access_token"]))
            self.tenant_token = res["tenant_access_token"]
            return self.tenant_token

    def build_spreadsheet_api_header(self, token):
        return {"Authorization": "Bearer " + token, "Content-Type": "application/json; charset=utf-8"}

    def handle_response(self, resp):
        calling_frame = inspect.getouterframes(inspect.currentframe(), 2)[1]
        if resp.json()["code"] == 0:
            print("{} execute successfully.".format(calling_frame.function))
        else:
            print(resp.json())
            print("{} execute failed with msg {}.".format(
                calling_frame.function, resp.json()["msg"]))
        return resp.json()["code"] == 0

    # 获取表格元数据
    def query_spreadsheet_metainfo(self, ssToken=FEISHU_ENERGY_SPREADSHEET_TOKEN):
        url = "https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/{}".format(
            ssToken)

        res = requests.get(url, headers=self.get_request_header()).json()
        return res

    # 获取根目录的Token
    def query_root_metainfo(self):
        url = "https://open.feishu.cn/open-apis/drive/explorer/v2/root_folder/meta"
        return requests.get(url, headers=self.get_request_header()).json()

    # 获取目录下所有文件Token
    def query_all_files(self, token=None):
        url = "https://open.feishu.cn/open-apis/drive/v1/files"
        header = self.get_request_header()

        file_tokens = []
        body = {}
        if token:
            body["folder_token"] = token

        while True:
            res = requests.get(url, headers=header, json=body).json()
            for file in res["data"]["files"]:
                if file["type"] in ["file", "docx", "doc", "sheet"]:
                    file_tokens.append([file["type"], file["token"]])

            if res.get("has_more", False) == False:
                break
            else:
                body["page_token"] = res["next_page_token"]

        return file_tokens

    # 删除根目录下所有文件
    def clear_all_files(self):
        root_token = self.query_root_metainfo()
        file_tokens = self.query_all_files(root_token)

        for type_, token in file_tokens:
            url = "https://open.feishu.cn/open-apis/drive/v1/files/{}?type={}".format(
                token, type_)
            res = requests.delete(
                url, headers=self.get_request_header()).json()
            if res["code"] == 0 and res["msg"] == "success":
                print("Delete {} successfully".format(token))
            else:
                print("Delete {} failed with msg {}".format(token, res["msg"]))

    # 寻找是否存在该文件
    def find_spreadsheet(self, filename):
        root_token = self.query_root_metainfo()
        tokens = self.query_all_files(token=root_token)
        res = []
        for token_tuple in tokens:
            if token_tuple[0] != "sheet":
                continue
            token = token_tuple[1]
            meta_info = self.query_spreadsheet_metainfo(ssToken=token)
            if meta_info["data"]["spreadsheet"]["title"] == filename:
                res.append(token)
        return res

    # 创建表格文件，位于根目录下
    def create_spreadsheet(self, filename):
        token = self.find_spreadsheet(filename)
        if token:
            return token[0]

        url = "https://open.feishu.cn/open-apis/sheets/v3/spreadsheets"
        body = {"title": filename, "folder_token": FEISHU_SHARE_DATA_FOLDER_TOKEN}

        res = requests.post(
            url, json=body, headers=self.get_request_header()).json()
        if res["code"] != 0:
            print("Create spreadsheet {} failed with msg {}".format(
                filename, res["msg"]))
            return None
        else:
            return res["data"]["spreadsheet"]["spreadsheet_token"]

    # 开放链接阅读权限
    def update_open_access_level(self, type_="sheet", ssToken=FEISHU_ENERGY_SPREADSHEET_TOKEN):
        url = "https://open.feishu.cn/open-apis/drive/v2/permissions/{}/public?type={}".format(
            ssToken, type_)
        header = self.get_request_header()
        body = {
            "external_access_entity": "open",
            "security_entity": "anyone_can_view",
            "link_share_entity": "anyone_readable",
            "copy_entity": "anyone_can_view"
        }

        res = requests.patch(url, headers=header, json=body).json()

        if res["code"] == 0:
            print("Open access for {} successfully".format(ssToken))
        else:
            print("Open access failed with {}".format(res["msg"]))

    # 获取所有工作表信息
    def get_sheet_info(self, ssToken=FEISHU_ENERGY_SPREADSHEET_TOKEN):
        url = "https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/{}/sheets/query".format(
            ssToken)
        res = requests.get(url, headers=self.get_request_header()).json()

        return res

    # 获取对应工作表名的工作表ID
    def get_sheet_id(self, sheetname, ssToken=FEISHU_ENERGY_SPREADSHEET_TOKEN):
        res = self.get_sheet_info(ssToken=ssToken)
        for sheet_data in res["data"]["sheets"]:
            if sheet_data["title"] == sheetname:
                return sheet_data["sheet_id"]

        return None

    # 创建工作表，返回工作表ID
    def create_sheet(self, sheetname, ssToken=FEISHU_ENERGY_SPREADSHEET_TOKEN):
        sId = self.get_sheet_id(sheetname=sheetname, ssToken=ssToken)
        if sId:
            return sId

        url = "https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/{}/sheets_batch_update".format(
            ssToken)
        header = self.get_request_header()

        body = {
            "requests": [
                {
                    "addSheet": {
                        "properties": {
                            "title": sheetname
                        }
                    }
                }
            ]
        }

        res = requests.post(url, headers=header, json=body)
        self.handle_response(res)
        return res.json()["data"]["replies"][0]["addSheet"]["properties"]["sheetId"]

    # 删除工作表
    def _delete_sheet(self, sToken, ssToken):
        url = "https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/{}/sheets_batch_update".format(
            ssToken)
        header = self.get_request_header()

        body = {
            "requests": [
                {
                    "deleteSheet": {
                        "sheetId": sToken
                    }
                }
            ]
        }
        res = requests.post(url, headers=header, json=body)
        return self.handle_response(res)
    
    def delete_all_sheet(self, ssToken=FEISHU_ENERGY_SPREADSHEET_TOKEN):
        res = self.get_sheet_info(ssToken)
        for sheet_data in res["data"]["sheets"]:
            self._delete_sheet(sheet_data["sheet_id"], ssToken)
        

    # 冻结工作表行数
    def frozen_sheet_N_line(self, sToken, rows, cols, ssToken=FEISHU_ENERGY_SPREADSHEET_TOKEN):
        url = "https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/{}/sheets_batch_update".format(
            ssToken)
        header = self.get_request_header()

        body = {
            "requests": [
                {
                    "updateSheet": {
                        "properties": {
                            "sheetId": sToken,
                            "frozenRowCount": rows,
                            "frozenColCount": cols
                        }
                    }
                }
            ]
        }

        res = requests.post(url, headers=header, json=body)
        return self.handle_response(res)

    # 更新表格数据，填入左上角坐标如"A1"和待写入数据
    def update_sheet(self, sId, start_col, start_row, data, ssToken=FEISHU_ENERGY_SPREADSHEET_TOKEN):
        row_num = len(data)
        col_num = len(data[0])

        end_row = start_row + row_num
        end_col = column_name(column_index(start_col) + col_num)

        url = "https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/{}/values".format(
            ssToken)
        header = self.get_request_header()
        body = {
            "valueRange": {
                "range": "{}!{}{}:{}{}".format(sId, start_col, start_row, end_col, end_row),
                "values": data  # 必须是二维数组
            }
        }
        res = requests.put(url, headers=header, json=body)
        return self.handle_response(res)

    # 合并单元格
    def merge_cells(self, sId, start_col, start_row, stop_col, stop_row, ssToken=FEISHU_ENERGY_SPREADSHEET_TOKEN):
        url = "https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/{}/merge_cells".format(
            ssToken)
        header = self.get_request_header()
        body = {
            "range": "{}!{}{}:{}{}".format(sId, start_col, start_row, stop_col, stop_row),
            "mergeType": "MERGE_ALL"
        }

        res = requests.post(url, headers=header, json=body)

        return self.handle_response(res)

    def set_cell_style(self, sId, start_col, start_row, stop_col, stop_row, property, ssToken=FEISHU_ENERGY_SPREADSHEET_TOKEN):
        """
        @property: dict
            bold:       bool        True/False
            fontSize:   int         10
            formatter:  string      @/0/#,##0/0%/0.00%
            hAlign:     bool        True/False
            vAlign:     bool        True/False
            borderType: string      
            borderColor:string      
        """

        url = "https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/{}/style".format(
            ssToken)
        header = self.get_request_header()
        ranges = "{}!{}{}:{}{}".format(
            sId, start_col, start_row, stop_col, stop_row)

        body = {
            "appendStyle": {
                "range": ranges,
                "style": {
                    "font": {
                        "bold": property.get("bold", False),
                        "fontSize": "{}pt/1.5".format(property.get("fontSize", "12"))
                    },
                    "formatter": property.get("formatter", ""),
                    "hAlign": property.get("hAlign", 1),
                    "vAlign": property.get("vAlign", 1),
                    "foreColor": property.get("foreColor", "#000000"),
                    "borderType": property.get("borderType", "NO_BORDER"),
                    "borderColor": property.get("borderColor", "#000000")
                }
            }
        }

        res = requests.put(url=url, headers=header, json=body)
        return self.handle_response(res)


if __name__ == "__main__":
    Agent = FeishuAgent()
    title = "EnergyReport-WE"
    Agent.delete_all_sheet()
    # token = [Agent.create_spreadsheet(title)]
    # res = Agent.update_open_access_level(ssToken=token[0])