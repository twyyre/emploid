from emploid import Emploid
from api import API
from time import sleep
from load_elements import *
import pyperclip

def action_activate(emp):

    x = 0
    y = 0
    xx = 0
    yy = 0

    user_type = element_user_type_system_admin

    def func_(emp):
        sleep(2)
        user_list = emp.locate_all(element_user_edit_btn)
        if(user_list):
            print("user detected")
            # emp.click(user_list[0])
        else:
            print("could not detect user rows")
    emp.promise(_func=func_, _tooltip="check for rows")

    def func_(emp):
        #check for types of user
        elm = emp.locate(element_user_activision_state, _confidence=0.9)
        if(elm):
            emp.moveto(elm)
            emp.mouse_move_relative(_xoffset=0, _yoffset=10, _seconds=0)  
            emp.mouse_move_relative(_xoffset=-100, _yoffset=0, _seconds=0)

            global x, y, xx, yy
            x, y = emp.get_mouse_pos()
            xx = 200
            yy = 100
    emp.promise(_func=func_, _tooltip="move to activision state")

    def func_(emp):
        print("------------------------checkpoint02")
        elm = emp.locate(element_user_activate_btn)
       
        try:
            elm = emp.locate_in_region(element_user_activate_btn, _confidence=0.9, _x=x, _y=y, _xx=xx, _yy=yy)
        except Exception as e:
            print("could not capture element in region")
            print(e)
            
        if(elm):
            print("DETECTED")
            emp.moveto(elm)
            emp.click(elm)
        else:
            print("NOT DETECTED")
    emp.promise(_func=func_, _tooltip="find element in region")

    # print("TEST SECTION")
    sleep(0.5)
    try:
        elm = emp.locate(element_user_activate_accept)
    except Exception as e:
        print("could not locate element")
    try:
        emp.click(elm, "click accept")
    except Exception as e:
        print("could not click element")
