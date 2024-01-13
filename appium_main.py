import unittest
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


emp = Emploid()

# emp.appium_server_start()
emp.appium_emulator_start()
emp.appium_connect()

emp.appium_server_stop()
# emp.appium_emulator_stop()

print("started test")
emp.driver.activate_app('com.android.chrome')

sleep(2)

buttons = emp.driver.find_elements(By.XPATH, "//*")
for btn in buttons:
    btn_class = btn.get_attribute('class')
    # print(btn_class)
    if('search' in btn.text.lower()):
        try:
            print("----", btn.text)
            btn.send_keys("http://10.10.20.46:6001")
            emp.driver.press_keycode(ak.ENTER)
        except:
            pass
        break
        # sleep(2)
        # btn.send_keys(Keys.ENTER)
        # action = TouchAction(driver)
        # action.press(x=10, y=10).release().perform()
    
sleep(2)

buttons = emp.driver.find_elements(By.XPATH, "//*[contains(@class, 'android.view.View')]")
for btn in buttons:
    try:
        if("write a test" in btn.text.lower()):
            # btn_class = btn.get_attribute('class')
            # print(btn_class, "[", btn.text, "]")
            btn.click()
    except:
        pass

action = TouchAction(emp.driver)
elements = emp.driver.find_elements(By.XPATH, "//*")
emp.driver.swipe(470, 1400, 470, 0, 400)
emp.driver.swipe(470, 1400, 470, 0, 400)
emp.driver.swipe(470, 1400, 470, 0, 400)

# action.press(elements[20]).perform()
# action.move_to(elements[-1]).perform()
# action.release().perform()
    # if('search' in btn.text.lower()):
    #     try:
    #         print("----", btn.text)
    #         btn.send_keys("how to use appium with python")
    #         driver.press_keycode(ak.ENTER)
    #     except:
    #         pass
    #     break  
# driver.press_button('back')



# os.system(f"taskkill /PID {emp.emu.pid} /f")
# os.system(f"taskkill /PID {emp.appium_server.pid} /f")

print("test finished")
exit()