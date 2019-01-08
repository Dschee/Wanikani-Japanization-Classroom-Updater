# Wanikani Japanization Classroom Updater

## Introduction

This project is an updater for the Wanikani japanization classroom forum thread ; it updates the spreadsheet with the
data from the Wanikani user profiles.

## Installation
- Clone the project
- Install python 3 and use `pip3 install -r requirements.txt` to install required dependencies
- Enable the google sheets API on your account (https://developers.google.com/sheets/api/quickstart/python)
- Download the "credentials.json" file and put it in the same folder as the project
- Go to the "spreadsheet_handler" file and edit the `SPREADSHEET_ID` with the ID of the spreadsheet you want to edit 
(it needs to be formatted the same way as the classroom one)
- Execute `python3 main.py`
- Your browser might ask for your permission to utilize one of your account.
The spreadsheet should be updated with everybody's level and items !
