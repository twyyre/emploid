from emploid import Emploid
from api import API
from time import sleep
from load_elements import *
import pyperclip

def action_add_customer(emp, 
    _account_number,
    _nationality, 
    _national_id, 
    _company_name, 
    _commerical_record, 
    _license_number, 
    _license_date, 
    _branch, 
    _branch_id, 
    _account_desc, 
    _type, 
    _otp_sn, 
    _gender_type, 
    _customer_name, 
    _firstname, 
    _middlename, 
    _lastname, 
    _mothername, 
    _birthplace, 
    _customer_status, 
    _passport_number, 
    _publish_location, 
    _familyhead_stat, 
    _passport_id, 
    _family_members_number,
    _email,
    _city,
    _area,
    _mobile,
    _mobile_confirm,
    _contract_number,
    _contract_number_confirm,
    _address
    ):
        
    nationality = _nationality
    national_id = _national_id
    company_name = _company_name#"company name"
    commerical_record = _commerical_record#"11119519515"
    license_number = _license_number#"11119519515"
    license_date = _license_date#"٢٠٢٣"
    # account_type = "account type"
    branches = [element_customer_branch_one_inpt_option, element_customer_branch_two_inpt_option, element_customer_branch_three_inpt_option]
    branch = branches[_branch]#"branch"
    branch_id = _branch_id#"branch ID"
    account_desc = _account_desc#"account description"
    types = [element_customer_a3mal_account_type_option_current, element_customer_a3mal_account_type_option_aggregate]
    acc_type = types[_type]
    account_number = _account_number
    otp_sn = _otp_sn
    customer_name = _customer_name
    firstname = _firstname
    middlename = _middlename
    lastname = _lastname
    mothername = _mothername
    birthplace = _birthplace
    customer_status = _customer_status
    passport_number = _passport_number
    publish_location = _publish_location
    familyhead_stat = _familyhead_stat
    passport_id = _passport_id
    family_members_number = _family_members_number
    email = _email
    city = _city
    area = _area
    mobile = _mobile
    mobile_confirm = _mobile_confirm
    contract_number = _contract_number
    contract_number_confirm = _contract_number_confirm
    address = _address

    err_customerAlreadyExists2 = None
    err_itemAlreadyExists = None

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

    emp.input_into(account_number, element_customer_account_number_inpt, "click on account number input")

    emp.click(element_customer_next_btn, "click next")

    def func_(emp):
        detected = emp.locate(element_error_customerAlreadyExists2)
        if(detected):
            print("customerAlreadyExists")
            global err_customerAlreadyExists2
            err_customerAlreadyExists2 = True
            exit()
        else:
            raise Exception

    emp.promise(_func=func_, _tooltip="check for customerAlreadyExists", _tries=3, _delay=1)
    
    def func_(emp):
        elm = emp.locate(element_customer_error_account_number_is_not_valid)
        if(elm):
            emp.moveto(elm)
            print("error: accountNumberIsNotValid")
        else:
            print("successful")
    emp.promise(_func=func_, _tooltip="check for accountNumberIsNotValid")

    detected = emp.detect(element_customer_customer_add_success1)
    if(detected):
        emp.click(element_customer_next_btn, "click next btn")
    else:
        pass

    emp.input_into(firstname, element_customer_a3mal_customer_firstname_inpt, "insert customer firstname") 
    emp.input_into(middlename, element_customer_a3mal_customer_middlename_inpt, "insert customer middlename") 
    emp.input_into(lastname, element_customer_lastname_inpt2, "insert customer lastname")

    emp.click(element_customer_gender_inpt2, "click gender input") 
    types = [element_customer_a3mal_customer_gender_male, element_customer_a3mal_customer_gender_female]
    gender_type = types[_gender_type]
    emp.click(gender_type, "choose gender type") 

    emp.click(element_customer_a3mal_customer_mothername_inpt, "click mother name inpt")
    pyperclip.copy(mothername)
    emp.keyboard_hotkey("ctrl", "v") 

    emp.click(element_customer_a3mal_customer_birthplace_inpt, "click on birthplace input") 
    pyperclip.copy(birthplace)
    emp.keyboard_hotkey("ctrl", "v") 

    emp.click(element_customer_a3mal_customer_birthdate_inpt, "click customer birthdate input")
    emp.click(element_customer_hasanan2)

    types = [element_customer_a3mal_citizen_inpt_option, element_customer_a3mal_non_citizen_inpt_option]
    nationality = types[nationality]
    emp.click(element_customer_nationality_inpt2, "click on nationality input")
    emp.click(nationality, "choose nationality option")

    emp.click(element_customer_status_inpt2) 
    types = [element_customer_a3mal_customer_status_single, element_customer_a3mal_customer_status_married, element_customer_a3mal_customer_status_divorced, element_customer_a3mal_customer_status_widowed]
    customer_status = types[customer_status]
    emp.click(customer_status) 

    emp.input_into(passport_number, element_customer_a3mal_customer_passport_number_inpt) 
    emp.click(element_customer_a3mal_customer_passport_publish_location_inpt, "click publish location input") 
    pyperclip.copy(publish_location)
    emp.keyboard_hotkey("ctrl", "v") 

    emp.click(element_customer_a3mal_customer_passport_publish_date_inpt) 
    emp.click(element_customer_hasanan2)

    emp.mouse_scroll_down() 

    emp.click(element_customer_a3mal_customer_passport_expiration_date_inpt) 
    emp.click(element_customer_hasanan2)

    emp.input_into(national_id, element_customer_national_id_inpt2)

    emp.input_into(contract_number, element_customer_contract_number_inpt2)

    emp.mouse_scroll_down() 

    emp.click(element_customer_familyhead_inpt2) 
    types = [element_customer_familyhead_yes_option2, element_customer_familyhead_no_option2]
    familyhead_stat = types[familyhead_stat]
    emp.click(familyhead_stat) 

    emp.input_into(family_members_number, element_customer_a3mal_customer_family_members_number_inpt)

    emp.mouse_scroll_down() 

    emp.click(element_customer_next_btn)

    emp.mouse_scroll_up() 
    emp.mouse_scroll_up() 
    emp.mouse_scroll_up() 
    emp.mouse_scroll_up() 
    emp.mouse_scroll_up() 

    emp.input_into(email, element_customer_a3mal_customer_email_inpt)

    emp.click(element_customer_a3mal_customer_city_inpt)
    pyperclip.copy(city)
    emp.keyboard_hotkey("ctrl", "v") 

    emp.click(element_customer_a3mal_customer_area_inpt)
    pyperclip.copy(area)
    emp.keyboard_hotkey("ctrl", "v") 

    emp.click(element_customer_address_inpt)
    pyperclip.copy(address)
    emp.keyboard_hotkey("ctrl", "v") 

    emp.input_into(mobile, element_customer_a3mal_customer_mobile_inpt)
    emp.input_into(mobile_confirm, element_customer_a3mal_customer_mobile_confirm_inpt)
    emp.click(element_customer_a3mal_customer_add_btn)

    sleep(0.5)

    emp.mouse_move(_y=0, _x=0, _seconds=0)

    emp.input_into(contract_number, element_customer_a3mal_customer_contract_number_inpt)

    emp.click(element_customer_a3mal_customer_next_btn_3)

    sleep(0.5)

    emp.input_into(contract_number_confirm, element_customer_a3mal_customer_contract_number_confirm_inpt)

    emp.click(element_customer_a3mal_customer_confirm_btn_3)

    def func_(self):
        success = emp.detect(element_error_itemAlreadyExists)
        if(success):
            emp.click(element_error_itemAlreadyExists)
            print("err_itemAlreadyExists")
            global err_customerAlreadyExists2
            err_customerAlreadyExists2 = None
            exit()
        else:
            raise Exception("err_itemAlreadyExists")
    emp.promise(_func=func_, _tooltip="check err_itemAlreadyExists", _tries=3, _delay=1)

    emp.click(element_customer_a3mal_customer_add_btn_2)
    
    def func_(self):
        success = emp.detect(element_customer_a3mal_customer_add_success)
        if(success):
            emp.click(element_customer_a3mal_customer_ok_btn)
            print("successfully added a3mal customer")
            exit()
        else:
            raise Exception("adding a3mal customer failed")
    emp.promise(_func=func_, _tooltip="check for success", _tries=3, _delay=1)
    









