# TODO: Read the instructions
# SCENARIO: List all the Data Explorer queries you have here for your team-mates future know-how
'''
Metrics are executed in this order as they are stored in such order in Metrics Spreadsheet

153 - Some Random Data Explorer Query Name One: https://yourDiscourseForumSite.com/admin/plugins/explorer?id=153
154 - Some Random Data Explorer Query Name Two: https://yourDiscourseForumSite.com/admin/plugins/explorer?id=154
150 - Some Random Data Explorer Query Name Two: https://yourDiscourseForumSite.com/admin/plugins/explorer?id=150
...

All queries IDs in the order they are stored in Metrics Spreadsheet:
[153, 154, 150, 156, 157, 110, 170, 175, 235, 324, 105, 98]

# TODO: It's worth specifying the Data Explorer output format so that all queries outputs the same results format
Data Explorer Queries Output Format: [['10-2020', 987], ['11-2019', 387], ...]]
'''

# DATA EXPLORER QUERIES IDS
QUERIES_IDs = [153, 154, 150, 156, 157, 110, 170, 175, 235, 324, 105, 98]

# GOOGLE API HANDLING

# Spreadsheet ID is this long string in spreadsheet URL
# TODO: Fill in Spreadsheet ID
SPREADSHEET_ID = '<SPREADSHEET_ID>'

SERVICE_ACCOUNT_FILE = 'credentials.json'
SHEETS_API_SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Sheet IDs are the numbers at the end of the URL when we access certain sheet
SHEETS_IDs = {
    'YourSheetOne': 865328430,
    'YourSheetTwo': 2898681310,
    'YourSheetThree': 1006397104,
}

# Spreadsheet rows into which data should be inserted
METRICS_RANGES = {
    'Metrics': 'Metrics!C3:C14',
}

# DISCOURSE API HANDLING

DATA_EXPLORER_QUERY_ENDPOINT = 'https://yourDiscourseForumSite.com/admin/plugins/explorer/queries/<QUERY_ID>/run'

# TODO: Fill in API_USERNAME and API_KEY
API_USERNAME = '<DISCOURSE_API_USERNAME>'
API_KEY = '<DISCOURSE_API_KEY>'
HEADERS = {'Content-Type': 'multipart/form-data', 'Api-Key': API_KEY, 'Api-Username': API_USERNAME}
