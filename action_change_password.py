from emploid import Emploid
from api import API
from time import sleep
from load_elements import *

action_name = "action_change_password"

emp = Emploid()
emp.set_failsafe(False)
emp.set_delay(0.5)
show = emp.show

old_password = "09090909"
new_password = "99889988"
confirm_password = "99889988"

#--------------------------------
def func_(emp):
    show("importing image...")

    show("locating element")
    elm = emp.locate(element_change_password)

    if(elm):
        show("detected")
        emp.click(elm)

    else:
        show("could not detect element")
        raise Exception

    return elm
emp.promise(_func=func_, _tooltip="locate logo")

#--------------------------------
def func_(emp):
    show("importing image...")

    show("locating element")
    btn_list = emp.locate_all(element_change_password_input)

    if(btn_list):
        show("detected")
        emp.click(btn_list[0])
        emp.input_into(old_password)

        emp.click(btn_list[1])
        emp.input_into(new_password)

        emp.click(btn_list[2])
        emp.input_into(confirm_password)

        elm = emp.locate(element_change_password_confirm)
        emp.click(elm)

    else:
        show("could not detect element")
        raise Exception
    
    return elm
emp.promise(_func=func_, _tooltip="input user password")

#--------------------------------
def func_(emp):
    success = emp.locate(element_change_password_success)

    if(success):
        print("password updated successfully")
        emp.click(success)
    else:
        show("could not detect success indicator")
        raise Exception

emp.promise(_func=func_, _tooltip="check if successful")
