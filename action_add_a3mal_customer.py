from emploid import Emploid
from api import API
from time import sleep
from load_elements import *
import pyperclip

action_name = "action_add_user"

emp = Emploid()
emp.set_failsafe(False)
emp.set_delay(0.5)
show = emp.show

name = "واحد أحول"
username = "wahedahwal04"

nationality = 0 #citizen
national_id = "1190910953021"

company_name = "company name"
commerical_record = "11119519515"
license_number = "11119519515"
license_date = "٢٠٢٣"
account_type = "account type"
branch = "branch"
branch_id = "branch ID"
account_desc = "account description"

user_type = element_user_type_system_admin

#
def func_(emp):
    btn_list = emp.locate_all(element_dashboard_btns)
    emp.click(btn_list[1]) #customer management
emp.promise(_func=func_, _tooltip="click on user management button 1")

#
def func_(emp):
    btn_list = emp.locate_all(element_dashboard_btns)
    emp.click(btn_list[2]) #customer management
emp.promise(_func=func_, _tooltip="click on user management button 2")

#
def func_(emp):
    btn_list = emp.locate_all(element_dashboard_btns)
    emp.click(btn_list[0]) #customer management
emp.promise(_func=func_, _tooltip="click on user management button 3")

#
def func_(emp):
    elm = emp.locate(element_customer_a3mal_nationality_inpt)
    if(elm):
        emp.click(elm)
        elm = emp.locate(element_customer_a3mal_citizen_inpt_option)
        if(elm):
            emp.click(elm)
            
    else:
        raise Exception
    
    #
    def func_(emp):
        global national_id
        elm = emp.locate(element_customer_a3mal_national_id_inpt)
        if(elm):
            emp.click(elm)
            emp.input_into(national_id)
        else:
            raise Exception
    emp.promise(_func=func_, _tooltip="click on national ID input")
emp.promise(_func=func_, _tooltip="click on nationality input")

#
def func_(emp):
    elm = emp.locate(element_customer_a3mal_next_btn)
    if(elm):
        emp.click(elm)
    else:
        raise Exception
emp.promise(_func=func_, _tooltip="click next")

#
def func_(emp):
    elm = emp.locate(element_customer_a3mal_company_name_inpt)
    if(elm):
        emp.click(elm)
        emp.input_into(company_name)
    else:
        raise Exception
emp.promise(_func=func_, _tooltip="click company name input")

#
def func_(emp):
    elm = emp.locate(element_customer_a3mal_commercial_record_inpt)
    if(elm):
        emp.click(elm)
        emp.input_into(commerical_record)

    else:
        raise Exception
emp.promise(_func=func_, _tooltip="click commerical record")

#
def func_(emp):
    elm = emp.locate(element_customer_a3mal_license_number_inpt)
    if(elm):
        emp.click(elm)
        emp.input_into(license_number)

    else:
        raise Exception
emp.promise(_func=func_, _tooltip="click license number")

#
def func_(emp):
    elm = emp.locate(element_customer_a3mal_license_date_inpt)
    if(elm):
        emp.click(elm)
        
        elm = emp.locate(element_customer_a3mal_license_date_entry_btn)

        if(elm):
            emp.click(elm)
                    
            elm = emp.locate(element_customer_a3mal_license_date_entry_inpt)

            if(emp):
                # emp.click(elm)
                # emp.click(elm)
                emp.keyboard_press("backspace")


                #inputing into date input does not work
                # license_date = "2023/12/12"
                # print("string:", license_date)
                # emp.pa.hotkey('CRTL', 'a')

                for char in license_date:
                    emp.input_into(char)
                
                # for char in license_date:
                #     pyperclip.paste(str(char))

                elm = emp.locate(element_customer_a3mal_hasanan)

                if(emp):
                    emp.click(elm)
                else:
                    raise Exception
            else:
                raise Exception
                
    else:
        raise Exception
emp.promise(_func=func_, _tooltip="click license date")

#
def func_(emp):
    elm = emp.locate(element_customer_a3mal_account_type_inpt)
    if(elm):
        emp.click(elm)
        # 

    else:
        raise Exception
emp.promise(_func=func_, _tooltip="click account type")

#
def func_(emp):
    elm = emp.locate(element_customer_a3mal_branch_inpt)
    if(elm):
        emp.click(elm)
        emp.input_into(branch)

    else:
        raise Exception
emp.promise(_func=func_, _tooltip="click branch")

#
def func_(emp):
    elm = emp.locate(element_customer_a3mal_branch_id_inpt)
    if(elm):
        emp.click(elm)
        emp.input_into(branch_id)

    else:
        raise Exception
emp.promise(_func=func_, _tooltip="click branch id input")

#
def func_(emp):
    elm = emp.locate(element_customer_a3mal_account_desc_inpt)
    if(elm):
        emp.click(elm)
        emp.input_into(account_desc)

    else:
        raise Exception
emp.promise(_func=func_, _tooltip="click account description input")

emp.mouse_scroll_down() #so that the add button is visible

#
def func_(emp):
    elm = emp.locate(element_customer_a3mal_add_btn)
    if(elm):
        emp.click(elm)
    else:
        raise Exception
emp.promise(_func=func_, _tooltip="click add btn")

#
def func_(emp):
    elm = emp.locate(element_customer_a3mal_next_btn2)
    if(elm):
        emp.click(elm)
    else:
        raise Exception
emp.promise(_func=func_, _tooltip="click next btn")



