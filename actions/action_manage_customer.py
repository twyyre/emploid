from emploid import Emploid
from api import API
from time import sleep
from load_elements import *
import pyperclip

def action_manage_customer(emp, ):
    def func_(emp):
        btn_list = emp.locate_all(element_dashboard_btns)
        emp.click(btn_list[1]) #customer management
    emp.promise(_func=func_, _tooltip="click on customer management")

    def func_(emp):
        btn_list = emp.locate_all(element_dashboard_btns)
        emp.click(btn_list[1]) #manage customers
    emp.promise(_func=func_, _tooltip="click on manage customer data")

    def func_(emp):
        btn_list = emp.locate_all(element_dashboard_btns)
        emp.click(btn_list[1]) #customer management
    emp.promise(_func=func_, _tooltip="click on manage customer data")

    emp.input_into("asdasd", element_customer_a3mal_manage_national_id_inpt, "input national id")
    emp.input_into("asdasd", element_customer_a3mal_manage_mobile_inpt, "input mobile")
    emp.click(element_customer_a3mal_manage_search_btn)



