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
# emp.appium_server_start()
emp.appium_connect()

print("started test")
# emp.activate_app('com.lib.libank')
emp.activate_app('com.android.chrome')

search_bar = emp.promise_element(_ent="com.android.chrome:id/search_box_text", _tries=100, _delay=5)

if(search_bar):
    emp.input_into(_str="ayoubqa", _elm=search_bar)

# sleep(2)
# emp.appium_emulator_stop()
# emp.appium_server_stop()
exit()