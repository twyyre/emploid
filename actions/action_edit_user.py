from emploid import Emploid
from api import API
from time import sleep
from load_elements import *
import pyperclip


def action_edit_user(emp, _name, _username,_email, _mobile, _password, _type):

    name = _name
    username = _username
    email = _email #email.address
    mobile = _mobile
    password = _password
    confirm_password = _password

    #choose type
    types = [element_user_type_branch_employee, element_user_type_bank_employee, element_user_type_system_admin]
    user_type = types[_type]

    #
    def func_(emp):
        user_list = emp.locate_all(element_user_edit_btn)

        if(user_list):
            emp.click(user_list[0], _tooltip="click on edit btn")
        else:
            raise Exception("could not detect btns")

    emp.click(user_type, _tooltip="choose user type")

    #
    def func_(emp):
        global name
        import pyperclip
        name = pyperclip.copy(name)
        emp.moveto(element_user_edit_name_input)
        emp.mouse_move_relative(_xoffset=0, _yoffset=50, _seconds=0)  
        emp.mouse_move_relative(_xoffset=-50, _yoffset=0, _seconds=0)  
        emp.press() #name
        emp.keyboard_hotkey("ctrl", "a")
        emp.keyboard_hotkey("ctrl", "v")
    emp.promise(_func=func_, _tooltip="input user name")

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
        emp.keyboard_hotkey("ctrl", "v")
    emp.promise(_func=func_, _tooltip="input username")

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
        emp.keyboard_hotkey("ctrl", "v")
    emp.promise(_func=func_, _tooltip="input user email")

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
        emp.keyboard_hotkey("ctrl", "v")
    emp.promise(_func=func_, _tooltip="input user mobile")

    # #
    # def func_(emp):
    #     elm = emp.locate(element_user_add_password_input, _confidence=0.9)
    #     emp.click(elm) #password
    #     emp.input_into(password)
    # emp.promise(_func=func_, _tooltip="input user password")

    # #
    # def func_(emp):
    #     elm = emp.locate(element_user_add_password_confirm_input, _confidence=0.9)
    #     emp.click(elm) #confirm password
    #     emp.input_into(confirm_password)
    # emp.promise(_func=func_, _tooltip="confirm user password")

    # emp.mouse_scroll_down() #so that the submit button is visible

    #
    def func_(emp):
        elm = emp.locate(element_user_edit_btn_2, _confidence=0.9)
        emp.click(elm) #confirm password
    emp.promise(_func=func_, _tooltip="click submit btn")

    #
    def func_(emp):
        elm = emp.locate(element_user_add_success_message, _confidence=0.9)
        if(elm):
            show("user added successfully")
        else:
            show("failed to add user")
    emp.promise(_func=func_, _tooltip="check for success message")

    #
    def func_(emp):
        elm = emp.locate(element_user_add_success, _confidence=0.9)
        emp.click(elm) #confirm password
    emp.promise(_func=func_, _tooltip="click ok btn")