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

nationality = 0 #citizen
national_id = "1190910953021"


user_type = element_user_type_system_admin

#
def func_(emp):
    btn_list = emp.locate_all(element_dashboard_btns)
    emp.click(btn_list[1]) #customer management
emp.promise(_func=func_, _tooltip="click on user management button 1")

#
def func_(emp):
    btn_list = emp.locate_all(element_dashboard_btns)
    emp.click(btn_list[2]) #customer management
emp.promise(_func=func_, _tooltip="click on user management button 2")

#
def func_(emp):
    btn_list = emp.locate_all(element_dashboard_btns)
    emp.click(btn_list[0]) #customer management
emp.promise(_func=func_, _tooltip="click on user management button 3")

#
def func_(emp):
    elm = emp.locate(element_customer_a3mal_nationality_inpt)
    if(elm):
        emp.click(elm)
        elm = emp.locate(element_customer_a3mal_citizen_inpt_option)
        if(elm):
            emp.moveto(elm)
            input()
    else:
        raise Exception
emp.promise(_func=func_, _tooltip="click on nationality input")

#
def func_(emp):
    elm = emp.locate(element_customer_a3mal_national_id_inpt)
    emp.click(elm) #customer management
emp.promise(_func=func_, _tooltip="click on national ID input")

#
def func_(emp):
    elm = emp.locate(element_customer_a3mal_next_btn)
    if(elm):
        emp.click(elm)
    else:
        raise Exception
emp.promise(_func=func_, _tooltip="click next")



