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

#generate email for email confirmation
# def func_(emp):
#     global email
#     email = emp.email_generate()
#     show(f"generated email: {email.address}")
# emp.promise(_func=func_, _tooltip="generate email for email confirmation")

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
    emp.click(btn_list[1]) #customer management
emp.promise(_func=func_, _tooltip="click on customer management")

#
def func_(emp):
    btn_list = emp.locate_all(element_dashboard_btns)
    emp.click(btn_list[1]) #manage customers
emp.promise(_func=func_, _tooltip="click on manage customer data")

#
def func_(emp):
    btn_list = emp.locate_all(element_dashboard_btns)
    emp.click(btn_list[0]) #customer management
emp.promise(_func=func_, _tooltip="click on manage customer data")



