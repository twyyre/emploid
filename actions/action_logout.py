from emploid import Emploid
from api import API
from time import sleep
from load_elements import *

def action_logout(emp):
    # print("LOG OUT ACTION")
    def func_(emp):
        clicked = emp.click(element_logout, "click logout btn", _tries=4)
        sleep(0.2)
        if(clicked):
            clicked = emp.click(element_logout_yes, "confirm logout")
            if(clicked):
                return True
            else:
                raise Exception("could not detect confirm logout btn")
        else:
            return False
    emp.promise(_func=func_)