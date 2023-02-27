from emploid import Emploid
from api import API
from time import sleep
from load_elements import *
import pyperclip

action_name = "action_search_user"

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
username = "ayoub"
email = "itameioss@gmail.com"#email.address
mobile = "944860551"
password = "99889988"
confirm_password = "99889988"
# user_type = element_user_type_branch_employee
# user_type = element_user_type_bank_employee
user_type = element_user_type_system_admin

#
def func_(emp):
    sleep(2)
    user_list = emp.locate_all(element_user_edit_btn)
    if(user_list):
        print("user detected")
        emp.click(user_list[0])
    else:
        print("could not detect user rows")
emp.promise(_func=func_, _tooltip="check for rows")

#
def func_(emp):
    #check for types of user
    elm = emp.locate(user_type, _confidence=0.9)
    emp.click(elm)
emp.promise(_func=func_, _tooltip="click on edit")

#
def func_(emp):
    #check for types of user
    elm = emp.locate(user_type, _confidence=0.9)
    emp.click(elm)
emp.promise(_func=func_, _tooltip="choose user type")

#
def func_(emp):
    elm = emp.locate(element_user_edit_name_input, _confidence=0.9)
    global name
    import pyperclip
    name = pyperclip.copy(name)
    # emp.input_into(name)
    emp.moveto(elm)
    emp.mouse_move_relative(_xoffset=0, _yoffset=50, _seconds=0)  
    emp.mouse_move_relative(_xoffset=-50, _yoffset=0, _seconds=0)  
    emp.press() #name
    emp.keyboard_hotkey("ctrl", "a")
    emp.keyboard_hotkey("ctrl", "v")
emp.promise(_func=func_, _tooltip="input user name")

#
def func_(emp):
    elm = emp.locate(element_user_edit_username_input, _confidence=0.9)
    global username
    import pyperclip
    username = pyperclip.copy(username)
    emp.moveto(elm)
    emp.mouse_move_relative(_xoffset=0, _yoffset=50, _seconds=0)  
    emp.mouse_move_relative(_xoffset=-50, _yoffset=0, _seconds=0)  
    emp.press() #name
    emp.keyboard_hotkey("ctrl", "a")
    emp.keyboard_hotkey("ctrl", "v")
emp.promise(_func=func_, _tooltip="input username")

#
def func_(emp):
    elm = emp.locate(element_user_edit_email_input, _confidence=0.9)
    global email
    import pyperclip
    email = pyperclip.copy(email)
    emp.moveto(elm)
    emp.mouse_move_relative(_xoffset=0, _yoffset=50, _seconds=0)  
    emp.mouse_move_relative(_xoffset=-50, _yoffset=0, _seconds=0)  
    emp.press() #name
    emp.keyboard_hotkey("ctrl", "a")
    emp.keyboard_hotkey("ctrl", "v")
emp.promise(_func=func_, _tooltip="input user email")

emp.mouse_scroll_down()

#
def func_(emp):
    elm = emp.locate(element_user_edit_mobile_input, _confidence=0.9)
    global mobile
    import pyperclip
    mobile = pyperclip.copy(mobile)
    emp.moveto(elm)
    emp.mouse_move_relative(_xoffset=0, _yoffset=50, _seconds=0)  
    emp.mouse_move_relative(_xoffset=-50, _yoffset=0, _seconds=0)  
    emp.press() #name
    emp.keyboard_hotkey("ctrl", "a")
    emp.keyboard_hotkey("ctrl", "v")
emp.promise(_func=func_, _tooltip="input user mobile")

# #
# def func_(emp):
#     elm = emp.locate(element_user_add_password_input, _confidence=0.9)
#     emp.click(elm) #password
#     emp.input_into(password)
# emp.promise(_func=func_, _tooltip="input user password")

# #
# def func_(emp):
#     elm = emp.locate(element_user_add_password_confirm_input, _confidence=0.9)
#     emp.click(elm) #confirm password
#     emp.input_into(confirm_password)
# emp.promise(_func=func_, _tooltip="confirm user password")

# emp.mouse_scroll_down() #so that the submit button is visible

#
def func_(emp):
    elm = emp.locate(element_user_edit_btn_2, _confidence=0.9)
    emp.click(elm) #confirm password
emp.promise(_func=func_, _tooltip="click submit btn")

#
def func_(emp):
    elm = emp.locate(element_user_add_success_message, _confidence=0.9)
    if(elm):
        show("user added successfully")
    else:
        show("failed to add user")
emp.promise(_func=func_, _tooltip="check for success message")

#
def func_(emp):
    elm = emp.locate(element_user_add_success, _confidence=0.9)
    emp.click(elm) #confirm password
emp.promise(_func=func_, _tooltip="click ok btn")