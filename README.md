# Emploid

**Emploid** is a Python package designed to simplify the automation of web, Android, and Windows processes. With a focus on ease of use and flexibility, Emploid is the perfect tool for developers looking to streamline repetitive tasks.

---

## Features

- **Web Automation**: Automate browser tasks such as form submissions, web scraping, and more.
- ```bash
  from emploid.emploid import Emploid
  from emploid.constants import *
  
  emp = Emploid(_driver_type=SETTINGS_USE_SELENIUM)
  emp.get("https://google.com")
  emp.click("/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div")
  emp.submit("hello world", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
  emp.pause()
- **Android Automation**: Control Android devices for app testing, UI interaction, and task automation.
- **Windows Automation**: Manage desktop applications, simulate keyboard/mouse input, and automate system processes.

---

## Installation

Install Emploid via pip:

```bash
pip install emploid
