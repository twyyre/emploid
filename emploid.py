from os import listdir
from time import sleep
class Emploid:

    def __init__(self) -> None:

        import pyautogui as pa
        import numpy as np
        import cv2 as cv
        from api import API
        from scribe import Scribe

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

    def import_image(self, _dir, _internal=True):
        if(_internal):
            path = self.internal_path+_dir
            return self.cv.imread(path)
        else:
            return self.cv.imread(_dir)

    def press(self):
        'left' 'middle' 'right'
        self.pa.click()
        
    def click(self, _elm):
        elm = _elm
        self.pa.click(elm)

    def lclick(self, _elm):
        self.pa.leftClick(_elm)

    def rclick(self, _elm):
        self.pa.rightClick(_elm)

    def dbclick(self, _elm):
        self.pa.doubleClick(_elm)

    def mdclick(self, _elm):
        self.pa.middleClick(_elm)

    def input_into(self, _str):
        self.pa.write(_str)

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
        
    def moveto(self, _elm):
        self.pa.moveTo(_elm, duration = 0.1)

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

    def promise(self, _func, *_args, _tooltip="<no tooltip>", _tries=15, _delay=2, _fullerror=True, _noerror=False, _noprint=False):


        if(_tooltip==""):
            _tooltip="<no tooltip>"

        print(f"----------------({_tooltip})----------------")

        if(not _tries==None):
            if(_tries < 1):
                _tries = None

        state = True
        trigger = False

        while ((trigger==False) and (_tries==None or _tries > 0)):

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
                        print(_tooltip + " failed ("+str(_tries)+f". . .) {_str}")

                sleep(_delay)
                state = False
        return state

    def execute_steps(self, _delay=1):

        for step in self.steps:

            element = self.cv.imread(self.elm_path+f"/{step}")

            while True:

                elm_pos = self.pa.locateOnScreen(element)

                if(elm_pos):

                    print(f"{step} detected")

                    if("DELAYY" in step):
                        sleep(8)
                    elif("DELAY" in step):
                        sleep(5)

                    if "DBC" in step:
                        print("action: Double click")
                        self.pa.doubleClick(element)

                    elif "LC" in step:
                        print("action: Left click")

                        while True:
                            try:
                                self.lclick(element)
                                break
                            except:
                                pass

                    elif "RC" in step:
                        print("action: Right click")
                        self.rclick(element)

                    elif "DRG" in step:
                        print("action: DRAG")
                        target = f"elements/{self.steps[self.steps.index(step)+1]}"
                        self.pa.moveTo(x=element)
                        self.pa.keyDown(self.pa.PRIMARY)
                        self.drag_element = element
                        self.pa.moveTo(x=target)
                        self.pa.keyUp(self.pa.PRIMARY)
                    
                    elif "LA" in step:

                        needle = element
                        needles = list(self.pa.locateAllOnScreen(needle))
                        self.pa.leftClick(needles[-1])
                        
                        # if("LC" in step):
                        #     self.pa.leftClick(needles[-1])
                        # if("DC" in step):
                        #     self.pa.leftClick(needles[-1])
                        #     self.pa.leftClick(needles[-1])

                        print(needles)

                    if "INPT_FIRSTNAME" in step:
                        
                        if(self.LANG==ARABIC):
                            from usernames import ar_fnames as fnames
                        if(self.LANG==ENGLISH):
                            from usernames import en_fnames as fnames

                        index = randint(0, len(fnames)-1)
                        self.fname = fnames[index]

                        print("move to element")
                        self.pa.moveTo(elm_pos)
                        # sleep(1)
                        print("click element")
                        self.pa.click()
                        # sleep(2)
                        self.pa.click()

                        # sleep(2)
                        # self.pa.doubleClick()

                        # with(open("fname.txt", "w", encoding="utf-8") as f):
                        #     f.write(self.fname)
                        # sleep(1)
                        # with(open("fname.txt", "r", encoding="utf-8") as f):
                        #     self.fname = f.read()

                        self.write(self.fname)
                        

                        # Store our string to the clipboard
                        # pyperclip.copy(self.fname)
                        # pyperclip.copy(self.fname)
                        # sleep(2)
                        # Hotkey the paste command
                        # self.pa.hotkey("crtl", "v")
                        # for i in self.fname:
                        #     self.pa.keyDown(i)
                    


                    if "INPT_LASTNAME" in step:

                        print("0")
                        
                        if(self.LANG==ARABIC):
                            from usernames import ar_lnames as lnames
                        if(self.LANG==ENGLISH):
                            from usernames import en_lnames as lnames

                        index = randint(0, len(lnames)-1)
                        self.lname = lnames[index]

                        print("move to element")
                        self.pa.moveTo(elm_pos)

                        print("click element")
                        self.pa.click()
                        # sleep(2)
                        self.pa.click()


                        # sleep(2)
                        # self.pa.click(element)
                        print(self.lname)

                        # with(open("lname.txt", "w", encoding="utf-8") as f):
                        #     f.write(self.lname)
                        # sleep(1)
                        # with(open("lname.txt", "r", encoding="utf-8") as f):
                        #     self.lname = f.read()

                        self.pa.write(self.lname)

                        # pyperclip.copy(self.lname)
                        # pyperclip.copy(self.lname)
                        # sleep(1)
                        # # Hotkey the paste command
                        # self.pa.hotkey("ctrl", "v")
                        # self.pa.doubleClick()
                        # sleep(2)
                        # for i in self.lname:
                        #     self.pa.keyDown(i)

                        self.fullname = self.fname + " " + self.lname
                        

                    if "INPT_EMAIL" in step:
                        
                        if(self.LANG==ARABIC):
                            self.pa.keyDown('alt')
                            self.pa.press('shift')
                            self.pa.keyUp('ALT')
                            
                        self.pa.doubleClick(element)
                        # sleep(2)
                        for i in self.email:
                            self.pa.keyDown(i)
                        
                    if "INPT_PASSWORD" in step:
                        sleep(2)
                        for i in self.password:
                            self.pa.keyDown(i)

                    if "INPT_CODE" in step:

                        self.pa.leftClick(element)

                        print("checking for new messages...")

                        try:
                            while (not len(self.mails)):
                                self.mails = self.account.get_messages()
                                sleep(2)

                            print("mail received!")

                            mail = self.mails[0]

                            code = self.find_code(5, str(mail.text))
                            
                            print("code:", code)

                            for i in code:
                                self.pa.keyDown(i) 
                                
                            

                        except Exception as e:
                            print(e)
                            pass

                    if "CONFIRMED" in step:

                        from api import API
                        register = API().api_profile_register(_profile_email=self.email, _profile_password=self.password, _profile_name=self.fullname)
                        print(register)
                            
                    break

                else:
                    print(f"{step} not found, waiting. . .")

                
                # sleep(_delay)



    



