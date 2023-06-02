from google.oauth2 import service_account
from googleapiclient.discovery import build

class GoogleSheetAgent():
    def __init__(self, credentials=None):
        creds = service_account.Credentials.from_service_account_file(credentials)
        self.service = build("sheets", "v4", credentials=creds)

    def update(self, sheetID="19935qbJgQONgggFQBm80nBxOAjTGnL7_pEjslfzi7q8", write_array = [[]], sheet_name="CCRC", valueInputOptions="RAW"):
        if not self.check_sheet_existence(sheetID, sheet_name):
            self.create_sheet(sheetID, sheet_name)

        body = {"values": write_array}
        range = sheet_name + "!A1"
        result = self.service.spreadsheets().values().update(spreadsheetId=sheetID,
                                                             range=range, valueInputOption=valueInputOptions, body=body).execute()

        return '{0} cells updated.'.format(result.get('updatedCells')), "https://docs.google.com/spreadsheets/d/{}".format(sheetID)
    
    def check_sheet_existence(self, sheetID, sheet_name):
        sheet_exists = False
        spreadsheet = self.service.spreadsheets().get(spreadsheetId = sheetID).execute()
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
