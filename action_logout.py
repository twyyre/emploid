from emploid import Emploid
from api import API
from time import sleep
from load_elements import *

action_name = "action_logout"

emp = Emploid()
emp.set_failsafe(False)
emp.set_delay(0.5)
show = emp.show

sleep(1)

#--------------------------------
def func_(emp):
    show("importing image...")

    show("locating element")
    elm = emp.locate(element_logout, _confidence=0.9)

    if(elm):
        show("detected")
        emp.click(elm)
    else:
        show("could not detect element")
        raise Exception

    return elm
emp.promise(_func=func_, _tooltip="click logout btn")

#--------------------------------
def func_(emp):
    show("importing image...")

    show("locating element")
    elm = emp.locate(element_logout_yes, _confidence=0.9)

    if(elm):
        show("detected")
        emp.click(elm)
    else:
        show("could not detect element")
        raise Exception

    return elm
emp.promise(_func=func_, _tooltip="confirm logout")