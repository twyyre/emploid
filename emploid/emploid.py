#BUILTIN IMPORTS
import json
import logging
import os
from os import getcwd, listdir
from os.path import isfile, join
import platform
from random import randint
import re
import sys
from time import sleep
import time
import string
import subprocess as sp
import datetime
import inspect

#
import cv2 as cv
import numpy as np
import numpy as np
import requests

#PYAUTOGUI IMPORTS
import pyautogui as pa
import pyperclip as clip

#APPIUM IMPORTS
from appium import webdriver as AppiumDriver
from appium.webdriver.common.appiumby import AppiumBy as By
from appium.options.android import UiAutomator2Options # Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
from appium.options.common import AppiumOptions
# from appium.webdriver.common.touch_action import TouchAction as AppiumAction
from appium.webdriver.extensions.android.nativekey import AndroidKey as ak

#SELENIUM IMPORTS
from selenium import webdriver as SeleniumDriver
from selenium.webdriver.support import expected_conditions as SeleniumConditions
from selenium.webdriver.support.ui import WebDriverWait as SeleniumWait
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.remote_connection import ChromeRemoteConnection
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By as SeleniumBy
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import Select #used to deal with select HTML elements

#my modules
from emploid.constants import *
from emploid.driver import init_emploid_driver
import emploid.tools as tls
from emploid.scribe import Scribe
# from taskman import Taskman

#sql server database connection module
import pyodbc
from emploid.logdec import decorator_wrapper

logger = logging.getLogger(__name__)

class Emploid():

    @staticmethod
    def loggerd(_func, *args):
        """a decorator for logging and error handling."""
        def wrapper(*args, **kwargs):
            try:
                emp = args[0]
                try:
                    #CREATE LOG FILE-------------------------------------------
                    if(emp.create_logs_directory):
                        year = datetime.datetime.now().year
                        month = datetime.datetime.now().month
                        day = datetime.datetime.now().day
                        hour = datetime.datetime.now().hour
                        minute = datetime.datetime.now().minute
                        second = datetime.datetime.now().second
                        log_filename = f"{emp.log_path}/internal_log {year}-{month}-{day}-{hour}-{minute}-{second}.log"

                        tls.f_write(_filename=log_filename, _content="")
                        
                        logging.basicConfig(filename=log_filename, encoding='utf-8', format='%(asctime)s %(message)s', level=logger.INFO)
                    #----------------------------------------------------------
                    print("log dir created")
                    input()
                    log_message = str(f"emploid started '{_func.__name__}'").replace("'", "\"")
                    args_message = ""
                    kwargs_message = ""
                    
                    if(len(args)):
                        args_message = str(args).replace("'", "\"")
                    else:
                        args_message = 'NULL'
                        
                    if(len(kwargs)):
                        kwargs_message = str(json.dumps(kwargs)).replace("'", "\"")
                    else:
                        kwargs_message = 'NULL'
                    
                    logger.info(log_message)
                except Exception as e:
                    print("error when creating log:", e)
                
                if(LOG_TO_DB):
                    try:
                        query = f"""INSERT INTO logs (actionname, userid, message, fullerror, request, response, params, kwargs) VALUES ('{_func.__name__}', 'NULL', '{log_message}', 'NULL', 'NULL', 'NULL', '{args_message}', '{kwargs_message}');"""
                        emp.query(_query=query)
                    except Exception as e:
                        print("could not save log to DB:", e)
                    
                return _func(*args, **kwargs)
            
            except Exception as e:
                print("-----------------NORMAL ERROR-----------------")
                e = str(e).replace("'", "\"")
                print(e)
                
                if(LOG_TO_DB):
                    try:
                        emp.query(_query=f"""INSERT INTO logs (actionname, userid, message, fullerror, request, response, params, kwargs) VALUES ('{_func.__name__}', 'NULL', '-----------------NORMAL ERROR-----------------', '{e}', 'NULL', 'NULL', 'NULL', 'NULL');""")
                    except:
                        print("could not log normal error into database")
                        print(e)

                print("-----------------LOG ERROR-----------------")
                logger.exception(e)
                    
        return wrapper
        #----------------------------------------------------------
    
    #----------------------------------------------------------
    
    @loggerd
    def __init__(
            self, 
            _driver_type=SETTINGS_USE_SELENIUM,
            _autoconnect=False,
            _headless=USE_HEADLESS, 
            _incognito=USE_INCOGNITO,
            _vpn=USE_VPN, 
            _request_delay=REQUEST_DELAY,
            # _user_profile=None,
            _browser_type=BROWSER_TYPE_CHROME,
            _maximized=False,
            _window_size=None,
            _report_path=None,
            _log_path=None,
            _log_to_db=False
        ):

        self.file_path = os.path.dirname(os.path.abspath(__file__))
        self.driver_type = _driver_type
        self.create_environment_directory = False
        self.log_path = _log_path
        self.create_logs_directory = True if self.log_path else False
        self.create_reports_directory = False
        self.report_path = "./"
        self.load_entities = False
        self.log_to_db = _log_to_db
        self.logging = False
        self.driver = init_emploid_driver(self.driver_type) #Init Driver instance
        
        #SET REPORT PATH-------------------------------------------
        if(self.create_reports_directory):
            if not os.path.exists(self.report_path):
                os.makedirs(self.report_path)
        #----------------------------------------------------------

        #SET LOG PATH----------------------------------------------
        if(self.create_logs_directory):
            if not os.path.exists(self.log_path):
                os.makedirs(self.log_path)
        #----------------------------------------------------------

        #CREATE LOG FILE-------------------------------------------
        # if(self.create_logs_directory):
        #     year = datetime.datetime.now().year
        #     month = datetime.datetime.now().month
        #     day = datetime.datetime.now().day
        #     hour = datetime.datetime.now().hour
        #     minute = datetime.datetime.now().minute
        #     second = datetime.datetime.now().second
        #     log_filename = f"{self.log_path}/internal_log {year}-{month}-{day}-{hour}-{minute}-{second}.log"

        #     tls.f_write(_filename=log_filename, _content="")
            
        #     logger.basicConfig(filename=log_filename, encoding='utf-8', format='%(asctime)s %(message)s', level=logger.INFO)
        # #----------------------------------------------------------

        #CREATE ENVIRONMENT DIRECTORY------------------------------
        # if(self.create_environment_directory):
        #     self.environment_path = "environment"
        #     self.constants_path = f"{self.environment_path}/constants.py"

        #     if not os.path.exists(self.environment_path):
        #         os.makedirs(self.environment_path)
        #----------------------------------------------------------

        #CREATE CONSTANTS.PY---------------------------------------
        # if(self.create_environment_directory):
        #     if(not os.path.exists(self.constants_path)):
        #         tls.f_write(_filename=self.constants_path, _content="#here lies the constants")
        #----------------------------------------------------------

        # if(self.driver_type==SETTINGS_USE_APPIUM):
        #     self.flutter_console = self.taskman.start_task("flutter_console.py")

        # self.resolve_imports() #imports necessary libraries depending on used driver type

        # self.api = API()
        
        # self.taskman = Taskman()
        
        self.by = self.driver.get_by()
        self.pa = pa
        self.cv = cv
        self.np = np

        self.row_index = 0
        self.confidence = 0.77

        self.start_time = time.perf_counter()
        self.end_time = None

        # self.scribe = Scribe(_report_path=self.report_path)
        # self.scribe.new_page("emploid report")
        self.request_delay = _request_delay
        
        self.internal_path = "elements/"
        self.browser_type = _browser_type
        self.window_width = 500
        self.window_height = 800
        self.incognito = _incognito
        self.headless = _headless
        self.vpn = _vpn
        self.autoconnect = _autoconnect
        self.vpn_index = 0
        self.exception = None

        self.appium_server = None
        self.emu = None

        #DATABASE VARIABLES----------------------------------------
        self.db_connection = None
        self.database_server = DATABASE_SERVER
        self.database_name = DATABASE_NAME
        self.database_username = DATABASE_USER_NAME
        self.database_password = DATABASE_USER_PASSWORD
        #----------------------------------------------------------

        # try:
        #     print("connecting to database...")
        #     self.db_connection = self.db_connect()

        #     if(self.db_connection):
        #         self.show("connected to database")
            
        # except Exception as e:
        #     self.show("could not connect to DB.")

        # self.average_scroll_distance = 50

        # if(self.screen_get_size()!=(1920, 1080)): #this is no longer needed because elements now can be detected regardless of resolution
        #     raise Exception("resolution is not supported. Screen Resolution must be (1920x1080).")

        # if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
        #     self.load_elements()
        # if(self.driver_type==SETTINGS_USE_APPIUM or self.driver_type==SETTINGS_USE_SELENIUM):
        #     self.load_identifiers()
        # self.taskman = Taskman()
        # self.beholder = self.taskman.start_task("record.py")
        
        self.show("started")
        
    @loggerd
    def init(self):
        pass
        
    @loggerd
    def set_driver_type(self, _driver_type):
        self.driver_type = _driver_type
        return self
    @loggerd
    def set_autoconnect(self):
        self.autoconnect = True
        return self
    @loggerd
    def set_headless(self):
        self.headless = True
        return self
    @loggerd
    def set_incognito(self):
        self.incognito = True
        return self
    @loggerd
    def set_vpn(self):
        self.vpn = True
        return self
    @loggerd
    def set_request_delay(self, _delay):
        self.request_delay = _delay
        return self
    @loggerd
    def set_user_profile(self, _user_profile):
        self.user_profile = _user_profile
        return self
    @loggerd
    def set_browser_type(self, _browser_type):
        self.browser_type = _browser_type
        return self
    @loggerd
    def set_maximized(self):
        self.maximized = True
        return self
    @loggerd
    def set_window_size(self, _window_size):
        self.window_size = _window_size
        return self
    @loggerd
    def set_report_path(self, _report_path):
        self.report_path = _report_path
        return self
    @loggerd
    def set_log_path(self, _log_path):
        self.log_path = _log_path
        return self
    @loggerd
    def set_log_to_db(self):
        self.log_to_db = True
        return self
    @loggerd
    def set_load_entities(self):
        self.load_entities = True
        return self

    @loggerd
    def load_entities_function(self):
        """This function is for loading entities froma file. Entities can be Xpaths or PIL images or anything in-between."""
        # try:
        #     self.load_elements if self.driver_type==SETTINGS_USE_PYAUTOGUI else None()
        # except Exception as e:
        #     print(e)
        return self

    @loggerd
    def __del__(self):
        # self.taskman.kill_task(self.beholder, _delay=2)
        # if(self.driver_type==SETTINGS_USE_APPIUM):
            # self.taskman.kill_task(self.flutter_console)

        self.end_time = time.perf_counter()
        time_ = round(self.end_time - self.start_time)

        # try:
        #     self.db_close(self.db_connection)
        # except Exception as e:
        #     print(e)

        self.show(f"test duration: {time_} seconds.")

    @loggerd
    def db_connect(self, _database_server=None, _database_name=None, _database_username=None, _database_password=None):
        # Define the connection parameters
        database_server = DATABASE_SERVER if _database_server is None else _database_server
        database_name = DATABASE_NAME if _database_name is None else _database_name
        database_username = DATABASE_USER_NAME if _database_username is None else _database_username
        database_password = DATABASE_USER_PASSWORD if _database_password is None else _database_password

        # Create the connection string
        if(DATABASE_ENGINE=="sqlserver"):
            conn_str = f"""
                DRIVER={{SQL Server}};
                SERVER={database_server};
                DATABASE={database_name};
                UID={database_username};
                PWD={database_password};
                Trusted_Connection=yes;
            """
            try:
                # Establish a connection to the database
                conn = pyodbc.connect(conn_str)
                self.db_connection = conn
                return conn

            except pyodbc.Error as e:
                # Handle any errors that occur during connection or execution
                print(f"Error: {e}")
                self.wait(3)
                
        else:
            raise Exception("selected DATABASE_ENGINE is not supported.")
        

    def query(self, _db_con=None, _query=""): #for some reason adding the logger decorater to this function freezes emploid from starting
        """executes a query on the database and returns the result"""
            
        result = []

        db_conn = self.db_connection if _db_con is None else _db_con

        # Create a cursor object to execute SQL queries
        cursor = db_conn.cursor().execute(_query)
        try:
            columns = [column[0] for column in cursor.description]
            for row in cursor.fetchall():
                result.append(dict(zip(columns, row)))
        except Exception as e:
            pass

        cursor.commit()
        cursor.close()
        return (result)

    
    @loggerd
    def quick_query(self, _database_server=None, _database_name=None, _database_username=None, _database_password=None, _query=None):
        """quickly connects to specified server, database and table, and executes a query"""
        conn = self.db_connect(_database_server, _database_name, _database_username, _database_password)
        result = self.query(conn, _query)
        self.db_close(conn)
        return result
    
    @loggerd
    def db_close(self, _db_con):
        """closes existing connection to database"""
        db_con = self.db_connection if _db_con is None else _db_con
        db_con.close()
        return db_con
    
    @loggerd
    def return_print(*_strings):
        print(_strings)
        return _strings

    @loggerd
    def set_log_path(self, _path):
        if not os.path.exists(_path):
            os.makedirs(_path)
        self.log_path = _path
        # logger.basicConfig(filename=self.log_path, encoding='utf-8', format='%(asctime)s %(message)s', level=logger.DEBUG)
        return self.log_path
    
    @loggerd
    def determine_browser(self):
        self.driver.determine_browser()
        return self.driver
    
    @loggerd
    def get(self, _url="", _tooltip="get link", _scribble=False):
        """loads a web page in the browser"""
        if(_url):
            self.driver.get(_url)
            if(_scribble):
                self.row_index += 1
            # self.scribe.insert_row(_row_number=self.row_index, _action_name=_tooltip, _expected_result=_tooltip, _actual_result=True, _result_state=True, _scribble=_scribble)
            return True
        else:
            raise Exception("please provide a URL.")

    # @loggerd
    # def resolve_imports(self):

    #     if(self.driver_type==SETTINGS_USE_APPIUM):
    #         from appium import webdriver as AppiumDriver
    #         from appium.webdriver.common.appiumby import AppiumBy as By
    #         from appium.options.android import UiAutomator2Options # Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
    #         from appium.options.common import AppiumOptions
    #         # from appium.webdriver.common.touch_action import TouchAction as AppiumAction <-- this is deprecated
    #         from appium.webdriver.extensions.android.nativekey import AndroidKey as ak
        
    #     if(self.driver_type==SETTINGS_USE_SELENIUM):
    #         from selenium import webdriver
    #         from selenium.webdriver.common.by import By
            # from selenium.webdriver.common.keys import Keys

    @loggerd
    def show(self, *_args) -> None:
        print("\n------------------------")
        for arg in _args:
            print("----", arg)
        print("\n------------------------")

    @loggerd
    def load_elements(self, _dir='elements') -> None:
        elm_dir = getcwd()+_dir
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            directories = list(os.walk(elm_dir))
            print("directories:\n", directories)
            with(open("load_elements.py", 'w', encoding='utf-8') as f):
                f.write("from module.emploid.emploid import Emploid\nfrom module.emploid.constants import *\nimport cv2 as cv\nfrom time import sleep\nemp = Emploid(_driver_type=SETTINGS_USE_PYAUTOGUI)\n")
                if(len(directories)):
                    for current_dir in directories:
                        try:
                            extension_index = -4
                            for png in current_dir[2]:
                                if(png[extension_index:].lower()==".png"):
                                    line = "element_"+png[:extension_index]+"=emp.import_image(\""+current_dir[0].replace("\\", "/")+"/"+png+"\", cv.IMREAD_GRAYSCALE)\n"
                                    line = line.replace(_dir, "")
                                    f.write(line)
                                    print("line:", line)
                                else:
                                    print("not a png")
                            else:
                                print(f"""failed to load [element_{png[:-4]}] from {current_dir[0]}""")
                        except Exception as e:
                            print("error:", e)
                    
            # content = tls.f_read("load_elements.py")
            # tls.f_write("load_elements.py", content)
        else:
            raise Exception("driver type not supported")
    
    @loggerd
    def load_identifiers(self): #for future use
        # import emploid.identifiers as id
        pass
        

    # @loggerd
    # def get_steps(self) -> list[str]:
    #     """SETTINGS_USE_PYAUTOGUI-specific function. It loads screenshots as steps from the internal path."""
    #     self.steps = listdir(self.internal_path)
    #     # for dir in self.steps:
    #     #     self.steps[0].append(dir)
    #     #     print("dir:"+self.steps[0][0])
    #     print(f"got ({len(self.steps)}) steps")
        
    @loggerd
    def image_compare(self, _img1, _img2) -> float:
        """compares two images and returns similarity percentage between them."""
        # load the input images
        img1 = _img1
        img2 = self.scale_to(_img2, img1)

        # convert the images to grayscale
        img1 = self.cv.cvtColor(img1, self.cv.COLOR_BGR2GRAY)
        img2 = self.cv.cvtColor(img2, self.cv.COLOR_BGR2GRAY)

        img_a_array = self.np.array(img1)
        img_b_array = self.np.array(img2)
        difference = (img_a_array == img_b_array).sum()
        pixel_num = img1.shape[0]*img1.shape[1]

        return difference/pixel_num
    
    @loggerd
    def convert_to_grayscale(self, _img):
        """converts ``_img`` to grayscale."""
        return self.cv.cvtColor(_img, self.cv.COLOR_BGR2GRAY)
    
    @loggerd
    def detect_template(self, _needle: cv.Mat, _haystack: cv.Mat, _method=cv.TM_CCOEFF_NORMED, _threshold = 0.5):
        template = _needle
        haystack = _haystack
        method= _method
        threshold = _threshold
        # Convert main image to grayscale if it's in color
        # if len(main_image.shape) > 2:
        #     main_image_gray = cv.cvtColor(main_image, cv.COLOR_BGR2GRAY)
        # else:
        #     main_image_gray = main_image

        # Perform template matching
        result = cv.matchTemplate(haystack, template, method)

        # Find the location of the best match
        _, max_val, _, max_loc = cv.minMaxLoc(result)

        print("accuracy:", max_val)

        # Check if the match is above the threshold
        if max_val >= threshold:
            # return max_loc, result, template
            return_template = True
        else:
            return_template = False

        if(return_template):
            template_location = max_loc
            result = result
            template = template
            if template_location is not None and result is not None and template is not None:
                print("Template found at (x, y):", template_location)

                # Draw a rectangle around the detected template
                h, w = template.shape[:2]
                top_left = template_location
                bottom_right = (top_left[0] + w, top_left[1] + h)
                return result
            else:
                raise Exception("Template not found or below accuracy threshold.")
    
    @loggerd
    def scale_to(self, _img1, _img2):
        #scales image 1 to image 2 size
        image3 = cv.resize(_img1, (_img2.shape[1], _img2.shape[0]), cv.INTER_LINEAR_EXACT)
        
        if(image3.shape == _img2.shape):
            return image3
        else:
            return False

    @loggerd
    def import_image(self, _dir, _method=cv.IMREAD_GRAYSCALE, _internal=True, _report=True):
        if(_internal):
            path = _dir
            elm = self.cv.imread(path, _method)
            if(elm is not None):
                if(_report):
                    # print(f"element ({_dir}) IMPROTED successfully")
                    self.element_count += 1
                return elm
            else:
                if(_report):
                    print(f"element ({_dir}) FAILED to import")
                    
        else:
            return Exception("non-internal paths are not currently suppoorted")

    @loggerd
    def import_images(self, _dir, _internal=True):
        elements = []
        if(_internal):
            _dir = self.internal_path+_dir
        else:
            pass
        # print("------------directory name:", _dir)
        for element in listdir(_dir):

            # print("------------files in directory:", len(listdir(_dir)))
            
            element_path = join(_dir, element)
            # print("------------element path:", element_path)
            if isfile(element_path):
                # print("------------element is a file:", element)
                element = self.import_image(element_path, _internal=False)
                # print("------------element:", element)
                elements.append(element)
            else:
                # print("------------element is not a file")
                pass

        return elements
    
    @loggerd
    def determine_entity(self, _ent):
        """determines whether passed ``_ent`` is a webelement, an xpath, a css selector, or a package name."""
        return self.driver.determine_entity(_ent)

    @loggerd
    def promise_element(self, _ent, _mode=None, _tries=3, _delay=1, _confidence=0.9, _tooltip=f"promising element..."):
        """
        this function "promises" to return an element if it is possible. Whether you pass it a screenshot, an xpath, or a package Id.\n
        it can try as many ``_tries`` as possible to find the element with a ``_delay`` between each attempt.
        """
        #This function needs modification, it doesn't raise an exception when the element is not found where it should. Will look into it later.
        is_element = self.driver.define_element(_ent)

        if(is_element):
            return _ent
        else:
            def func_(self):
                print("locating element...")
                elm = self.locate(_ent, _confidence=_confidence)
                if(elm):
                    print("detected")
                    return elm
                else:
                    print("could not detect element")
                    return False
            return self.promise(_func=func_, _tries=_tries, _delay=_delay, _tooltip=_tooltip)
    
    @loggerd
    def keyboard_paste(self, _str) -> None:
        """copies the specified ``_str`` into the clipboard and pastes it using ``CRTL + V``."""
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            clip.copy(_str)
            self.keyboard_hotkey("ctrl", "v")

    @loggerd
    def press(self, _btn: int =0) -> None:
        
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            btns = ['left', 'right', 'middle' ]
            self.pa.click(button=btn)
            btn = btns[_btn]
        elif(self.driver_type==SETTINGS_USE_APPIUM):
            # return AppiumAction.press(_btn).perform()
            raise Exception("not yet supported")
        elif(self.driver_type==SETTINGS_USE_SELENIUM):
            raise Exception("not yet supported")
    
    @loggerd
    def swipe_up(self, _distance=500):
        if(self.driver_type==SETTINGS_USE_APPIUM):
            # Define the start and end coordinates for the swipe action
            start_x = self.screen_get_width()/2  # starting x-coordinate (you may need to adjust this)
            start_y = self.screen_get_height()/2  # starting y-coordinate
            end_x = start_x  # ending x-coordinate (same as starting x-coordinate for vertical swipe)
            end_y = start_y + _distance  # ending y-coordinate (you may need to adjust this)

            # Perform the swipe action
            self.driver.swipe(start_x, start_y, end_x, end_y, duration=800)  # you can adjust the duration as needed
            return True
        return False

    @loggerd
    def swipe_down(self, _distance=500):
        # Define the start and end coordinates for the swipe action
        start_x = self.screen_get_width()/2  # starting x-coordinate (you may need to adjust this)
        start_y = self.screen_get_height()/2  # starting y-coordinate
        end_x = start_x  # ending x-coordinate (same as starting x-coordinate for vertical swipe)
        end_y = start_y - _distance  # ending y-coordinate (you may need to adjust this)

        # Perform the swipe action
        self.driver.swipe(start_x, start_y, end_x, end_y, duration=800)  # you can adjust the duration as needed

    @loggerd
    def check_installed(self, _package):
        if(self.driver_type==SETTINGS_USE_APPIUM):
            return self.driver.is_app_installed(_package)
        raise Exception("method not supported for this driver type")
        
    @loggerd
    def click(self, _elm, _tries=3, _delay=1, _confidence=0.8, _exit=False, _tooltip="", _scribble=False) -> bool:
        """clicks an element, promising to find it beforehand."""
        def func_(self):
            elm = _elm
            elm = self.promise_element(_elm, _confidence=_confidence, _tooltip=_tooltip)
            if(elm):
                if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
                    self.pa.click(elm)
                if(self.driver_type==SETTINGS_USE_APPIUM):
                    elm.click()
                if(self.driver_type==SETTINGS_USE_SELENIUM):
                    elm.click()
                return True, elm
            else:
                raise Exception("could not click element")
        status, elm = self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)
        if(_scribble):
            self.row_index += 1
        # self.scribe.insert_row(self.row_index, _action_name=_tooltip, _expected_result=_tooltip, _actual_result=status, _result_state=status, _scribble=_scribble)
        return status, elm
    
    @loggerd
    def detect_element(self, _elm, _tries=3, _delay=1, _confidence=0.8, _exit=False, _tooltip="", _scribble=False) -> bool:
        """clicks an element, promising to find it in the process."""
        def func_(self):
            elm = _elm
            elm = self.promise_element(_elm, _confidence=_confidence, _tooltip=_tooltip)
            if(elm):
                return True, elm
            else:
                raise Exception("could not click element")
        status, elm = self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)
        if(_scribble):
            self.row_index += 1
        # self.scribe.insert_row(self.row_index, _action_name=_tooltip, _expected_result=_tooltip, _actual_result=status, _result_state=status, _scribble=_scribble)
        return status, elm
    
    @loggerd
    def set_value(self, _elm=None, _value=None):
        """sets the value attribute of an html element using javascript"""
        return self.execute_javascript("arguments[0].value = arguments[1];", _elm, _value)

    @loggerd
    def lclick(self, _elm, _tooltip="Left Click", _tries=3, _delay=1, _exit=False)  -> bool:
        def func_(self):
            elm = _elm
            elm = self.promise_element(_elm, _tooltip=_tooltip)
            if(elm):
                self.pa.leftClick(elm)
                return True
            else:
                raise Exception("could not left click element")
        return self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)

    @loggerd
    def rclick(self, _elm, _tooltip="Right Click", _tries=3, _delay=1, _exit=False) -> bool:
        def func_(self):
            elm = _elm
            elm = self.promise_element(_elm, _tooltip=_tooltip)
            if(elm):
                self.pa.rightClick(elm)
                return True
            else:
                raise Exception("could not right click element")
        return self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)

    @loggerd
    def dbclick(self, _elm, _tooltip="Double Click", _tries=3, _delay=1, _exit=False) -> bool:
        def func_(self):
            elm = _elm
            elm = self.promise_element(_elm, _tooltip=_tooltip)
            if(elm):
                self.pa.doubleClick(elm)
                return True
            else:
                raise Exception("could not double click element")
        return self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)

    @loggerd
    def mdclick(self, _elm, _tooltip="Middle Click", _tries=3, _delay=1, _exit=False) -> bool:
        def func_(self):
            elm = _elm
            elm = self.promise_element(_elm, _tooltip=_tooltip)
            if(elm):
                self.pa.middleClick(elm)
                return True
            else:
                raise Exception("could not middle click element")
        return self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)

    @loggerd
    def get_func_name(self, _level=1) -> str:
        #level is the scope level of function to get the name of
        #_level 0 will return name of this function
        #_level 1 (default) will return name of function that called this function
        #etc
        
        # return inspect.stack()[1].code_context[0]
        return str(inspect.stack()[_level][3])

    @loggerd
    def input_into(self, _str, _elm=None, _confidence=0.77, _tries=3, _delay=1, _exit=False, _action_name="", _tooltip="", _click=True, _scribble=False) -> bool:
        """
        input text into element.
        """
        click = _click
        #if an element is passed, it clicks it before passing the text
        #THIS FUNCTION CURRENTLY WORKS WITH ELEMENTS ONLY. ELEMENTS MUST BE PASSED INTO IT.
        def func_(self):
            if(_elm is not None):
                if(click):
                    clicked, elm = self.click(_elm,  _tries=1, _confidence=_confidence)
                else:
                    self.detect_element(_elm,  _tries=1, _confidence=_confidence)
                if(clicked):
                    if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
                        if(self.contains_arabic_letters(_str)):
                            print(f"string ({_str}) contains arabic letters")
                            clip.copy(_str)
                            clip.paste() #this needs testing with appium
                            # self.keyboard_hotkey("ctrl", "v")
                        else:
                            self.pa.write(_str)
                    if(self.driver_type==SETTINGS_USE_APPIUM):
                        sleep(1)
                        elm.clear()
                        elm.send_keys(_str)
                    if(self.driver_type==SETTINGS_USE_SELENIUM):
                        sleep(1)
                        try:
                            elm.clear()
                        except:
                            pass
                        elm.send_keys(_str)

                    return True, elm
                else:
                    raise Exception("could not click elment")
            raise Exception("could not input into element")
        status, result = self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)
        if(_scribble):
            self.row_index += 1
        # self.scribe.insert_row(self.row_index, _action_name=_tooltip, _expected_result=_tooltip, _actual_result=status, _result_state=status, _scribble=_scribble)
            

        # print("status:", status)
        return status, result

    @loggerd
    def submit(self, _str, _elm, _tries=3, _delay=1, _tooltip="submit text to an input field", _scribble=False):
        """simulates inputing text into an input and then pressing enter."""
        check = self.input_into(_str=_str, _elm=_elm, _tries=_tries, _delay=_delay, _tooltip=_tooltip)
        self.enter()
        if(_scribble):
            self.row_index += 1
        # self.scribe.insert_row(self.row_index, _action_name=_tooltip, _fourth_column="asdasdasda", _expected_result=_tooltip, _actual_result=check, _result_state=check, _scribble=_scribble)
        return check

    @loggerd
    def tap(self, _x, _y):
        """taps a specific point on screen"""
        return self.driver.tap([(_x, _y)])
    
    @loggerd
    def keyboard_press(self, _key) -> None:
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            self.pa.press(_key)
        if(self.driver_type==SETTINGS_USE_SELENIUM):
            raise Exception("not supported right now")
        if(self.driver_type==SETTINGS_USE_APPIUM):
            self.driver.press_keycode(_key)
        
    @loggerd
    def enter(self, _elm=None):
        """simulates pressing the enter key"""
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            # self.pa.press(_key)
            pass
        if(self.driver_type==SETTINGS_USE_APPIUM):
            self.driver.press_keycode(ak.ENTER)
            pass
        if(self.driver_type==SETTINGS_USE_SELENIUM):
            ActionChains(self.driver).key_down(Keys.ENTER).perform()

    @loggerd
    def escape(self, _elm=None):
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            raise Exception("not supported yet.")
            # self.pa.press(_key)
            pass
        if(self.driver_type==SETTINGS_USE_APPIUM):
            raise Exception("not supported yet.")
            self.driver.press_keycode(ak.ENTER)
            pass
        if(self.driver_type==SETTINGS_USE_SELENIUM):
            ActionChains(self.driver).key_down(Keys.ESCAPE).perform()

    @loggerd
    def report_action(self, _row_number, _action_name, _expected_result, _actual_result, _result_state, _scribble: bool = False):
        #What even is this function for? What was I thinking when creating it? We'll never know.
        # self.scribe.insert_row(_row_number, _action_name, _expected_result, _actual_result, _result_state, _scribble=_scribble)
        pass

    @loggerd
    def display_elements(self):
        """displays a list of all elements found on the screen."""
        if(self.driver_type==SETTINGS_USE_APPIUM):
            allelms = self.locate_all()
            for elm in allelms:
                print(elm.get_attribute('class'), elm.text)

    @loggerd
    def keyboard_hold(self, _key) -> None:
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            self.pa.keyDown(_key)
        else:
            raise Exception("not supported for this driver type")

    @loggerd
    def keyboard_release(self, _key) -> None:
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            self.pa.keyUp(_key)
        else:
            raise Exception("not supported for this driver type")
    
    @loggerd
    def keyboard_hotkey(self, *_keys) -> None:
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            self.pa.hotkey(*_keys) 
        else:
            raise Exception("not supported for this driver type")

    @loggerd
    def find_element(self, _xpath, _method=SeleniumBy.XPATH):
        return self.driver.find_element(_method, _xpath)
    
    @loggerd
    def find_elements(self, _xpath, _method=SeleniumBy.XPATH):
        return self.driver.find_elements(_method, _xpath)
    
    @loggerd
    def locate(self, _elm, _confidence=0.9, _mode=None, _grayscale=True): 
        """locates an element through the provied identifier ``_elm``"""
        mode = _mode
        
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            if(mode==DETECTION_MODE_REGULAR):
                return self.pa.locateOnScreen(_elm, confidence=_confidence, grayscale=_grayscale)#, region=(0,0, 300, 400))
            elif(mode==DETECTION_MODE_TEMPLATE_MATCHING):
                #currently, in order for this function to work it MUST save a copy of the screenshot to storage and then load it again. Will look into this in the future and try to find a way to load it from memory that works
                raise Exception("not supported at the moment")
                _screen = self.pa.screenshot().save("elements/haystack.png")
                _screen = self.import_image("haystack.png")
                _elm = cv.imread("needle.png", cv.IMREAD_GRAYSCALE)
                _screen = cv.imread("haystack.png", cv.IMREAD_GRAYSCALE)
                _elm = self.multi_scale_template_matching(_screen, _elm, _confidence=_confidence)
                print("needle:", type(_elm))
                print("haystack:", type(_screen))
                tls.pause()
                _elm = self.detect_template(self, _elm, _screen)
                cv.imwrite("result.png", _elm)
                _elm = cv.imread("result.png")
        if(self.driver_type==SETTINGS_USE_APPIUM):
            if "com." in _elm.lower() and ":id" in _elm.lower(): _mode=SeleniumBy.ID
            if "//" in _elm.lower(): _mode=SeleniumBy.XPATH
            return self.find_element(_elm, _method=_mode)
        if(self.driver_type==SETTINGS_USE_SELENIUM):
            # print("element type:", _elm)
            if "/" in _elm.lower(): _mode=SeleniumBy.XPATH
            return self.find_element(_elm, _method=_mode)

    @loggerd
    def locate_in_region(self, _elm, _x, _y, _xx, _yy, _confidence=0.9, _mode=DETECTION_MODE_REGULAR, _grayscale=True): 
        mode = _mode
        if(mode==DETECTION_MODE_REGULAR):
            return self.pa.locateOnScreen(_elm, confidence=_confidence, grayscale=_grayscale, region=[_x, _y, _xx, _yy])
        elif(mode==DETECTION_MODE_TEMPLATE_MATCHING):
            #currently, in order for this function to work it MUST save a copy of the screenshot to storage and then load it again. Will look into this in the future and try to find a way to load it from memory that works
            raise Exception("not supported at the moment")
            _screen = self.pa.screenshot().save("elements/haystack.png")
            _screen = self.import_image("haystack.png")
            _elm = self.multi_scale_template_matching(_screen, _elm)
            # Display the result
            cv.imshow('Multi-Scale Template Matching Result', _screen)
            cv.waitKey(0)
            cv.destroyAllWindows()
            
    @loggerd
    def locate_all(self, _confidence=0.9, _mode=DETECTION_MODE_REGULAR, _grayscale=True):
        """Locates all elements on the current view."""
        mode = _mode
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            if(mode==DETECTION_MODE_REGULAR):
                return list(self.pa.locateAllOnScreen(_elm, confidence=_confidence, grayscale=_grayscale))
            elif(mode==DETECTION_MODE_TEMPLATE_MATCHING):
                raise Exception("not supported at the moment")
                #currently, in order for this function to work it MUST save a copy of the screenshot to storage and then load it again. Will look into this in the future and try to find a way to load it from memory that works
                _screen = self.pa.screenshot().save("elements/haystack.png")
                _screen = self.import_image("haystack.png")
                _elm = self.multi_scale_template_matching(_screen, _elm)
        if(self.driver_type==SETTINGS_USE_APPIUM):
            return self.find_elements("//*")

    @loggerd
    def contains_arabic_letters(self, input_string):
        #written by chat-gpt
        import re
        # Define a regular expression pattern for Arabic letters
        arabic_letters_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+')

        # Check if the input string contains Arabic letters
        return bool(arabic_letters_pattern.search(input_string))
        
    @loggerd
    def prompt(self, _str) -> None:
        return self.pa.prompt(_str)
    
    def spaghette(self):
        return "Toucha the spaghette"

    @loggerd
    def confirm(self, _str):
        value = self.pa.confirm(_str)
        if(value.lower()=="cancel"):
            return False
        if(value.lower()=="ok"):
            return True

    @loggerd
    def alert(self, _str=""):
        return self.pa.alert(_str, 'EMPLOID ALERT')
        
    @loggerd
    def moveto(self, _elm, _tooltip="Move Mouse to Element", _tries=3, _delay=1, _exit=False) -> bool:
        def func_(self):
            if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
                elm = _elm
                elm = self.promise_element(_elm, _tooltip=_tooltip)
                if(elm):
                    self.pa.moveTo(elm, duration = 0.1)
                    return True
                else:
                    raise Exception("could not move mouse to element")
            else:
                raise Exception("not supported for this driver type")
        return self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)

    @loggerd
    def mouse_scroll(self, _value: float, _x: float=None, _y: float=None) -> None:
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            self.pa.scroll(_value, x=_x, y=_y) #positive up, negative down

    @loggerd
    def mouse_scroll_up(self, _value: float=250, _x: float=None, _y: float=None) -> None:
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            value = abs(_value)
            self.mouse_scroll(value, _x, _y)

    @loggerd
    def mouse_scroll_down(self, _value: float=-250, _x: float=None, _y: float=None) -> None:
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            value = -abs(_value)
            self.mouse_scroll(value, _x, _y)

    @loggerd
    def get_pixel(self, _elm=None, _px=0, _py=0):
        """gets the color of a pixel at a specific point"""
        #To obtain the RGB color of a pixel in a screenshot, use the Image object’s getpixel() method:
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            if(_elm):
                return _elm.getpixel((_px, _py))
            else:
                return self.pa.pixel((_px, _py))

    @loggerd
    def get_screenshot(self, _screen_name : str):
        """captures a screenshot of the screen"""
        return self.pa.screenshot(_screen_name)

    @loggerd
    def get_mouse_pos(self):
        """gets the mouse position on screen"""
        return self.pa.position()

    @loggerd
    def set_delay(self, _value: float) -> None:
        """sets a delay between actions for template-matching driver."""
        self.pa.PAUSE = _value

    @loggerd
    def set_failsafe(self, _value: bool) -> None:
        self.pa.FAILSAFE = _value

    @loggerd
    def mouse_move_relative(self, _xoffset=0, _yoffset=0, _seconds=0) -> None:
        self.pa.moveRel(_xoffset, _yoffset, duration=_seconds)

    @loggerd
    def mouse_move(self, _x, _y, _seconds=0) -> None:
        self.pa.moveTo(_x, _y, duration=_seconds)

    @loggerd
    def mouse_drag_to(self, _x, _y, _seconds) -> None:
        self.pa.dragTo(_x, _y, duration=_seconds)  # drag mouse to XY

    @loggerd
    def mouse_drag_to_relative(self, _xoffset, _yoffset, _seconds) -> None:
        self.pa.dragTo(_xoffset, _yoffset, duration=_seconds) 

    @loggerd
    def program_run(self, _path):
        from pywinauto import Desktop, Application
        prog_path = _path
        program_name = prog_path.split("/")[-1]
        program_name = program_name.split("\\")[-1]
        prog = Application().start(prog_path)
        return prog#Application(backend='uia').connect(path=program_name, title_re='New Tab')
    
    @loggerd
    def chrome_run(self, _url: str="", _incognito=False, _maximized=True) -> None:
        #this function is not used
        if(_incognito):
            _incognito = "-incognito"
        else:
            _incognito = ""
        if(_maximized):
            _maximized = "--start-maximized"
        else:
            _maximized = ""
        if(self.driver_type==SETTINGS_USE_SELENIUM):
            from selenium import webdriver
            from selenium.webdriver.chrome.service import Service
            from selenium.webdriver.chrome.options import Options as chromeOptions
            chromeoptions = chromeOptions()
            chromeoptions.add_argument("--start-maximized")
            chromeoptions.add_argument("--incognito")
            self.driver = webdriver.Chrome(options=chromeoptions, service=Service(executable_path="drivers/chromedriver.exe"))
            # self.driver.maximize_window()
            self.driver.get(_url)
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            from pywinauto import Desktop, Application
            chrome_dir = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            page_url = _url
            chrome = Application().start(chrome_dir + f' --force-renderer-accessibility {_incognito} {_maximized} ' + _url)
            app_new_tab = Application(backend='uia').connect(path='chrome.exe', title_re='New Tab')
            return True

    @loggerd
    def get_otp(self, _sn=797693694):
        
        result = requests.get(f"{TESTAPI_GET_OTP}?sn={_sn}")
        return result.json()

    @loggerd
    # def email_generate(self):
        
    #     self.show("getting email...")
    #     while True:
    #         try:
    #             from pymailtm import MailTm, Account, Message
    #             return MailTm().get_account()
    #         except:
    #             pass

    # @loggerd
    # def email_listen(self, _email) -> str:
    #     try:
    #         mails = []
    #         while (not len(mails)): #this needs modification
    #             mails = _email.get_messages()
    #             sleep(2)
    #         return mails
    #     except Exception as e:
    #         print(e)
    #         pass

    # @loggerd
    # def email_find_code(self, n, s) -> str:
    #     import re
    #     result = re.search('\\d{%s}'%n, s)
    #     return result.group(0) if result else result

    # @loggerd
    # def send_get(self, _url, _params=None, _json=True):
    #     return self.testman.get(_url, _params=_params, _json=_json)
    
    # @loggerd
    # def send_post(self, _url, _params, _json=True):
    #     return self.testman.post(_url=_url, _params=_params, _json=_json)
    
    @loggerd
    def clipboard_copy(self):
        import win32clipboard
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return data
    
    @loggerd
    def detect(self, _elm, _tooltip="detect element"):
        def func_(self, _confidence=0.9):
            print("locating element")
            elm = self.promise_element(_elm, _tooltip=_tooltip)
            if(elm):
                print("detected")
                return elm
            else:
                print("could not detect element")
                return False
        return self.promise(_func=func_, _tooltip=f"attempt to locate element...")

    @loggerd
    def promise(self, _func, *_args, _tooltip="", _tries=3, _delay=1, _fullerror=False, _noerror=False, _noprint=False, _exit=False, _scribble=False):
        if(_tooltip==""):
            _tooltip = self.get_func_name(_level=2)
        print(f"----------------promise ({_tooltip})----------------")
        if(not _tries==None):
            if(_tries < 1):
                _tries = None
        state = True
        trigger = False
        while ((trigger==False) and (_tries==None or _tries>0)):
            if(_tries is not None):
                _tries -= 1
            try:
                result = _func(self, *_args)
                #insert Scribe row
                # if(result):
                #     col = "btn-success"
                # else:
                #     col = "btn-danger"
                # self.scribe.insert_row(0, _tooltip, "True", result, col, _scribble=_scribble)

                trigger = True
                state = True
                return result
            except Exception as e:
                if(_fullerror):
                    _str = "\nwith Exception:\n" + str(e)
                    pass
                else:
                    _str = ""
                if(not _noprint):
                    if(_noerror):
                        print(_tooltip)
                    else:
                        print(_tooltip + " FAILED ("+str(_tries)+f". . .) {_str}")
                sleep(_delay)
                state = False
        if(_exit):
            exit()
        else:
            # self.scribe.insert_row(0, _tooltip, "True", state, "btn-danger")
            pass
        return state
    
    @loggerd
    def screen_get_size(self):
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            return self.pa.size()
        if(self.driver_type==SETTINGS_USE_APPIUM):
            # Get screen size
            return self.driver.get_window_size()

    @loggerd
    def screen_get_width(self):
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            return self.pa.size()[0]
        if(self.driver_type==SETTINGS_USE_APPIUM):
            # Get screen size
            screen_size = self.driver.get_window_size()

            # Extract width and height from the screen size
            return screen_size['width']

    @loggerd
    def screen_get_height(self):
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            return self.pa.size()[1]
        if(self.driver_type==SETTINGS_USE_APPIUM):
            # Get screen size
            screen_size = self.driver.get_window_size()

            # Extract width and height from the screen size
            return screen_size['height']
        
    @loggerd
    def point_in_screen(self, _x, _y):
        return self.pa.onScreen(_x, _y)

    # @loggerd
    # def random_string(self, _length):
    #     pass

    # @loggerd
    # def appium_server_start(self):
    #     """Starts Appium Server\n"""
    #     print("starting appium server...")
    #     info = sp.STARTUPINFO()
    #     info.dwFlags = sp.STARTF_USESHOWWINDOW
    #     info.wShowWindow = 1
    #     self.appium_server = sp.Popen([sys.executable, APPIUM_SERVER_EXE], shell=True, startupinfo=info, creationflags=sp.CREATE_NEW_CONSOLE)
    #     return self.appium_server
    
    # @loggerd
    # def appium_emulator_start(self):
    #     """
    #     Starts the android emulator at the path: APPIUM_COMMAND_EMULATOR_START.\n
    #     You should probably start your emulator individually.
    #     """
    #     print("starting emulator...")
    #     self.emu = sp.Popen(APPIUM_COMMAND_EMULATOR_START, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    #     return self.emu
    
    @loggerd
    def appium_connect(self, _adb_connect=False):
        """Connects to appium server, and subsequently, the emulator."""
        try:
            with open("config/emu_config.json", 'r') as emu_config:
                capabilities = json.load(emu_config)
        except:
            capabilities = json.loads('{"platformName": "Android", "automationName": "uiautomator2"}')
        while True:
            try:
                print("connecting to appium server...")
                if(_adb_connect):
                    #when connecting to the likes of bluestacks, the command adb connect needs to be run first
                    pass
                self.driver = AppiumDriver.Remote(APPIUM_SERVER_URL, options=AppiumOptions().load_capabilities(capabilities))
                break
            except:
                pass

    # @loggerd
    # def appium_server_stop(self):
    #     """this currently does not work for some reason"""
    #     if(self.appium_server):
    #         self.appium_server.kill()
    #         os.system(f"taskkill /F /IM node.exe")

    @loggerd
    def appium_emulator_stop(self):
        if(self.emu):
            self.emu.kill()

    # @loggerd
    # def move_to(self, _element):
    #     return AppiumAction.move_to(_element).perform()
    
    # @loggerd
    # def mouse_release(self):
    #     AppiumAction.release().perform()
        
    @loggerd
    def activate_app(self, _app):
        """activates an app that is installed on the emulator device."""
        return self.driver.activate_app(_app)
    
    @loggerd
    def close_app(self, _app):
        """closes an app that is installed on the emulator device."""
        return self.driver.terminate_app(_app)

    @loggerd
    def generate_random_string(_length=10, _letters=True, _numbers=True, _other=True):
        from random import choice
        import string
        """generates a random string of a specified length"""
        # Define the characters that can be used in the random string
        characters = None
        characters = characters + string.ascii_letters
        characters = characters + string.digits
        # Generate the random string
        random_string = ''.join(choice(characters) for i in range(_length))
        return random_string

    @loggerd
    def multi_scale_template_matching(self, main_image, template, _confidence=0.77): #WRITTEN BY CHAT-GPT

        # Convert images to grayscale
        main_gray = cv.cvtColor(main_image, cv.COLOR_BGR2GRAY)
        template_gray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

        # Initialize a list to store the results at different scales
        results = []

        # Define a range of scales to consider
        scales = np.linspace(0.2, 1.0, 10)[::-1]

        for scale in scales:
            # Resize the template
            resized_template = cv.resize(template_gray, (0, 0), fx=scale, fy=scale)

            # Use template matching
            result = cv.matchTemplate(main_gray, resized_template, cv.TM_CCOEFF_NORMED)

            # Find the location of the best match
            _, _, _, max_loc = cv.minMaxLoc(result)

            # Store the results along with the scale
            results.append((scale, max_loc, result[max_loc[1], max_loc[0]]))

        # Select the result with the highest correlation score
        best_result = max(results, key=lambda x: x[2])

        # Extract the relevant information
        best_scale, best_loc, _ = best_result

        # Calculate the size of the template in the original image
        h, w = template_gray.shape
        best_size = (int(w * best_scale), int(h * best_scale))

        # Draw a rectangle around the matched area
        # cv.rectangle(main_image, best_loc, (best_loc[0] + best_size[0], best_loc[1] + best_size[1]), (0, 255, 0), 2)

        threshold_percentage = 0.3799999999999999
        
        # Get the correlation coefficient (similarity measure)
        correlation_coefficient = result[max_loc[1], max_loc[0]]

        # Extract the subimage
        subimage = main_image[best_loc[1]:best_loc[1] + best_size[1], best_loc[0]:best_loc[0] + best_size[0]]
        self.cv.imwrite("subimage.png", subimage)
        subimage = self.cv.imread("subimage.png")

        # Check if the correlation coefficient is above the threshold
        if correlation_coefficient <= threshold_percentage:
            print(f"Template found with similarity: {correlation_coefficient}")
            return subimage
        else:
            raise Exception(f"threshold ({correlation_coefficient}) is higher than {threshold_percentage}")

        # Draw a rectangle around the matched area
        # cv.rectangle(main_image, best_loc, (best_loc[0] + best_size[0], best_loc[1] + best_size[1]), (0, 255, 0), 2)

        threshold_percentage = _confidence
    
        # Get the correlation coefficient (similarity measure)
        correlation_coefficient = result[max_loc[1], max_loc[0]]

        # Check if the correlation coefficient is above the threshold
        if correlation_coefficient >= threshold_percentage:
            print(f"Template found with similarity: {correlation_coefficient}")
            return subimage
        else:
            raise Exception(f"threshold ({correlation_coefficient}) is lower than {threshold_percentage}")
        
    @loggerd
    def get_methods(self):
        methods = [method for method in dir(Emploid) if callable(getattr(Emploid, method))]
        methods = [method for method in methods if not method.startswith("__")]
        return methods
    
    @loggerd
    def print_methods(self):
        methods = self.get_methods()
        for method in methods: print(methods.index(method), method)

    @loggerd
    def test_chance(self, _probability): #tests the chance of execution for actions

        _probability = int(_probability)
        if(_probability>100):
            _probability = 100
        i = randint(0, 100)
        if(i<=_probability):
            return True
        return False

    @loggerd
    def add_action(self, _action=None, _value=None, _target=None, _chance=100, _priority=0): #adds an action to the LOCAL ACTIONS list (self.actions). This is used on imported actions from actions.json and not on CLOUD ACTIONS (which are passed to run_action() directly and are executed immediately)
        #imported from my FBBM module for facebook automation
        raise Exception("not supported yet.")
        self.actions.append({"action":_action, "value":_value, "target":_target, "chance":_chance, "priority":_priority})

        self.show(f"action {_action} ({_value}) added to {self.email}.")
        
    @loggerd
    def import_local_actions(self):

        #imported from my FBBM module for facebook automation
        raise Exception("not supported yet.")
        if(isfile("actions.json")):

            actions_dict = json.load(open("actions.json", encoding="utf8"))
            
            for key in actions_dict.keys():

                action = actions_dict[key]["action"]
                value = actions_dict[key]["value"]
                target = actions_dict[key]["target"]
                chance = actions_dict[key]["chance"]
                priority = actions_dict[key]["priority"]
                print("action:", action, "\nvalue:", value, "\ntarget:", target, "\nchance:", chance, "\npriority:", priority)
                
                self.add_action(action, value, target, int(chance), priority)
        show(f"{len(self.actions)} Local actions imported")
        

    @loggerd
    def generate_vip_actions(self): #generates actions for profiles, pages and groups in VIP list

        #imported from my FBBM module for facebook automation
        raise Exception("not supported yet.")
        from fbb_data.vip_upg import vip_profiles, vip_pages, vip_groups, vip_support, vip_targets

        # for profile in vip_profiles:

        #     self.add_action(_action=CONST.ACT_REACT_TO_COMMENT, _value="", _target=profile, _chance=80, _priority=0)
        #     self.add_action(_action=CONST.ACT_COMMENT_ON_POST, _value="(y)", _target=profile, _chance=80, _priority=0)
        #     self.add_action(_action=CONST.ACT_REACT_TO_POST, _value=CONST.REACT_LIKE, _target=profile, _chance=80, _priority=0)
        #     self.add_action(_action=CONST.ACT_SEND_FRIEND_REQUEST, _value="", _target=profile, _chance=80, _priority=0)
        #     self.add_action(_action="send_message", _value="(y)", _target=profile, _chance=100, _priority=0)

        for page in vip_pages:
            
            # self.add_action(_action=CONST.ACT_REACT_TO_COMMENT, _value="", _target=page, _chance=80, _priority=0)
            # self.add_action(_action=CONST.ACT_COMMENT_ON_POST, _value="(y)", _target=page, _chance=80, _priority=0)
            self.add_action(_action=CONST.ACT_REACT_TO_POST, _value=CONST.REACT_LIKE, _target=page, _chance=100, _priority=0)
            self.add_action(_action=CONST.ACT_SHARE_TO_RANDOM_GROUP, _value=page, _target="", _chance=80, _priority=0)
            # self.add_action(_action=CONST.ACT_ADD_SUGGESTED_FRIEND, _value="", _target="", _chance=65, _priority=0)
            self.add_action(_action=CONST.ACT_POST_QUOTE_IN_RANDOM_GROUP, _value="", _target="", _chance=80, _priority=0)

        # for page in vip_support:
            
        #     # self.add_action(_action=CONST.ACT_REACT_TO_COMMENT, _value="", _target=page, _chance=80, _priority=0)
        #     self.add_action(_action=CONST.ACT_COMMENT_ON_POST, _value=CONST.ACT_REQUEST_SUPPORT_COMMENT, _target=page, _chance=80, _priority=0)
        #     self.add_action(_action=CONST.ACT_REACT_TO_POST, _value=CONST.REACT_LIKE, _target=page, _chance=100, _priority=0)
        #     # self.add_action(_action=CONST.ACT_POST_TO_RANDOM_GROUP, _value=page, _target="", _chance=80, _priority=0)
        #     # self.add_action(_action=CONST.ACT_ADD_SUGGESTED_FRIEND, _value="", _target="", _chance=80, _priority=0)
        #     self.add_action(_action=CONST.ACT_POST_QUOTE_IN_RANDOM_GROUP, _value="", _target="", _chance=80, _priority=0)

        # for page in vip_targets:
            
        #     self.add_action(_action=CONST.ACT_REACT_TO_POST, _value=CONST.REACT_HAHA, _target=page, _chance=100, _priority=0)
        #     self.add_action(_action=CONST.ACT_COMMENT_ON_POST, _value=CONST.ACT_REQUEST_PNEGATIVE_COMMENT, _target=page, _chance=80, _priority=0)
        #     self.add_action(_action=CONST.ACT_POST_TO_RANDOM_GROUP, _value=page, _target="", _chance=80, _priority=0)
        #     # self.add_action(_action=CONST.ACT_ADD_SUGGESTED_FRIEND, _value="", _target="", _chance=80, _priority=0)
        #     self.add_action(_action=CONST.ACT_POST_QUOTE_IN_RANDOM_GROUP, _value="", _target="", _chance=80, _priority=0)

        show(f"{len(self.actions)} vip actions generated")

    @loggerd
    def get_cloud_actions(self):
        #imported from my FBBM module for facebook automation
        raise Exception("not supported yet.")
        #Send profile ID to Server to get profile's actions
        print("\nprofile id:", self.id)
        global prioritized_actions
        
        try:
            prioritized_actions = requests.get(f"https://libyasoftware.com/lypybot/api.php/action/getProfileActions?profile_id={self.id}").json() 
            sleep(self.request_delay)
        except Exception as e:
            print(e)
            prioritized_actions = None
            pass

    @loggerd
    def load_extension(self, _extension):
        """adds an extension from a file to the running chrome profile."""
        #imported from my FBBM module for facebook automation
        self.chrome_options.add_extension(_extension)

        # extension_id = "majdfhpaihoncoakbjgbdhglocklcgno"
        # page = "html/pages/welcome.html"
        # url = f"chrome-extension://{extension_id}/{page}.html"
        # url = "chrome-extension://majdfhpaihoncoakbjgbdhglocklcgno/html/foreground.html"
        
        # def func_(self):
        #     self.get()
        # self.promise(_func=func_, _tooltip="getting link", _tries=100, _delay=3)

    @loggerd
    def activate_vpn(self):
        #imported from my FBBM module for facebook automation
        # raise Exception("not supported yet.")
        # self.vpn_index = 2

        self.pressed_activate = False

        if(self.vpn_loaded):

            # self.vpn_tab = self.new_tab("https://mbasic.facebook.com")
            # self.select_tab(self.vpn_tab)

            self.vpn_tab = self.new_tab("")
            
            if(self.browser_type==BROWSER_TYPE_FIREFOX):
                
                def func_(self):

                    #in firefox, we need to get the extension id first since it changes with every installation
                    # show("get the extension id")
                    # self.get("about:support")
                    # self.select_tab(self.vpn_tab)

                    # table = self.driver.find_element(By.XPATH, "//*[@id='addons-tbody']")
                    # highlight(self, table)

                    # rows = table.find_elements(By.TAG_NAME, "tr")

                    # print("rows:", len(rows))

                    # extension_id = ""

                    # for row in rows:
                    #     columns = row.find_elements(By.TAG_NAME, "td")

                    #     for col in columns:
                    #         index = columns.index(col)
                            
                    #         highlight(self, col, "yellow")

                    #         if(index==0):
                    #             title = col
                    #             if(title.text=="Free VPN Proxy"):
                    #                 pass
                    #             else:
                    #                 break

                    #         if(index==4):

                    #             extension_id = col.text
                    #             extension_id = extension_id.replace("{", "")
                    #             extension_id = extension_id.replace("}", "")

                    # self.driver.vpn_url = f"moz-extension://{extension_id}/html/foreground.html"

                    # self.driver.firefox_profile._addon_details("sadsad")
                    
                    def func_(self):
                        # print("extension id:", extension_id)
                        self.select_tab(self.vpn_tab)
                        self.driver.get(self.driver.vpn_url)
                        # pause()
                    self.promise(_func=func_, _tooltip=f"getting link ({self.driver.vpn_url})", _tries=100, _delay=3)
                    
                    if(
                        "blocked" in self.driver.page_source.lower()
                        or "Thank You For Installing VeePN".lower() in self.driver.page_source.lower()
                        ):
                        raise Exception ("Extension has been blocked by Chrome")
                self.promise(_func=func_, _tooltip="getting extension id", _tries=100, _delay=3)

            if(self.browser_type==BROWSER_TYPE_CHROME):
                def func_(self):
                    self.driver.vpn_url = None
                    
                    if(self.vpn_index==0):
                        self.driver.vpn_url = "chrome-extension://majdfhpaihoncoakbjgbdhglocklcgno/html/foreground.html"

                    if(self.vpn_index==1):
                        self.driver.vpn_url = "chrome-extension://jifpbeccnghkjeaalbbjmodiffmgedin/popup/index.html"
                        
                    self.select_tab(self.vpn_tab)

                    if(self.driver.vpn_url):
                        self.driver.get(self.driver.vpn_url)

                        if(True):
                            if(
                                "blocked" in self.driver.page_source.lower()
                                or "Thank You For Installing VeePN".lower() in self.driver.page_source.lower()
                                ):
                                raise Exception ("Extension has been blocked by Chrome")
                self.promise(_func=func_, _tooltip="getting link", _tries=100, _delay=3)
            
            if(self.vpn_index==0):
                def func_(self):
                    self.get(self.driver.vpn_url)
                    btn = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div[1]/div/div/span")
                    btn.click()
                self.promise(_func=func_, _tooltip="click activate", _delay=0)

            if(self.vpn_index==1):
                def func_(self):
                    self.get(self.driver.vpn_url)
                    btn = self.driver.find_element(By.CLASS_NAME, "agreement_agree")
                    btn.click()
                self.promise(_func=func_, _tooltip="click yes", _delay=0)

            def func_(self):
                try:
                    if(self.vpn):
                        # vpn_tab = self.activate_vpn()
                        if(self.vpn_tab != None):
                            self.pressed_activate = True
                            self.select_tab(self.vpn_tab)
                            sleep(2)
                            vpn_tab_title = self.driver.title
                            # print("vpn_tab:", vpn_tab_title)

                    # print("vpn_tab:", vpn_tab)

                    if(self.pressed_activate):
                        for tab in self.driver.window_handles:
                            self.select_tab(tab)
                            tab_title = self.driver.title
                            try:
                                if(tab!=self.vpn_tab):
                                    print(f"{tab_title}!={vpn_tab_title}")
                                    self.close_tab(tab)
                            except:
                                pass
                except Exception as e:
                    print(e)
            self.promise(_func=func_, _tooltip="c0000", _delay=0)

            while True:

                if(self.pressed_activate):

                    print("in self.promise")
                    self.catch_extension_error()
                    self.select_tab(self.vpn_tab)

                    sleep(1)

                    if(self.vpn_index==0):
                        try:
                            continue_btn = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[3]/div/div/button")
                            # continue_btn = driver.find_element(By.XPATH, "//button[contains(@text='Continue')]")
                            # highlight(driver, continue_btn)
                            continue_btn.click()

                            sleep(1)

                            start_btn = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[3]/div/div/button")
                            # start_btn = driver.find_element(By.XPATH, "//button[contains(@text='Start')]")
                            # highlight(driver, start_btn)
                            start_btn.click()
                            
                        except Exception as e:
                            # print(e)
                            # input()
                            pass
                    
                        try:
                            if "VPN is ON".lower() in self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div[1]/div/div/div").text.lower():
                                print("VPN ACTIVATED")
                                break
                            if "VPN is OFF".lower() in self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div[1]/div/div/div").text.lower():
                                print("VPN OFF")

                                def func_(self):
                                    btn = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div[1]/div/div/span")
                                    btn.click()
                                self.promise(_func=func_, _tooltip="click activate", _delay=0)

                                if(self.vpn_tab):
                                    for tab in self.driver.window_handles:
                                        self.act.select_tab(tab)
                                    
                                    if(tab!=self.vpn_tab):
                                        self.act.close_tab(tab)
                                        break
                                else:
                                    print("vpn_tab is None")
                                    input()

                                break
                        except:
                            print("error999")
                    else:
                        break
                else:
                    break

            def func_(self):
                btn = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[5]/div[1]/div")
                btn.click()
            self.promise(_func=func_, _tooltip="skip - back arrow", _delay=0)

            return self.vpn_tab
        else:
            print("VPN has not been loaded.")

    @loggerd
    def get_generated_image(self, _img_name="img.png"):
        #imported from my FBBM module for facebook automation
        self.show("get generated image from https://www.generatormix.com/random-image-generator")

        link = "https://picsum.photos/200"

        add_and = False

        if(self.test_chance(40)):
            link += "?grayscale&"
            add_and = True
        
        if(self.test_chance(30)):

            strength = 0.5

            if(add_and):
                link += f"&blur={strength}"
            else:
                link += f"?blur={strength}"

        if(self.grab_file(link, _img_name)):
            self.show("Image saved!")
        else:
            self.show("Error saving Image.")

        return _img_name

    @loggerd
    def get_generated_face(self):
        #imported from my FBBM module for facebook automation
        self.get("https://this-person-does-not-exist.com/en")
        
        img_name = "genface.png"

        def func_(self, img_name):
            emploid = self.driver.find_element(SeleniumBy.XPATH, "//img[@id='avatar']").get_attribute("emploid")
            
            if(self.grab_file(emploid, img_name)):
                self.show("img saved!")
            
            else:
                self.show("img did not save")

            return img_name
            

        self.promise(_func=func_, _args=img_name, _tooltip="get category", _delay=1, _tries=10)

    @loggerd
    def grab_file(self, _link="NONE", _name="NONE"): #grab file from link (currently used to grab pictures)
        #imported from my FBBM module for facebook automation
        print("file link:", _link)

        link = _link
        name = _name
        args = [link, name]

        def func_(self, _link, _name):
            try:
                r = requests.get(_link, allow_redirects=True)
                # sleep(self.request_delay)
            except Exception as e:
                print(e)
                r = None
                pass

            with open(_name, 'wb') as f:
                f.write(r.content)

        return self.promise(_func=func_, _args=args, _tooltip="grab file from link")

    @loggerd
    def test_ip(self): 
        """get the PUBLIC IP of the device through an online service or JSON request"""
        return tls.f_read(self.grab_file('http://lumtest.com/myip.json', "myip.json"))

    @loggerd
    def execute_javascript(self, _script, *_params):
        if(self.driver_type==SETTINGS_USE_SELENIUM):
            return self.driver.execute_script(_script, *_params)
        raise Exception("not supported for this driver type.")
    
    @loggerd
    def highlight(self, _elm, _color="red"): #imported from my FBBM module for facebook automation
        """highlights a web ``_elm`` with acceptable CSS ``_col``."""

        if(self.driver_type==SETTINGS_USE_SELENIUM):
            return self.driver.execute_script("""
                arguments[0].style.background = arguments[1];
                return true;
            """, _elm, _color)
        
    @loggerd
    def new_tab(self, link="google.com", select=False):
        """opens up a new browser tab."""
        window = self.driver.execute_script("""window.open(arguments[0],"_blank");""", link)

        tab_name = self.driver.window_handles[len(self.driver.window_handles) -1]

        if select:
            self.select_tab(tab_name)

        return tab_name

    @loggerd
    def close_tab(self, _tab):
        """closes a tab.\ndo NOT use on a window with a single tab otherwise the browser will close entirely and you'll receive an error."""
        self.driver.execute_script("window.close(arguments[0]);", _tab)

    @loggerd
    def select_tab(self, _tab):
        """selects an open tab so that further actions are done on the web page open in that tab."""
        for tab in self.driver.window_handles:
            if tab==_tab:
                self.driver.switch_to.window(_tab)

    @loggerd
    def catch_extension_error(self):
        """used inside of ``activate_vpn``"""
        def func_(self):
            if(self.exception is None):
                text = self.driver.page_source.lower()
                if "blocked by chrome" in text:
                    print("EXCEPTION:", "extension blocked by chrome")
                    self.user.kill()
        self.promise(_func=func_, _tooltip="check if extension blocked by chrome", _tries=10, _delay=0, _noprint=True)

    @loggerd
    def pause(self):
        """pauses the program until a key is pressed in the CMD."""
        self.show("emploid is paused. press any key to continue.")
        input()

    @loggerd
    def wait(self, _seconds):
        """waits for a number of seconds while displaying a timer in the CMD"""
        for i in range(0, _seconds):
            print(f"waiting ({_seconds - i}) seconds...")
            sleep(1)
            
    @loggerd
    def refresh(self):
        if(self.driver_Type==SETTINGS_USE_SELENIUM):
            self.driver.refresh()
            
    @loggerd
    def run(self):
        while True:
            pass