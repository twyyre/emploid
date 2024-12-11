from emploid.constants import *

def determine_driver_type(_driver_type):
    if (_driver_type==SETTINGS_USE_APPIUM): 
        #APPIUM IMPORTS
        from appium import webdriver as AppiumDriver
        from appium.webdriver.common.appiumby import AppiumBy as By
        from appium.options.android import UiAutomator2Options # Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
        from appium.options.common import AppiumOptions
        # from appium.webdriver.common.touch_action import TouchAction as AppiumAction
        from appium.webdriver.extensions.android.nativekey import AndroidKey as ak
        keys = Keys
        return AppiumDriver
    elif (_driver_type==SETTINGS_USE_SELENIUM): 
        #SELENIUM IMPORTS
        from selenium import webdriver as SeleniumDriver
        from selenium.webdriver.support import expected_conditions as SeleniumConditions
        from selenium.webdriver.support.ui import WebDriverWait as SeleniumWait
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        from selenium.webdriver import ActionChains
        from selenium.webdriver.chrome.remote_connection import ChromeRemoteConnection
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By as SeleniumBy
        from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        from selenium.webdriver.firefox.service import Service as FirefoxService
        from selenium.webdriver.support.ui import Select #used to deal with select HTML elements
        import selenium.common.exceptions
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options as chromeOptions
        return SeleniumDriver.Chrome
    elif (_driver_type==SETTINGS_USE_PYAUTOGUI): 
        #PYAUTOGUI IMPORTS
        import pyautogui as pa
        import pyperclip as clip
        keys = pa.KEYBOARD_KEYS
        pa.set_failsafe(False)
        pa.set_delay(0.2)
        element_count = 0
        steps = []
        return pa