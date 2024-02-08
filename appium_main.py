from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy as By
from appium.options.android import UiAutomator2Options # Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
from appium.options.common import AppiumOptions
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.nativekey import AndroidKey as ak
from selenium.webdriver.common.keys import Keys
import subprocess as sp
import sys
import os
from constants import *
from emploid import Emploid

emp = Emploid(_driver_type=SETTINGS_USE_APPIUM)

# emp.appium_emulator_start()
emp.appium_server_start()
emp.appium_connect()
emp.check_installed('com.facebook.')
print("started test")
# emp.activate_app('com.lib.libank')
# emp.activate_app('com.android.chrome')
if(not emp.check_installed(APP_FACEBOOK_LITE)):
    print("app is not installed. Installing...")
    emp.driver.install_app(r'C:\\Users\\a.almuntasir\\emploidBPV2\\apks\\fbl.apk')
else:
    print("app already installed.")
emp.activate_app(APP_FACEBOOK_LITE)
sleep(5)
emp.display_elements()

# emp.click(_elm="com.android.packageinstaller:id/permission_deny_button", _tooltip="click DENY")

emp.driver.tap([(309, 578)]) #deny
sleep(1)

emp.driver.tap([(160, 180)])
sleep(1)
active_element = emp.driver.switch_to.active_element
active_element.send_keys("needyrelish1@pretreer.com")
sleep(1)

emp.driver.tap([(235, 290)])
active_element = emp.driver.switch_to.active_element
active_element.send_keys("lypybot2022")
sleep(1)

emp.driver.tap([(262, 367)]) #login
sleep(1)

emp.driver.tap([(304, 584)]) #deny


# sleep(2)
# emp.appium_emulator_stop()
# emp.appium_server_stop()
exit()