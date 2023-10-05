# MoneyHelper DTT Automated Tests

- Public repo, do not store any senstive info, keys or other goodies in code.
- Unlike other projects, this will be the 1st to not include end to end tests, instead focussing on behaviour driven development.

## Prerequistes

- Install [Python](https://www.python.org/downloads/)
- Grab the webdriver for your browser (for local runs) - [Chrome](https://googlechromelabs.github.io/chrome-for-testing/) [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## To get up and running

- Clone this repo
- cd into the project directory
- If on windows, place the Edge webdriver (msedgedriver.exe) in selenium-azure-dtt/Webdrivers/
- If on mac, place the Chrome webdriver (chromedriver) in selenium-azure-dtt/Webdrivers/
- Please note: The webdriver you use locally can be defined in environment.py and is entrirely flexible
- Initialise the Python virtual env Windows: ``python -m venv .venv`` MAC: ``python3 -m venv .venv``
- Actiave the virtual env - Windows: ``.venv/Scripts/Activate`` MAC: ``source .venv/bin/activate``
- Install dependencies using pip: ``pip install -r requirements.txt``
- Run tests with ``behave``
