# Imports
import json
import requests
import config
import datetime
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Global Variables
METRICS = []


# Store metrics date as the first element of the metrics array
# SCENARIO: Metrics are added to the spreadsheet with the first element which is the reporting month
def handle_spreadsheet_date_column():
    today = datetime.date.today()
    first = today.replace(day=1)
    report_date = first - datetime.timedelta(days=1)
    formatted_report_date = report_date.strftime("%b %Y")
    METRICS.append(formatted_report_date)


# Run metrics Data Explorer queries and store the results in an array
# SCENARIO: All the metrics you have have their related Data Explorer queries that are run here
def fetch_queried_metrics():
    for query_id in config.QUERIES_IDs:
        query_endpoint = config.DATA_EXPLORER_QUERY_ENDPOINT.replace("<QUERY_ID>", str(query_id))
        request = requests.post(url=query_endpoint, headers=config.HEADERS)
        response = json.loads(request.text)
        response_rows = response["rows"]
        query_metric = response_rows[1][2]
        METRICS.append(query_metric)


# Save metrics values to Metrics Google Sheet
# SCENARIO: Save the previously fetched metrics with reporting month to specific column in your spreadsheet
def save_metrics_to_sheets(range, sheetID):

    # Configure access between Google Sheets API and the spreadsheet
    credentials = service_account.Credentials.from_service_account_file(
        config.SERVICE_ACCOUNT_FILE, scopes=config.SHEETS_API_SCOPES)
    service = build('sheets', 'v4', credentials=credentials)

    # Prepare proper input value format for the Google Sheets API
    metrics = []
    for metric in METRICS:
        value = [metric]
        metrics.append(value)

    # Body of the request to insert a column into a spreadsheet
    request_body = {
        'requests': [
            {
                'insertDimension': {
                    'range': {
                        'sheetId': sheetID,
                        'dimension': 'COLUMNS',
                        'startIndex': 2,
                        'endIndex': 3
                    },
                    'inheritFromBefore': False
                }
            }
        ]
    }

    # Insert new column C for last month data
    service.spreadsheets().batchUpdate(
        spreadsheetId=config.SPREADSHEET_ID,
        body=request_body
    ).execute()

    # Update spreadsheet with last month data
    service.spreadsheets().values().update(
        spreadsheetId=config.SPREADSHEET_ID,
        range=range,
        valueInputOption='USER_ENTERED',
        body={'values': metrics}
    ).execute()


# Run all the functions defined above
def main():
    handle_spreadsheet_date_column()
    fetch_queried_metrics()
    save_metrics_to_sheets(config.METRICS_RANGES['Metrics'], config.SHEETS_IDs['Metrics'])


main()
