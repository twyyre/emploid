from emploid import Emploid
from api import API
from time import sleep
from load_elements import *
import pyperclip

def action_deactivate(emp, _deactivision_note="deactivate note"):

    deactivision_note = _deactivision_note
    x = 0
    y = 0
    xx = 0
    yy = 0

    #
    def func_(emp):
        sleep(2)
        user_list = emp.locate_all(element_user_edit_btn)
        if(user_list):
            print("user detected")
            # emp.click(user_list[0])
        else:
            print("could not detect user rows")
    emp.promise(_func=func_, _tooltip="check for rows")

    #
    def func_(emp):
        #check for types of user
        elm = emp.locate(element_user_activision_state, _confidence=0.9)
        if(elm):
            emp.moveto(elm)
            emp.mouse_move_relative(_xoffset=0, _yoffset=20, _seconds=0)  
            emp.mouse_move_relative(_xoffset=-150, _yoffset=0, _seconds=0)

            global x, y, xx, yy
            x, y = emp.get_mouse_pos()
            xx = 200
            yy = 100
    emp.promise(_func=func_, _tooltip="move to activision state")
    exit()
    #
    def func_(emp):

        print("------------------------checkpoint02")
        elm = emp.locate_in_region(element_user_deactivate_btn, _confidence=0.9, _x=x, _y=y, _xx=xx, _yy=yy)
        if(elm):
            print("DETECTED")
            emp.moveto(elm)
            emp.click(elm)
            exit()
        else:
            print("NOT DETECTED")
            exit()
    emp.promise(_func=func_, _tooltip="find element in region")

    #
    def func_(emp):
        #check for types of user
        elm = emp.locate(element_user_activate_note_inpt, _confidence=0.9)
        emp.click(elm)
        emp.input_into(deactivision_note)
    emp.promise(_func=func_, _tooltip="input deactivision note")

    #
    def func_(emp):
        #check for types of user
        elm = emp.locate(element_user_activate_accept, _confidence=0.9)
        emp.click(elm)
    emp.promise(_func=func_, _tooltip="click accept")