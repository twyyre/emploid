from os import listdir
from time import sleep

class Emploid:

    def __init__(self) -> None:
        import pyautogui as pa
        import numpy as np
        import cv2 as cv
        from api import API
        from modules.emp_scribe import Scribe

        self.pa = pa
        self.cv = cv
        self.np = np
        self.api = API
        self.scribe = Scribe

        self.steps = []
        self.internal_path = "elements/"

        # self.average_scroll_distance = 50
        self.keys = self.pa.KEYBOARD_KEYS

    def show(self, *_args):
        for arg in _args:
            print("----", arg)
        print("\n------------------------")

    def get_steps(self):
        self.steps = listdir(self.internal_path)

        # for dir in self.steps:
        #     self.steps[0].append(dir)
        #     print("dir:"+self.steps[0][0])

        print(f"got ({len(self.steps)}) steps")
        
    def image_compare(self, _img1, _img2):

        # load the input images
        img1 = _img1
        img2 = _img2

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

    def import_image(self, _dir, _internal=True, _report=True):
        if(_internal):
            path = self.internal_path+_dir
            import numpy as np
            elm = self.cv.imread(path)
            if(elm is not None):
                if(_report):
                    # print(f"element ({_dir}) IMPROTED successfully")
                    pass
                return elm
            else:
                if(_report):
                    print(f"element ({_dir}) FAILED to import")
                    pass
        else:
            return Exception("non-internal paths are not currently suppoorted")
        
    def promise_element(self, _ent):

        import pyscreeze
        a = isinstance(_ent, pyscreeze.Box)

        if(a):
            return _ent
        else:
            def func_(self):

                print("locating element")
                elm = self.locate(_ent)

                if(elm):
                    print("detected")
                    return elm
                else:
                    print("could not detect element")
                    return False
            return self.promise(_func=func_, _tooltip=f"promising element...")

    def press(self):
        'left' 'middle' 'right'
        self.pa.click()
        
    def click(self, _elm, _tooltip="Click", _tries=3, _delay=1, _exit=False):
        def func_(self):
            elm = _elm
            elm = self.promise_element(_elm)
            if(elm):
                self.pa.click(elm)
                return True
            else:
                raise Exception("could not click element")
        return self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)

    def lclick(self, _elm, _tooltip="Left Click", _tries=3, _delay=1, _exit=False):
        def func_(self):
            elm = _elm
            elm = self.promise_element(_elm)
            if(elm):
                self.pa.leftClick(elm)
                return True
            else:
                raise Exception("could not left click element")
        return self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)

    def rclick(self, _elm, _tooltip="Right Click", _tries=3, _delay=1, _exit=False):
        def func_(self):
            elm = _elm
            elm = self.promise_element(_elm)
            if(elm):
                self.pa.rightClick(elm)
                return True
            else:
                raise Exception("could not right click element")
        return self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)

    def dbclick(self, _elm, _tooltip="Double Click", _tries=3, _delay=1, _exit=False):
        def func_(self):
            elm = _elm
            elm = self.promise_element(_elm)
            if(elm):
                self.pa.doubleClick(elm)
                return True
            else:
                raise Exception("could not double click element")
        return self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)

    def mdclick(self, _elm, _tooltip="Middle Click", _tries=3, _delay=1, _exit=False):
        def func_(self):
            elm = _elm
            elm = self.promise_element(_elm)
            if(elm):
                self.pa.middleClick(elm)
                return True
            else:
                raise Exception("could not middle click element")
        return self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)

    def get_func_name(self, _level=1):
        #level is the scope level of function to get the name of
        #_level 0 will return name of this function
        #_level 1 (default) will return name of function that called this function
        #etc
        import inspect
        return str(inspect.stack()[_level][3])

    def input_into(self, _str, _elm=None, _tooltip="Input Text into Element", _tries=3, _delay=1, _exit=False):
        #inputs text into whatever element is active on screen.
        #if an element is passed, it clicks it before passing the text
        def func_(self):
            if(_elm is not None):
                clicked = self.click(_elm, _tooltip=_tooltip)
                if(clicked):
                    self.pa.write(_str)
            return True
        self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)
    
    def keyboard_press(self, _key):
        self.pa.press(_key)

    def keyboard_hold(self, _key):
        self.pa.keyDown(_key)

    def keyboard_release(self, _key):
        self.pa.keyUp(_key)
    
    def keyboard_hotkey(self, *_keys):
        self.pa.hotkey(*_keys) 

    def locate(self, _elm, _confidence=0.9, _grayscale=True):
        return self.pa.locateOnScreen(_elm, confidence=_confidence, grayscale=_grayscale)#, region=(0,0, 300, 400))
    
    def locate_in_region(self, _elm, _x, _y, _xx, _yy, _confidence=0.9, _grayscale=True):
        return self.pa.locateOnScreen(_elm, confidence=_confidence, grayscale=_grayscale, region=[_x, _y, _xx, _yy])
        
    def locate_all(self, _elm, _confidence=0.9, _grayscale=True):
        return list(self.pa.locateAllOnScreen(_elm, confidence=_confidence, grayscale=_grayscale))

    def prompt(self, _str):
        return self.pa.prompt(_str)

    def confirm(self, _str):
        value = self.pa.confirm(_str)
        if(value.lower()=="cancel"):
            return False
        if(value.lower()=="ok"):
            return True

    def alert(self, _str):
        return self.pa.alert(_str)
        
    def moveto(self, _elm, _tooltip="Move Mouse to Element", _tries=3, _delay=1, _exit=False):
        def func_(self):
            elm = _elm
            elm = self.promise_element(_elm)
            if(elm):
                self.pa.moveTo(elm, duration = 0.1)
                return True
            else:
                raise Exception
        return self.promise(_func=func_, _tooltip=_tooltip, _tries=_tries, _delay=_delay, _exit=_exit)

    def mouse_scroll(self, _value: float, _x: float=None, _y: float=None):
        self.pa.scroll(_value, x=_x, y=_y) #positive up, negative down

    def mouse_scroll_up(self, _value: float=250, _x: float=None, _y: float=None):
        value = abs(_value)
        self.mouse_scroll(value, _x, _y)

    def mouse_scroll_down(self, _value: float=-250, _x: float=None, _y: float=None):
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

    def set_delay(self, _value: float):
        self.pa.PAUSE = _value

    def set_failsafe(self, _value: bool):
        self.pa.FAILSAFE = _value

    def mouse_move_relative(self, _xoffset=0, _yoffset=0, _seconds=0):
        self.pa.moveRel(_xoffset, _yoffset, duration=_seconds)

    def mouse_move(self, _x, _y, _seconds):
        self.pa.moveTo(_x, _y, duration=_seconds)

    def mouse_drag_to(self, _x, _y, _seconds):
        self.pa.dragTo(_x, _y, duration=_seconds)  # drag mouse to XY

    def mouse_drag_to_relative(self, _xoffset, _yoffset, _seconds):
        self.pa.dragTo(_xoffset, _yoffset, duration=_seconds) 

    def program_run(self, _path):
        from pywinauto import Desktop, Application
        prog_path = _path

        program_name = prog_path.split("/")[-1]
        program_name = program_name.split("\\")[-1]
        
        prog = Application().start(prog_path)
        return prog#Application(backend='uia').connect(path=program_name, title_re='New Tab')
    
    def chrome_run(self, _url: str="", _incognito=False, _maximized=True):

        if(_incognito):
            _incognito = "-incognito"
        else:
            _incognito = ""

        if(_maximized):
            _maximized = "--start-maximized"
        else:
            _maximized = ""

        from pywinauto import Desktop, Application
        chrome_dir = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        page_url = _url
        chrome = Application().start(chrome_dir + f' --force-renderer-accessibility {_incognito} {_maximized} ' + _url)
        app_new_tab = Application(backend='uia').connect(path='chrome.exe', title_re='New Tab')

    def email_generate(self):
        
        self.show("getting email...")

        while True:
            
            try:
                from pymailtm import MailTm, Account, Message
                return MailTm().get_account()
            except:
                pass

    def email_listen(self, _email):
        try:
            mails = []

            while (not len(mails)): #this needs modification
                mails = _email.get_messages()
                sleep(2)

            mail = mails[0]
            code = self.find_code(5, str(mail.text))
            
        except Exception as e:
            print(e)
            pass

    def email_find_code(self, n, s):
        import re
        result = re.search('\d{%s}'%n, s)
        return result.group(0) if result else result

    def send_get(self, _url, _params=None):
        return self.api.get(_url, _params=_params)
    
    def send_post(self, _url, _params):
        return self.api.post(_url=_url, _params=_params)
    
    def clipboard_copy(self):
        import win32clipboard
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        return data
    
    def detect(self, _elm):
        
        def func_(self, _confidence=0.9):

            print("locating element")
            elm = self.locate(_elm, _confidence=_confidence)

            if(elm):
                print("detected")
                return elm
            else:
                print("could not detect element")
                return False
        return self.promise(_func=func_, _tooltip=f"attempt to locate element...")

    def promise(self, _func, *_args, _tooltip="", _tries=3, _delay=1, _fullerror=True, _noerror=False, _noprint=False, _exit=False):

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
            return state
    
    def screen_get_size(self):
        return self.pa.size()
    
    def screen_get_width(self):
        return self.pa.size()[0]
    
    def screen_get_heigfht(self):
        return self.pa.size()[1]
        
    def point_in_screen(self, _x, _y):
        return self.pa.onScreen(_x, _y)