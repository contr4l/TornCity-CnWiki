from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime


class GoogleSheetAgent():
    def __init__(self, credentials=None):
        self.credentials = credentials

    def validate(self):
        self.creds = service_account.Credentials.from_service_account_file(
            self.credentials)
        self.service = build("sheets", "v4", credentials=self.creds)
        self.drive = build("drive", "v3", credentials=self.creds)

    def update(self, sheetID="19935qbJgQONgggFQBm80nBxOAjTGnL7_pEjslfzi7q8", write_array=[[]], sheet_name="CCRC", valueInputOptions="RAW"):
        if not self.check_sheet_existence(sheetID, sheet_name):
            self.create_sheet(sheetID, sheet_name)

        body = {"values": write_array}
        range = sheet_name + "!A1"
        self.service.spreadsheets().values().update(spreadsheetId=sheetID,
                                                    range=range, valueInputOption=valueInputOptions, body=body).execute()

        new_file_id = self.copy_sheet_to_new_spreadsheet(sheetID, sheet_name)
        self.share_to_anyone(new_file_id)
        return new_file_id

    def share_to_anyone(self, file_id):
        permission = {
            'type': 'anyone',
            'role': 'reader',
        }
        self.drive.permissions().create(
            fileId=file_id,
            body=permission,
            fields='id'
        ).execute()

    def get_sheet_id(self, ss_id, sheet_name):
        spreadsheet = self.service.spreadsheets().get(spreadsheetId=ss_id).execute()
        sheet_id = None
        for sheet in spreadsheet['sheets']:
            if sheet['properties']['title'] == sheet_name:
                sheet_id = sheet['properties']['sheetId']
                break
        return sheet_id

    def copy_sheet_to_new_spreadsheet(self, prev_ss_id, sheet_name):
        sheet_id = self.get_sheet_id(prev_ss_id, sheet_name)

        now_ = datetime.now()
        new_sheet_name = sheet_name + " " + now_.strftime("%Y-%m-%d")

        meta_data = {
            'properties': {
                'title': new_sheet_name
            }
        }

        response = self.service.spreadsheets().create(body=meta_data,
                                                      fields='spreadsheetId').execute()
        new_file_id = response["spreadsheetId"]

        request_body = {
            'destination_spreadsheet_id': new_file_id,
        }
        response = self.service.spreadsheets().sheets().copyTo(
            spreadsheetId=prev_ss_id,
            sheetId=sheet_id,
            body=request_body
        ).execute()

        self.delete_sheet(new_file_id, "Sheet1")
        return new_file_id

    def delete_sheet(self, ss_id, sheet_name):
        to_delete_id = self.get_sheet_id(ss_id, sheet_name)
        requests = [
            {
                "deleteSheet": {
                    "sheetId": to_delete_id,
                }
            }
        ]
        self.service.spreadsheets().batchUpdate(
            spreadsheetId=ss_id,
            body={
                "requests": requests
            }
        ).execute()

    def check_sheet_existence(self, sheetID, sheet_name):
        sheet_exists = False
        spreadsheet = self.service.spreadsheets().get(spreadsheetId=sheetID).execute()
        for sheet in spreadsheet["sheets"]:
            if sheet['properties']['title'] == sheet_name:
                sheet_exists = True
                break

        return sheet_exists

    def create_sheet(self, sheetId, sheet_name):
        requests = [
            {
                'addSheet': {
                    'properties': {
                        'title': sheet_name,
                        'gridProperties': {
                            'rowCount': 120,
                            'columnCount': 10
                        }
                    }
                }
            }
        ]

        self.service.spreadsheets().batchUpdate(spreadsheetId=sheetId,
                                                body={'requests': requests}).execute()

    def clear_all_files(self):
        results = self.drive.files().list(
            pageSize=1000, fields="nextPageToken, files(id, name)").execute()
        items = results.get("files", [])

        for item in items:
            # print(item["id"])
            try:
                self.drive.files().delete(fileId=item["id"]).execute()
            except:
                print(item["id"], " --- Failed to delete this file")

        print("Delete all files")
