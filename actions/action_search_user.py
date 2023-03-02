from emploid import Emploid
from api import API
from time import sleep
from load_elements import *
import pyperclip

def action_search_user(emp, _username):
    username = _username
    #
    def func_(emp):
        btn_list = emp.locate_all(element_dashboard_btns)
        emp.click(btn_list[2]) #user management
    emp.promise(_func=func_, _tooltip="click on user management button")

    emp.input_into(username, element_user_search_input, "click on search bar")
    emp.keyboard_hotkey("enter")

    #
    def func_(emp):
        user_list = emp.locate_all(element_user_edit_btn)
        if(user_list):
            print("users detected")
        else:
            print("could not detect user rows")
    emp.promise(_func=func_, _tooltip="check for rows")




