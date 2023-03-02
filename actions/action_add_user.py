from emploid import Emploid
from api import API
from time import sleep
from load_elements import *
import pyperclip

def action_add_user(emp, _name, _username, _email, _mobile, _password, _type):
    name = _name
    username = _username
    email = _email
    mobile = _mobile
    password = _password
    confirm_password = _password
    user_type = _type

    #choose type
    types = [element_user_type_branch_employee, element_user_type_bank_employee, element_user_type_system_admin]
    user_type = types[_type]
   
    #
    def func_(emp):
        btn_list = emp.locate_all(element_dashboard_btns)

        if(btn_list):
            emp.click(btn_list[2], _tooltip="click on user management button")
        else:
            raise Exception("could not detect btns")
    emp.promise(_func=func_)
    emp.click(element_user_add, "click user add btn")
    emp.click(user_type, "choose user type")
    emp.click(element_user_add_name_input, "click username input")
    name = pyperclip.copy(name)
    emp.keyboard_hotkey("ctrl", "v")
    emp.input_into(username, element_user_add_username_input, "input username")
    emp.input_into(email, element_user_add_email_input, "input user email")
    emp.mouse_scroll_down() #so that the rest of the input fields are visible
    emp.input_into(mobile, element_user_add_mobile_input, "input user mobile")
    emp.input_into(password, element_user_add_password_input, "input user password")
    emp.input_into(confirm_password, element_user_add_password_confirm_input, "confirm user password")
    emp.mouse_scroll_down() #so that the submit button is visible
    emp.click(element_user_add_add, "click submit btn")
    def func_(emp):
        elm = emp.locate(element_user_add_success_message, _confidence=0.9)
        if(elm):
            print("user added successfully")
        else:
            print("failed to add user")
    emp.promise(_func=func_, _tooltip="check for success message")
    emp.click(element_user_add_success, "click ok btn")