# Adidas QA Challenge

## Description
The application tests the general function of a debug app, which is saved in app folder of repo.

## Tech Stack
- Python  
- Pytest
- Appium

## Test Scenarios
- User can add review for a product and review is shown immediately in product page after it is saved. (**Failed**)
- User can add review for a product and review is shown in product page after app is relaunched. (**Passed**)
- User can add review with only rating and without message. (**Passed**)
- Elements are not shown in homepage when app is launched during internet disconnection. (**Passed**)
- User can not save review during internet disconnection and review is not shown in product page. (**Passed**)
- User can search for a product by its name. (**Not implemented, Failed**)
- User can search for a product by its description. (**Not implemented, Failed**)
- Search result is empty when search keyword is neither in product name nor description. (**Not implemented, Failed**)
- User can go to Setting page. (**Not implemented, Failed**)

## Running the test
### Prerequisites
- a real or virtual android device is connected to the system;
- python is installed;  
- appium server is on;   
- if appium server address is not http://localhost:4723/wd/hub, and environment variable APPIUM_SERVER_ADDRESS needs
to be set as the address  
e.g.  
in windows: $ set APPIUM_SERVER_ADDRESS={server address},   
in linux: $ export APPIUM_SERVER_ADDRESS={server address}

### Commands:
### in Windows:
- $ python3 -m venv venv
- $ venv\Scripts\activate.bat
- $ pip install -r requirements.txt
- $ pytest
### in Linux:
- $ python3 -m venv venv
- $ source venv/bin/activate
- $ pip install -r requirements.txt
- $ pytest

All the commands should be executed in root directory of the repo. 
A test report is generated in report folder after the test is finished.
