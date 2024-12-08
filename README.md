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

```python
pip install emploid
```

## Module Import

You import emploid into your .py files like this:

```python
from emploid.emploid import Emploid
from emploid.constants import *
```

## Web Automation
**Prerequistes:**
* Go to chrome://version from your chrome browser address bar and check the version of chrome installed on your machine.
* Download the same version of [Chromedriver](https://googlechromelabs.github.io/chrome-for-testing/) as your browser and place it under a "drivers" folder in your working directory.
* You can extract the XPATH of an element [from the browser](https://stackoverflow.com/questions/3030487/is-there-a-way-to-get-the-xpath-in-google-chrome#:~:text=All%20above%20answers%20are%20correct%20here%20is%20another%20way%20with%20screenshot%20too.) and pass it to methods such as emp.click(), emp.input_into() and emp.submit()
* At this point you can run your emploid program.

**Example code:**
```python
emp = Emploid(_driver_type=SETTINGS_USE_SELENIUM) #init emploid for web
emp.get("https://google.com") #go to google.com
emp.click("/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div") #click on popup accept button
emp.submit("hello world", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea") #search for the string "hello world"
emp.pause() #pause so that the browser window does not terminate
```
---

## Android Automation
**Prerequistes:**
* Download an emulator that allows adb connection like [MeMu](https://www.memuplay.com/download.html).
* You must install [Appium server](https://appium.io/docs/en/2.0/quickstart/install/)
```javascript
npm i --location=global appium
```
* You must install the [UiAutomator2 Driver](https://appium.io/docs/en/2.0/quickstart/uiauto2-driver/)
```javascript
appium driver install uiautomator2
```
* Now run appium from the command line:
```javascript
appium
```
* Use [Appium Inspector](https://github.com/appium/appium-inspector/releases) to grab widget identifiers to be able to interact with the. Such as XPATH.
* Now you can run your emploid program.

**Example code:**
```python
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
```python
emp = Emploid(_driver_type=SETTINGS_USE_PYAUTOGUI)
```
This section will be documented in the future.
---


