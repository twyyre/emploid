from emploid import Emploid
from api import API
from time import sleep
from load_elements import *
import pyperclip

def action_get_user_info(emp, _type):
    #choose type
    types = [element_user_type_branch_employee, element_user_type_bank_employee, element_user_type_system_admin]
    user_type = types[_type]

    #
    def func_(emp):
        sleep(2)
        user_list = emp.locate_all(element_user_edit_btn)
        if(user_list):
            print("user detected")
            emp.click(user_list[0])
        else:
            print("could not detect user rows")
    emp.promise(_func=func_, _delay=0, _tooltip="check for rows")

    #
    def func_(emp):
        #check for types of user
        elm = emp.locate(user_type, _confidence=0.9)
        emp.click(elm)
    emp.promise(_func=func_, _delay=0, _tooltip="click on edit")

    #
    def func_(emp):
        #I'm going to need to look for the three lemenets for user types and see which one is NOT detected. Because Pyautogui will not be able to detect the chosen option since the image is changed when selected.
        pass
    emp.promise(_func=func_, _delay=0, _tooltip="choose user type")

    #
    def func_(emp):
        elm = emp.locate(element_user_edit_name_input, _confidence=0.9)

        global name

        emp.moveto(elm)
        emp.mouse_move_relative(_xoffset=0, _yoffset=50, _seconds=0)  
        emp.mouse_move_relative(_xoffset=-50, _yoffset=0, _seconds=0)  
        emp.press() #name
        emp.keyboard_hotkey("ctrl", "a")
        emp.keyboard_hotkey("ctrl", "c")
        name = emp.clipboard_copy()
    emp.promise(_func=func_, _delay=0, _tooltip="input user name")

    #
    def func_(emp):
        elm = emp.locate(element_user_edit_username_input, _confidence=0.9)
        global username
        import pyperclip
        username = pyperclip.copy(username)
        emp.moveto(elm)
        emp.mouse_move_relative(_xoffset=0, _yoffset=50, _seconds=0)  
        emp.mouse_move_relative(_xoffset=-50, _yoffset=0, _seconds=0)  
        emp.press() #name
        
        emp.keyboard_hotkey("ctrl", "a")
        emp.keyboard_hotkey("ctrl", "c")
        username = emp.clipboard_copy()
    emp.promise(_func=func_, _delay=0, _tooltip="input username")

    #
    def func_(emp):
        elm = emp.locate(element_user_edit_email_input, _confidence=0.9)
        global email
        import pyperclip
        email = pyperclip.copy(email)
        emp.moveto(elm)
        emp.mouse_move_relative(_xoffset=0, _yoffset=50, _seconds=0)  
        emp.mouse_move_relative(_xoffset=-50, _yoffset=0, _seconds=0)  
        emp.press() #name
        emp.keyboard_hotkey("ctrl", "a")
        emp.keyboard_hotkey("ctrl", "c")
        email = emp.clipboard_copy()
    emp.promise(_func=func_, _delay=0, _tooltip="input user email")

    emp.mouse_scroll_down()

    #
    def func_(emp):
        elm = emp.locate(element_user_edit_mobile_input, _confidence=0.9)
        global mobile
        import pyperclip
        mobile = pyperclip.copy(mobile)
        emp.moveto(elm)
        emp.mouse_move_relative(_xoffset=0, _yoffset=50, _seconds=0)  
        emp.mouse_move_relative(_xoffset=-50, _yoffset=0, _seconds=0)  
        emp.press() #name
        emp.keyboard_hotkey("ctrl", "a")
        emp.keyboard_hotkey("ctrl", "c")
        mobile = emp.clipboard_copy()
    emp.promise(_func=func_, _delay=0, _tooltip="input user mobile")

    print("name:", name)
    print("username:", username)
    print("email:", email)
    print("mobile:", mobile)

    #
    def func_(emp):
        elm = emp.locate(element_user_exit_edit_screen, _confidence=0.9) 
        emp.click(elm)
    emp.promise(_func=func_, _delay=0, _tooltip="exit edit screen")