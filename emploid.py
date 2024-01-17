import os
from os import listdir
from time import sleep
from modules.taskman.taskman import Taskman
import cv2 as cv
import numpy as np
import random
import string
import pyautogui as pa
import numpy as np
from api import API
from modules.scribe.scribe import Scribe
from api import API
import tools
from constants import *
import pyperclip as clip
import subprocess as sp
import sys
from appium import webdriver as AppiumDriver
from appium.webdriver.common.appiumby import AppiumBy as By
from appium.options.android import UiAutomator2Options # Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
from appium.options.common import AppiumOptions
from appium.webdriver.common.touch_action import TouchAction as AppiumAction
from appium.webdriver.extensions.android.nativekey import AndroidKey as ak

class Emploid:

    def __init__(self, _driver_type=SETTINGS_USE_PYAUTOGUI) -> None:
        
        self.api = API()
        self.confidence=0.77
        self.pa = pa
        self.cv = cv
        self.np = np
        self.api = API
        self.scribe = Scribe()
        self.scribe.new_page("emploid report")
        self.set_failsafe(False)
        self.set_delay(0.2)
        self.element_count = 0
        self.steps = []
        self.internal_path = "elements/"
        self.driver_type = _driver_type if _driver_type is not None else SETTINGS_USE_PYAUTOGUI
        self.driver = None if self.driver_type==SETTINGS_USE_PYAUTOGUI else AppiumDriver()
        # self.average_scroll_distance = 50
        self.keys = self.pa.KEYBOARD_KEYS

        # if(self.screen_get_size()!=(1920, 1080)): #this is no longer needed because elements now can be detected regardless of resolution
        #     raise Exception("resolution is not supported. Screen Resolution must be (1920x1080).")
        load_entities_function = self.load_elements if self.driver_type==SETTINGS_USE_PYAUTOGUI else self.load_identifiers
        load_entities_function()
        self.appium_server = None
        self.emu = None
        # if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
        #     self.load_elements()
        # if(self.driver_type==SETTINGS_USE_APPIUM or self.driver_type==SETTINGS_USE_SELENIUM):
        #     self.load_identifiers()
        # self.taskman = Taskman()
        # self.beholder = self.taskman.start_task("record.py")

    def __del__(self):
        # self.taskman.kill_task(self.beholder, _delay=2)
        pass

    def show(self, *_args) -> None:
        for arg in _args:
            print("----", arg)
        print("\n------------------------")

    def load_elements(self):
        import os
        import tools
        directories = list(os.walk('elements'))

        with(open("load_elements.py", 'w', encoding='utf-8') as f):
            f.write("from emploid import Emploid\nimport cv2 as cv\nfrom api import API\nfrom time import sleep\nemp = Emploid()\n")
            if(len(directories)):
                for dir in directories:
                    for png in dir[2]:
                        if(png[-4:]==".png"):
                            line = "element_"+png[:-4]+"=emp.import_image(\""+dir[0].replace("\\", "/")+"/"+png+"\", cv.IMREAD_GRAYSCALE)\n"
                            line = line.replace("elements/", "")
                            f.write(line)
                else:
                    print("failed to load [element_"+png[:-4]+"]")
        content = tools.f_read("load_elements.py")

        tools.f_write("load_elements.py", content)
    
    def load_identifiers(self):
        import identifiers as id

    def get_steps(self) -> list[str]:
        self.steps = listdir(self.internal_path)

        # for dir in self.steps:
        #     self.steps[0].append(dir)
        #     print("dir:"+self.steps[0][0])

        print(f"got ({len(self.steps)}) steps")
        
    def image_compare(self, _img1, _img2) -> float:

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

    def convert_to_grayscale(self, _img):
        return self.cv.cvtColor(_img, self.cv.COLOR_BGR2GRAY)
    
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
    
    def scale_to(self, _img1, _img2):
        #scales image 1 to image 2 size
        image3 = cv.resize(_img1, (_img2.shape[1], _img2.shape[0]), cv.INTER_LINEAR_EXACT)
        
        if(image3.shape == _img2.shape):
            return image3
        else:
            return False

    def import_image(self, _dir, _method=cv.IMREAD_GRAYSCALE, _internal=True, _report=True):
        if(_internal):
            path = self.internal_path+_dir
            elm = self.cv.imread(path, _method)
            if(elm is not None):
                if(_report):
                    # print(f"element ({_dir}) IMPROTED successfully")
                    self.element_count += 1
                    pass
                return elm
            else:
                if(_report):
                    print(f"element ({_dir}) FAILED to import")
                    pass
        else:
            return Exception("non-internal paths are not currently suppoorted")
        
    def import_images(self, _dir, _internal=True):
        from os import listdir
        from os.path import isfile, join

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
    
    def promise_element(self, _ent, _confidence=0.9):
        #This function needs modification, it doesn't raise an exception when the element is not found where it should. Will look into it later.
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            import pyscreeze
            is_element = isinstance(_ent, pyscreeze.Box)
            return  _ent if is_element else None
        if(self.driver_type==SETTINGS_USE_SELENIUM):
            from selenium.webdriver.remote.webelement import WebElement
            is_element = isinstance(_ent, WebElement)
        if(self.driver_type==SETTINGS_USE_APPIUM):
            from appium.webdriver.webelement import WebElement
            is_element = isinstance(_ent, WebElement)

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
            return self.promise(_func=func_, _tooltip=f"promising element...")
    
    def keyboard_paste(self, _str) -> None:
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            clip.copy(_str)
            self.keyboard_hotkey("ctrl", "v")

    def press(self, _btn: int =0) -> None:
        
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            btns = ['left', 'right', 'middle' ]
            self.pa.click(button=btn)
            btn = btns[_btn]
        if(self.driver_type==SETTINGS_USE_APPIUM):
            return AppiumAction.press(_btn).perform()
            
        if(self.driver_type==SETTINGS_USE_SELENIUM):
            raise Exception("not yet supported")

    def swipe(self):
        self.driver.swipe(470, 1400, 470, 0, 400)
        
    def click(self, _elm, _tooltip="Click", _tries=3, _delay=1, _confidence=0.8, _exit=False) -> bool:
        def func_(self):
            elm = _elm
            elm = self.promise_element(_elm, _confidence=_confidence)
            if(elm):
                self.pa.click(elm)
                return True
            else:
                raise Exception("could not click element")
        return self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)

    def lclick(self, _elm, _tooltip="Left Click", _tries=3, _delay=1, _exit=False)  -> bool:
        def func_(self):
            elm = _elm
            elm = self.promise_element(_elm)
            if(elm):
                self.pa.leftClick(elm)
                return True
            else:
                raise Exception("could not left click element")
        return self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)

    def rclick(self, _elm, _tooltip="Right Click", _tries=3, _delay=1, _exit=False) -> bool:
        def func_(self):
            elm = _elm
            elm = self.promise_element(_elm)
            if(elm):
                self.pa.rightClick(elm)
                return True
            else:
                raise Exception("could not right click element")
        return self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)

    def dbclick(self, _elm, _tooltip="Double Click", _tries=3, _delay=1, _exit=False) -> bool:
        def func_(self):
            elm = _elm
            elm = self.promise_element(_elm)
            if(elm):
                self.pa.doubleClick(elm)
                return True
            else:
                raise Exception("could not double click element")
        return self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)

    def mdclick(self, _elm, _tooltip="Middle Click", _tries=3, _delay=1, _exit=False) -> bool:
        def func_(self):
            elm = _elm
            elm = self.promise_element(_elm)
            if(elm):
                self.pa.middleClick(elm)
                return True
            else:
                raise Exception("could not middle click element")
        return self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)

    def get_func_name(self, _level=1) -> str:
        #level is the scope level of function to get the name of
        #_level 0 will return name of this function
        #_level 1 (default) will return name of function that called this function
        #etc
        import inspect
        return str(inspect.stack()[_level][3])

    def input_into(self, _str, _elm=None, _tooltip="Input Text into Element", _confidence=0.77, _tries=3, _delay=1, _exit=False) -> bool:
        #inputs text into whatever element is active on screen.
        #if an element is passed, it clicks it before passing the text
        #THIS FUNCTION CURRENTLY WORKS WITH ELEMENTS ONLY. ELEMENTS MUST BE PASSED INTO IT.
        def func_(self):
            if(_elm is not None):
                clicked = self.click(_elm,  _confidence=_confidence, _tooltip=_tooltip)
                if(clicked):
                    if(self.contains_arabic_letters(_str)):
                        print("string contains arabic letters")
                        clip.copy(_str)
                        clip.paste()
                        # self.keyboard_hotkey("ctrl", "v")

                    else:
                        self.pa.write(_str)
                    return True
            raise Exception("could not input into element")
        self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)
    
    def keyboard_press(self, _key) -> None:
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            self.pa.press(_key)
        if(self.driver_type==SETTINGS_USE_APPIUM):
            self.driver.press_keycode(ak.ENTER)
        if(self.driver_type==SETTINGS_USE_SELENIUM):
            raise Exception("not supported right now")

    def keyboard_hold(self, _key) -> None:
        self.pa.keyDown(_key)

    def keyboard_release(self, _key) -> None:
        self.pa.keyUp(_key)
    
    def keyboard_hotkey(self, *_keys) -> None:
        self.pa.hotkey(*_keys) 

    def find_element(self, _xpath, _method=By.XPATH):
        return self.driver.find_element(_method, _xpath)
    
    def find_elements(self, _xpath, _method=By.XPATH):
        return self.driver.find_elements(_method, _xpath)
    
    def locate(self, _elm, _confidence=0.9, _mode=DETECTION_MODE_REGULAR, _grayscale=True): 
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
                tools.pause()
                _elm = self.detect_template(self, _elm, _screen)
                cv.imwrite("result.png", _elm)
                _elm = cv.imread("result.png")

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
            
    def locate_all(self, _elm, _confidence=0.9, _mode=DETECTION_MODE_REGULAR, _grayscale=True):
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

    def contains_arabic_letters(self, input_string):
        #written by chat-gpt
        import re
        # Define a regular expression pattern for Arabic letters
        arabic_letters_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+')

        # Check if the input string contains Arabic letters
        return bool(arabic_letters_pattern.search(input_string))
        
    def prompt(self, _str) -> None:
        return self.pa.prompt(_str)

    def confirm(self, _str):
        value = self.pa.confirm(_str)
        if(value.lower()=="cancel"):
            return False
        if(value.lower()=="ok"):
            return True

    def alert(self, _str):
        return self.pa.alert(_str)
        
    def moveto(self, _elm, _tooltip="Move Mouse to Element", _tries=3, _delay=1, _exit=False) -> bool:
        def func_(self):
            elm = _elm
            elm = self.promise_element(_elm)
            if(elm):
                self.pa.moveTo(elm, duration = 0.1)
                return True
            else:
                raise Exception
        return self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)

    def mouse_scroll(self, _value: float, _x: float=None, _y: float=None) -> None:
        self.pa.scroll(_value, x=_x, y=_y) #positive up, negative down

    def mouse_scroll_up(self, _value: float=250, _x: float=None, _y: float=None) -> None:
        value = abs(_value)
        self.mouse_scroll(value, _x, _y)

    def mouse_scroll_down(self, _value: float=-250, _x: float=None, _y: float=None) -> None:
        value = -abs(_value)
        self.mouse_scroll(value, _x, _y)

    def get_pixel(self, _elm=None, _px=0, _py=0):
        #To obtain the RGB color of a pixel in a screenshot, use the Image object’s getpixel() method:
        if(_elm):
            return _elm.getpixel((_px, _py))
        else:
            return self.pa.pixel((_px, _py))

    def get_screenshot(self, _screen_name : str):
        return self.pa.screenshot(_screen_name)

    def get_mouse_pos(self):
        return self.pa.position()

    def set_delay(self, _value: float) -> None:
        self.pa.PAUSE = _value

    def set_failsafe(self, _value: bool) -> None:
        self.pa.FAILSAFE = _value

    def mouse_move_relative(self, _xoffset=0, _yoffset=0, _seconds=0) -> None:
        self.pa.moveRel(_xoffset, _yoffset, duration=_seconds)

    def mouse_move(self, _x, _y, _seconds=0) -> None:
        self.pa.moveTo(_x, _y, duration=_seconds)

    def mouse_drag_to(self, _x, _y, _seconds) -> None:
        self.pa.dragTo(_x, _y, duration=_seconds)  # drag mouse to XY

    def mouse_drag_to_relative(self, _xoffset, _yoffset, _seconds) -> None:
        self.pa.dragTo(_xoffset, _yoffset, duration=_seconds) 

    def program_run(self, _path):
        from pywinauto import Desktop, Application
        prog_path = _path
        program_name = prog_path.split("/")[-1]
        program_name = program_name.split("\\")[-1]
        prog = Application().start(prog_path)
        return prog#Application(backend='uia').connect(path=program_name, title_re='New Tab')
    
    def chrome_run(self, _url: str="", _incognito=False, _maximized=True) -> None:
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
            self.driver.get(TEST_URL)
        if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
            from pywinauto import Desktop, Application
            chrome_dir = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            page_url = _url
            chrome = Application().start(chrome_dir + f' --force-renderer-accessibility {_incognito} {_maximized} ' + _url)
            app_new_tab = Application(backend='uia').connect(path='chrome.exe', title_re='New Tab')
            return True

    def get_otp(self, _sn=797693694):
        _url=f"http://10.10.20.46:9832/Pages/UpdateOtpState?Sn={_sn}&state=1&culture=ar-LY"
        result = self.api.get(_url)
        return result

    def email_generate(self):
        
        self.show("getting email...")

        while True:
            
            try:
                from pymailtm import MailTm, Account, Message
                return MailTm().get_account()
            except:
                pass

    def email_listen(self, _email) -> str:
        try:
            mails = []
            while (not len(mails)): #this needs modification
                mails = _email.get_messages()
                sleep(2)
            mail = mails[0]
            return self.find_code(5, str(mail.text))
        except Exception as e:
            print(e)
            pass

    def email_find_code(self, n, s) -> str:
        import re
        result = re.search('\d{%s}'%n, s)
        return result.group(0) if result else result

    def send_get(self, _url, _params=None, _json=True):
        return self.api.get(_url, _params=_params, _json=_json)
    
    def send_post(self, _url, _params, _json=True):
        return self.api.post(_url=_url, _params=_params, _json=_json)
    
    def clipboard_copy(self):
        import win32clipboard
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return data
    
    def detect(self, _elm):
        def func_(self, _confidence=0.9):
            print("locating element")
            elm = self.promise_element(_elm)
            if(elm):
                print("detected")
                return elm
            else:
                print("could not detect element")
                return False
        return self.promise(_func=func_, _tooltip=f"attempt to locate element...")

    def promise(self, _func, *_args, _tooltip="", _tries=3, _delay=1, _fullerror=True, _noerror=False, _noprint=False, _exit=False, _scribble=False):
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
                if(result):
                    col = "btn-success"
                else:
                    col = "btn-danger"
                self.scribe.insert_row(0, _tooltip, "True", result, col, _scribble=_scribble)

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
            self.scribe.insert_row(0, _tooltip, "True", state, "btn-danger")
            return state
    
    def screen_get_size(self):
        return self.pa.size()

    def screen_get_width(self):
        return self.pa.size()[0]

    def screen_get_heigfht(self):
        return self.pa.size()[1]
        
    def point_in_screen(self, _x, _y):
        return self.pa.onScreen(_x, _y)

    def random_string(self, _length):
        pass

    def appium_server_start(self):
        print("starting appium server...")
        info = sp.STARTUPINFO()
        info.dwFlags = sp.STARTF_USESHOWWINDOW
        info.wShowWindow = 1
        self.appium_server = sp.Popen([sys.executable, APPIUM_SERVER_EXE], shell=True, startupinfo=info, creationflags=sp.CREATE_NEW_CONSOLE)
        return self.appium_server
    
    def appium_emulator_start(self):
        print("starting emulator...")
        self.emu = sp.Popen(APPIUM_COMMAND_EMULATOR_START, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
        return self.emu
    
    def appium_connect(self):
        capabilities = dict(
            platformName='Android',
            automationName='uiautomator2',
            deviceName='Samsung S9',
            appPackage='',
            appActivity='',
            language='en',
            locale='US'
        )
        while True:
            try:
                print("connecting to appium server...")
                self.driver = AppiumDriver.Remote(APPIUM_SERVER_URL, options=AppiumOptions().load_capabilities(capabilities))
                break
            except:
                pass

    def appium_server_stop(self):
        """this currently does not work for some reason"""
        if(self.appium_server):
            self.appium_server.kill()
            os.system(f"taskkill /F /IM node.exe")

    def appium_emulator_stop(self):
        if(self.emu):
            self.emu.kill()

    def move_to(self, _element):
        return AppiumAction.move_to(_element).perform()
    
    def mouse_release(self):
        AppiumAction.release().perform()
        
    def activate_app(self, _app):
        return self.driver.activate_app(_app)

    def generate_random_string(length):
        from random import choice
        """Generate a random string of the specified length"""
        # Define the characters that can be used in the random string
        characters = string.ascii_letters + string.digits
        # Generate the random string
        random_string = ''.join(choice(characters) for i in range(length))
        return random_string

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