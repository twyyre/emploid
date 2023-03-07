from emploid import Emploid
from api import API
from time import sleep
from load_elements import *
import pyperclip

def action_add_customer(emp, _account_number):
        
    account_number = _account_number#"09090909090909"

    def func_(emp):
        btn_list = emp.locate_all(element_dashboard_btns)
        emp.click(btn_list[1]) #customer management
    emp.promise(_func=func_, _tooltip="click on user management button 1")

    def func_(emp):
        btn_list = emp.locate_all(element_dashboard_btns)
        emp.click(btn_list[2]) #customer management
    emp.promise(_func=func_, _tooltip="click on user management button 2")

    def func_(emp):
        btn_list = emp.locate_all(element_dashboard_btns)
        emp.click(btn_list[1]) #customer management
    emp.promise(_func=func_, _tooltip="click on user management button 3")

    def func_(emp):
        elm = emp.locate(element_customer_branch_inpt)
        if(elm):
            emp.click(elm)
            elm = emp.locate(element_customer_branch_two_inpt_option)
            if(elm):
                emp.click(elm)
            else: 
                raise Exception
        else:
            raise Exception
    emp.promise(_func=func_, _tooltip="click on branch input", _tries=5, _delay=2)

    emp.input_into("5555555555555", element_customer_account_number_inpt, "click on account number input")

    emp.click(element_customer_next_btn, "click next")
    
    def func_(emp):
        elm = emp.locate(element_customer_error_account_number_is_not_valid)
        if(elm):
            emp.moveto(elm)
            print("error: account number not found")
        else:
            print("successful")
    emp.promise(_func=func_, _tooltip="click next")




