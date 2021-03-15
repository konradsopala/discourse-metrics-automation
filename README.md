![](/Assets/CoverPhoto.png)

# Discourse Metrics Google Sheets Automation

As every team, you probably want to track where your Discourse community goes, what value you provide by maitnaining it and also make data-driven decisions. For quite a while now, you’ve been gathering certain metrics as you've been utilising [Data Explorer plugin](https://www.discourse.org/plugins/data-explorer.html) that provided you but also outside-team stakeholders on how things progress in your Land. Everything has been stored in Google Sheets. What can you do better then?!

## Intro

Automate that process not to waste you time anymore on manual fetching and inserting each metric! Get yourself a Python script that when run on a monthly basis fetches Data Explorer metrics data from the previous month and fills in that data to your Metrics spreadsheet by inserting a column with that data on the left hand side, so you can eassily see the most up to date data immediately once you open the sheeet. 


## Context

Here's the scenario you've probably been going through until you found this repo:

* Going to Metrics spreadsheet
* Clicking on each metric to be redirected to Data Explorer
* Runninh the query
* Copy-pasting the result to the Metrics spreadsheet
* Re-doing the process for all metrics that have associated queries

Then some spreadsheet formulas did their job and after all that everything was in place. Quite a lot of room for human error! That’s why you should decide to improve that!


## Prerequisites

* From the Discourse side of things, you'll need API_USERNAME and API_KEY that you can get from the admin dashboard API section. You should store them in the config.py file
* Have Python installed on your computer. You can download it [here](https://www.python.org/downloads/).
* Have Google Client Library installed
   * You can install it from your IDE terminal once you have all files ready
   * ```pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib```


## Configuration

### Google Sheets API

All the references that were used for the automation implementation were official Google Sheets API v4 docs that can be found here:
* [General info on Google Sheets API](https://developers.google.com/sheets/api)
* [Reading & Writing Cell Values](https://developers.google.com/sheets/api/guides/values)

Only official Google client libraries were used for that implementation. Following steps were taken to implement the automation:
* Create a project in Google Developer Console
* Enable Google Sheets API in “Explore and enable APIs” section
* Create credentials for hitting the API (Credentials → Service Accounts → Manage service accounts)
* Create service account in the mentioned above section
* Set service account permissions to Project → Editor so you can actually modify the sheet
* Go to your metrics spreadsheet and share it with the email that just got created in service account section of Google Developer Console
* Open the service account we just created and in the Keys section add key (credentials in a form of .json file)

If you'd like others in your team to run the script, they'll need the credentials for Google Sheets API. To get them you need to follow these steps:

* Login to https://console.cloud.google.com/ with your email
* Select your project at the top
* Go to **APIs & Services** and then **Credentials**
* In the **Service Accounts** section click on the email that is already there
* In the **Keys** section click on **Add Key** and then **Create new key**
* Select **JSON** as key type and download the file with your credentials
* Save the credentials file in the same directory where the script.py and config.py files are


## How to run it?

How you run it is pretty much up to you. You can configure it to be run automatically every month or semi-automatically, which means you'll be running the script each month. The important part is the right data format of your Data Explorer queries. If each of your query returns the results by month, then you will need to run the script betweetn first and last day of the month to fetch the data of the previous month. That's it! For more details check the script.py and config.py files!

## Automation Core

Basically the script fetches all your metrics from Data Explorer queries of yours and stores them in an array. It is done by running each query programatically by sending appropriate requests. Once that part is finished it inserts a column on the left side of your spreadhseet and fills in that data (so you can see all the months from most up to date to the oldest one on the right hand side). For more info on the functioning aspect of the automation just go to the code files!

![](/Assets/SampleScreenshot.png)
