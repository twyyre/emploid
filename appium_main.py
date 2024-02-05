from selenium.webdriver.common.keys import Keys
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

emp.appium_emulator_start()
emp.appium_server_start()
emp.appium_connect()

print("started test")
emp.activate_app('com.lib.libank')

print("sleeping...")
sleep(10)
#
# from classes.element_class import EmploidElement as e
# result = e(emp, """//*[@text="uinpt"]""")
# print(result)
# exit()
# emp.click("""//*[@text="uinpt"]""")
username_inpt = emp.input_into("ayoubqa", """//*[@text="uinpt"]""")

#
password_inpt = emp.find_element("""//*[@text="pinpt"]""")
password_inpt.click()
sleep(1)
password_inpt.clear()
password_inpt.send_keys("99889988")
#
allelms = emp.locate_all()
for elm in allelms:
    if("button" in elm.get_attribute("class").lower()):
        elm.click()

allelms = emp.locate_all()
for elm in allelms:
    print(elm.get_attribute('class'), elm.text)


# check = emp.click(element_password_show_btn, "click on show password")

# check = emp.input_into(user_name, element_username_input, "input username")


# sleep(2)
# emp.appium_emulator_stop()
# emp.appium_server_stop()
exit()