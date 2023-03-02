from emploid import Emploid
from api import API
from time import sleep
from load_elements import *
import pyperclip

def action_add_a3mal_customer(emp, _nationality, _national_id, _company_name, _commerical_record, _license_number, _license_date, _branch, _branch_id, _account_desc):
    nationality = _nationality
    national_id = _national_id
    company_name = _company_name#"company name"
    commerical_record = _commerical_record#"11119519515"
    license_number = _license_number#"11119519515"
    license_date = _license_date#"٢٠٢٣"
    # account_type = "account type"
    branch = _branch#"branch"
    branch_id = _branch_id#"branch ID"
    account_desc = _account_desc#"account description"

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
        emp.click(btn_list[0]) #customer management
    emp.promise(_func=func_, _tooltip="click on user management button 3")
    
    def func_(emp):
        elm = emp.locate(element_customer_a3mal_nationality_inpt)
        if(elm):
            emp.click(elm)
            elm = emp.locate(element_customer_a3mal_citizen_inpt_option)
            if(elm):
                emp.click(elm)
        else:
            raise Exception
        emp.input_into(national_id, element_customer_a3mal_national_id_inpt)
    emp.promise(_func=func_, _tooltip="click on nationality input")
    
    def func_(emp):
        elm = emp.locate(element_customer_a3mal_next_btn)
        if(elm):
            emp.click(elm)
        else:
            raise Exception
    emp.promise(_func=func_, _tooltip="click next")

    emp.input_into(company_name, element_customer_a3mal_company_name_inpt, "click company name input")
        
    emp.input_into(commerical_record, element_customer_a3mal_commercial_record_inpt, "click commerical record")

    emp.input_into(license_number, element_customer_a3mal_license_number_inpt, "click license number")
        
    emp.click(element_customer_a3mal_license_date_inpt, "click license date")
    
    emp.click(element_customer_a3mal_license_date_entry_btn)
            
    emp.click(element_customer_a3mal_license_date_entry_inpt)

    emp.keyboard_hotkey("crtl", "a") #I probably should use an alternative for keyboard hotkeys
    emp.keyboard_press("backspace")

    for char in license_date:
        emp.input_into(char)
    
    emp.click(element_customer_a3mal_hasanan)
      
    emp.click(element_customer_a3mal_account_type_inpt)
    
    emp.input_into(branch, element_customer_a3mal_branch_inpt, "click branch")

    emp.input_into(branch_id, element_customer_a3mal_branch_id_inpt, "click branch id input")

    emp.input_into(account_desc, element_customer_a3mal_account_desc_inpt, "click account description input")

    emp.mouse_scroll_down() #so that the add button is visible

    emp.click(element_customer_a3mal_add_btn, "click add btn")
    
    emp.click(element_customer_a3mal_next_btn2, "click next btn")