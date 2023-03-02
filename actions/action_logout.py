from emploid import Emploid
from api import API
from time import sleep
from load_elements import *

def action_logout(emp):
    # print("LOG OUT ACTION")
    def func_(emp):
            emp.click(element_logout)
            print("element LOCATED")
            sleep(0.2)
            elm = emp.locate(element_logout_yes)
            if(elm):
                  emp.click(elm)
            else:
                raise Exception("could not detect logout btn")
    emp.promise(_func=func_)