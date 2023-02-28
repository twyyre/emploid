from emploid import Emploid
from api import API
from time import sleep
from load_elements import *
import pyperclip

action_name = "action_add_user"

emp = Emploid()
emp.set_failsafe(False)
emp.set_delay(0.5)
show = emp.show

name = "واحد أحول"
username = "wahedahwal04"
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
    elm = emp.locate(element_user_add)
    emp.click(elm)
emp.promise(_func=func_, _tooltip="click user add btn")

#
def func_(emp):
    #check for types of user
    elm = emp.locate(user_type, _confidence=0.9)
    emp.click(elm)
emp.promise(_func=func_, _tooltip="choose user type")

#
def func_(emp):
    elm = emp.locate(element_user_add_name_input, _confidence=0.9)
    emp.click(elm) #name
    global name
    name = pyperclip.copy(name)
    # emp.input_into(name)
    emp.keyboard_hotkey("ctrl", "v")
emp.promise(_func=func_, _tooltip="input user name")

#
def func_(emp):
    elm = emp.locate(element_user_add_username_input, _confidence=0.9)
    emp.click(elm) #username
    emp.input_into(username)
emp.promise(_func=func_, _tooltip="input username")

#
def func_(emp):
    elm = emp.locate(element_user_add_email_input, _confidence=0.9)
    emp.click(elm) #email
    emp.input_into(email)
emp.promise(_func=func_, _tooltip="input user email")

emp.mouse_scroll_down()

#
def func_(emp):
    elm = emp.locate(element_user_add_mobile_input, _confidence=0.9)
    emp.click(elm) #mobile
    emp.input_into(mobile)
emp.promise(_func=func_, _tooltip="input user mobile")

#
def func_(emp):
    elm = emp.locate(element_user_add_password_input, _confidence=0.9)
    emp.click(elm) #password
    emp.input_into(password)
emp.promise(_func=func_, _tooltip="input user password")

#
def func_(emp):
    elm = emp.locate(element_user_add_password_confirm_input, _confidence=0.9)
    emp.click(elm) #confirm password
    emp.input_into(confirm_password)
emp.promise(_func=func_, _tooltip="confirm user password")

emp.mouse_scroll_down() #so that the submit button is visible

#
def func_(emp):
    elm = emp.locate(element_user_add_add, _confidence=0.9)
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



