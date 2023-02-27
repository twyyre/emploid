from emploid import Emploid
from api import API
from time import sleep
from load_elements import *

action_name = "action_login"

emp = Emploid()
emp.set_failsafe(False)
emp.set_delay(0.5)
show = emp.show

user_name = "shewa"
user_password = "11111111"
not_logged_in = 0

#--------------------------------
def func_(emp):
    show("importing image...")

    show("locating element")
    elm = emp.locate(element_jumhuriya_logo, _confidence=0.6)

    if(elm):
        show("detected")
    else:
        show("could not detect element")
        # raise Exception

    return elm
emp.promise(_func=func_, _tooltip="locate logo")

#--------------------------------
def func_(emp):
    show("importing image...")

    show("locating element")
    elm = emp.locate(element_username_input, _confidence=0.6)

    if(elm):
        show("detected")
        emp.click(elm)
        emp.input_into(user_name)
    else:
        show("could not detect element")
        global not_logged_in
        not_logged_in += 1

    return elm
emp.promise(_func=func_, _tooltip="input user password", _tries=3)

#--------------------------------
def func_(emp):
    show("importing image...")
    
    show("locating element")
    elm = emp.locate(element_password_input, _confidence=0.6)

    if(elm):
        show("detected")
        emp.click(elm)
        emp.input_into(user_password)
    else:
        show("could not detect element")
        global not_logged_in
        not_logged_in += 1


    return elm
emp.promise(_func=func_, _tooltip="input password", _tries=3)

#--------------------------------
def func_(emp):
    show("importing image...")

    show("locating element")
    elm = emp.locate(element_signin_btn, _confidence=0.6)

    if(elm):
        show("detected")
        emp.click(elm)
    else:
        show("could not detect element")
        raise Exception

    return elm
emp.promise(_func=func_, _tooltip="click signin btn")

# if(not_logged_in==2):
#     import action_logout


