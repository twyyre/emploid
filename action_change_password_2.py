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
    #check for types of user
    elm = emp.locate(element_user_change_password_btn, _confidence=0.9)
    emp.moveto(elm)
    emp.press()
emp.promise(_func=func_, _tooltip="click on change password icon")

#
def func_(emp):
    elm = emp.locate(element_user_change_password_confirm_btn, _confidence=0.9)
    if(elm):
        emp.click(elm)
    else:
        raise Exception
emp.promise(_func=func_, _tooltip="click yes btn")

#
def func_(emp):
    elm = emp.locate(element_user_copy_new_password, _confidence=0.9)
    if(elm):
        emp.click(elm) #confirm password
    else:
        raise Exception
emp.promise(_func=func_, _tooltip="click on copy password btn")