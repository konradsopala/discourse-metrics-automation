# Discourse Metrics Google Sheets Automation

## Context

As every team, you probably want to track where you go, what value you provide and also make data-driven decisions. For quite a while now, you’ve been gathering certain metrics that provided you but also outside-team stakeholders on how things progress in the your Land. It all looks perfect!

It's a Python script that when run on a monthly basis fetches Metrics data from the previous month and fills in that data to the Metrics spreadsheet by inserting a column with data on the left hand side. It doesn't matter when it is run in the month. Basically when you want the data for the previous month you can run it between the first and last day of current month. Apart from two elements, the digestability and ease of analysing that data by various stakeholders is far from perfect + all that data needed to be fetched manually by following this exact flow:

* Going to Metrics spreadsheet
* Clicking on each metric to be redirected to Data Explorer
* Run the query
* Copy-paste the result to the Metrics spreadsheet
* Re-do the process for all metrics that have associated queries

Then some spreadsheet formulas did their job and after all that everything was in place. Quite a lot of room for human error! That’s why you should decide to improve that!



## Prerequisites

* Have Python installed on your computer. You can download it [here](https://www.python.org/downloads/).
* Have Google Client Library installed
   * You can install it from your IDE terminal once you have all files ready
   * ```pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib```

## Credentials

### Google Sheets API

All the references that were used for the automation implementation were official Google Sheets API v4 docs that can be found here:
* General info on Google Sheets API [LINK]
* Reading & Writing Cell Values [LINK]

Only official Google client libraries were used for that implementation. Following steps were taken to implement the automation:
* Create a project in Google Developer Console
* Enable Google Sheets API in “Explore and enable APIs” section
* Create credentials for hitting the API (Credentials → Service Accounts → Manage service accounts)
* Create service account in the mentioned above section
* Set service account permissions to Project → Editor so you can actually modify the sheet
* Go to the Metrics spreadsheet and share it with the email that just got created in service account section of Google Developer Console
* Open the service account we just created and in the Keys section add key (credentials in a form of .json file)
* Develop the script code for the automation

In order to run the script, you'll need the credentials for Google Sheets API. To get them you need to follow these steps:

* Login to https://console.cloud.google.com/ with your Auth0 email
* Select **MetricsBoard** project at the top
* Go to **APIs & Services** and then **Credentials**
* In the **Service Accounts** section click on the email that is already there
* In the **Keys** section click on **Add Key** and then **Create new key**
* Select **JSON** as key type and download the file with your credentials
* Save the credentials file in the same directory where the script.py and config.py files are

### Discourse

From the Discourse side of things, you'll need API_USERNAME and API_KEY that you can get from the admin dashboard API section. You should store them in the config.py file.

## How to run it?

As of now there is a semi-automatic way to run the script from your IDE, having it configured once. 

### The semi-automatic way with IDE

* Download script.py and config.py to your machine
* Have one directory that will store those files as well as your credentials file
* Make sure to fill in all the details in config.py file. Needed things are marked with # TODO: 
* Run script.py from your IDE and see things happening inMetrics Spreadsheet 🎉
