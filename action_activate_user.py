from emploid import Emploid
from api import API
from time import sleep
from load_elements import *
import pyperclip

action_name = "action_activate_user"

emp = Emploid()
emp.set_failsafe(False)
emp.set_delay(0.5)
show = emp.show

name = "واحد أحول"
username = "ayoub"
email = "itameioss@gmail.com"
mobile = "944860551"
password = "99889988"
confirm_password = "99889988"

x = 0
y = 0
xx = 0
yy = 0

user_type = element_user_type_system_admin

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
        emp.mouse_move_relative(_xoffset=0, _yoffset=10, _seconds=0)  
        emp.mouse_move_relative(_xoffset=-100, _yoffset=0, _seconds=0)

        global x, y, xx, yy
        x, y = emp.get_mouse_pos()
        xx = 200
        yy = 100
emp.promise(_func=func_, _tooltip="move to activision state")

#
def func_(emp):

    print("------------------------checkpoint02")
    elm = emp.locate_in_region(element_user_activate_btn, _confidence=0.9, _x=x, _y=y, _xx=xx, _yy=yy)
    if(elm):
        print("DETECTED")
        emp.moveto(elm)
        # emp.click(elm)
    else:
        print("NOT DETECTED")
emp.promise(_func=func_, _tooltip="find element in region")

print(x, y, xx, yy)

exit()
# #
# def func_(emp):
#     #check for types of user
#     elm = emp.locate(element_user_activate_btn, _confidence=0.9)
#     emp.click(elm)
# emp.promise(_func=func_, _tooltip="click on activate")

# #
# def func_(emp):
#     #check for types of user
#     elm = emp.locate(element_user_activate_accept, _confidence=0.9)
#     emp.click(elm)
# emp.promise(_func=func_, _tooltip="click accept")