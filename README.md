# Emploid

**Emploid** is a Python package designed to simplify the automation of web, Android, and Windows processes. With a focus on ease of use and flexibility, Emploid is the perfect tool for anyone looking to streamline repetitive tasks.

---

## Features

- **Web Automation**: Automate browser tasks such as form submissions, web scraping, and more.
- **Android Automation**: Control Android devices for app testing, UI interaction, and task automation.
- **Windows Automation**: Manage desktop applications, simulate keyboard/mouse input, and automate system processes.

---

## Installation

Install Emploid via pip:

```bash
pip install emploid
```

## Module Import

You import emploid into your .py files like this:

```bash
from emploid.emploid import Emploid
from emploid.constants import *
```

## Web Automation
**Prerequistes:**
* You must download [Chromedriver](https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.87/win64/chromedriver-win64.zip) and place it under a "drivers" folder in your working directory.
* Make sure the Chromedriver version is the same as your chrome browser version.

**Example code:**
```bash
emp = Emploid(_driver_type=SETTINGS_USE_SELENIUM) #init emploid for web
emp.get("https://google.com") #go to google.com
emp.click("/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div") #click on popup accept button
emp.submit("hello world", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea") #search for the string "hello world"
emp.pause() #pause so that the browser window does not terminate
```
---

## Android Automation
**Example code:**
```bash
emp = Emploid(_driver_type=SETTINGS_USE_APPIUM)
emp.appium_connect()

emp.activate_app("com. android. chrome")
emp.click("""...""", _tries=10)
emp.input_into("hello", """//android.widget.EditText""", _tries=10)
emp.pause() #pause so that the browser window does not terminate
```
---

## Windows Automation
**Example code:**
```bash
emp = Emploid(_driver_type=SETTINGS_USE_PYAUTOGUI) #init emploid for windows
emp.get("https://google.com") #go to google.com
emp.click("/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div") #click on popup accept button
emp.submit("hello world", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea") #search for the string "hello world"
emp.pause() #pause so that the browser window does not terminate
```
---


