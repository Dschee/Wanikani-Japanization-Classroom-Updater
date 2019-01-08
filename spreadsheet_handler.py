from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Read/Write scope
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

# ID of the spreadsheet to check and edit
SPREADSHEET_ID = '1m9JI9sywChoSvdfuq-fsSct241sAUtCqhmZIbcXIV4c'
# Ranges of the names and the values to edit
NAME_RANGE = 'Sorted by Start Date!B9:B'
ITEMS_RANGE = 'Sorted by Start Date!C9:H'


class SpreadsheetHandler:
    def __init__(self):
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('sheets', 'v4', http=creds.authorize(Http()))
        self.sheet = service.spreadsheets()

    def get_profile_names(self):
        result = self.sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=NAME_RANGE).execute()
        values = result.get('values', [])
        names = []
        for row in values:
            if row[0]:
                names.append(row[0])
        return names

    def set_profiles_items(self, items):
        edit_values = []
        for item in items:
            edit_values.append([item['level'], item['apprentice'], item['guru'], item['master'], item['enlightened'], item['burned']])
        edit_body = {'values': edit_values}
        self.sheet.values().update(spreadsheetId=SPREADSHEET_ID, range=ITEMS_RANGE,
                                   valueInputOption='USER_ENTERED', body=edit_body).execute()
