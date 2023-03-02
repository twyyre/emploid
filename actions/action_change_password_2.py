from load_elements import *

def action_change_password(emp):
    def func_(emp):
        #check for types of user
        elm = emp.locate(element_user_change_password_btn, _confidence=0.9)
        emp.moveto(elm)
        emp.press()
    emp.promise(_func=func_, _tooltip="click on change password icon")

    def func_(emp):
        elm = emp.locate(element_user_change_password_confirm_btn, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            raise Exception
    emp.promise(_func=func_, _tooltip="click yes btn")

    def func_(emp):
        elm = emp.locate(element_user_copy_new_password, _confidence=0.9)
        if(elm):
            emp.click(elm) #confirm password
        else:
            raise Exception
    emp.promise(_func=func_, _tooltip="click on copy password btn")