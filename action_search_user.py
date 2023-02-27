from emploid import Emploid
from api import API
from time import sleep
from load_elements import *
import pyperclip

action_name = "action_search_user"

emp = Emploid()
emp.set_failsafe(False)
emp.set_delay(0.5)
show = emp.show

#generate email for email confirmation
# def func_(emp):
#     global email
#     email = emp.email_generate()
#     show(f"generated email: {email.address}")
# emp.promise(_func=func_, _tooltip="generate email for email confirmation")

name = "واحد أحول"
username = "ayoub"
email = "itameioss@gmail.com"#email.address
mobile = "944860551"
password = "99889988"
confirm_password = "99889988"
# user_type = element_user_type_branch_employee
# user_type = element_user_type_bank_employee
user_type = element_user_type_system_admin

#
def func_(emp):
    btn_list = emp.locate_all(element_dashboard_btns)
    emp.click(btn_list[2]) #user management
emp.promise(_func=func_, _tooltip="click on user management button")

#
def func_(emp):

    elm = emp.locate(element_user_search_input, _confidence=0.9)

    if(elm):
        show("search bar found")
        emp.click(elm)

    else:
        show("failed to find search bar")
emp.promise(_func=func_, _tooltip="click on search bar")

#
def func_(emp):
    emp.input_into(username)
    emp.keyboard_hotkey("enter")
emp.promise(_func=func_, _tooltip="input user name into search bar")

#
def func_(emp):
    user_list = emp.locate_all(element_user_edit_btn)
    if(user_list):
        print("users detected")
    else:
        print("could not detect user rows")
emp.promise(_func=func_, _tooltip="check for rows")




