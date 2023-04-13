from emploid import Emploid
from api import API
from time import sleep
from load_elements import *
import pyperclip

def action_add_a3mal_customer(emp, 
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
    _account_number, 
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
    _contract_number_confirm
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

    emp.err_nationalIdAlreadyUsed = None
    emp.err_customerAlreadyExists = None
    emp.err_otpNotAvailable = None
    
    def func_(emp):
        btn_list = emp.locate_all(element_dashboard_btns)
        emp.click(btn_list[1]) #customer management
    emp.promise(_func=func_, _tooltip="click on customer management button 1")

    def func_(emp):
        btn_list = emp.locate_all(element_dashboard_btns)
        emp.click(btn_list[2]) #customer management
    emp.promise(_func=func_, _tooltip="click on customer management button 2")

    def func_(emp):
        btn_list = emp.locate_all(element_dashboard_btns)
        emp.click(btn_list[0]) #customer management
    emp.promise(_func=func_, _tooltip="click on customer management button 3")
    
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

    def func_(emp):

        detected = emp.locate(element_error_nationalIdAlreadyUsed)
        if(detected):
            print("nationaIdAlreadyUsed")
            emp.err_nationalIdAlreadyUsed
            emp.err_nationalIdAlreadyUsed = True

        else:
            raise Exception
    emp.promise(_func=func_, _tooltip="check for nationalIdAlreadyUsed", _tries=3, _delay=1)
    
    if(not emp.err_nationalIdAlreadyUsed):
        # emp.input_into(company_name, element_customer_a3mal_company_name_inpt, "click company name input")
        emp.dbclick(element_customer_a3mal_company_name_inpt, "click company name input")
        
        pyperclip.copy(company_name)
        emp.keyboard_hotkey("ctrl", "v")
            
        emp.input_into(commerical_record, element_customer_a3mal_commercial_record_inpt, "click commerical record")

        emp.input_into(license_number, element_customer_a3mal_license_number_inpt, "click license number")
        
        emp.click(element_customer_a3mal_license_date_inpt, "click license date")
        
        emp.click(element_customer_a3mal_license_date_entry_btn)
                
        emp.click(element_customer_a3mal_license_date_entry_inpt, "click on manual entry btn")

        emp.keyboard_hotkey("crtl", "a") #I probably should use an alternative for keyboard hotkeys
        emp.keyboard_press("backspace")

        for char in license_date:
            emp.input_into(char)
        
        emp.click(element_customer_a3mal_hasanan)
        
        emp.click(element_customer_a3mal_account_type_inpt)
        emp.click(acc_type)
        
        emp.click(element_customer_a3mal_branch_inpt, "click branch inpt")
        emp.click(branch, "click branch option")

        emp.input_into(branch_id, element_customer_a3mal_branch_id_inpt, "click branch id input")

        emp.click(element_customer_a3mal_account_desc_inpt, "click account description input")
        
        pyperclip.copy(account_desc)
        emp.keyboard_hotkey("ctrl", "v")
        
        emp.input_into(account_number, element_customer_a3mal_account_number_inpt, "input account number")

        sleep(0.4)

        def func_(emp):
            detected = emp.locate(element_error_customerAlreadyExists)
            if(detected):
                print("emp.err_customerAlreadyExists")
                emp.err_customerAlreadyExists
                emp.err_customerAlreadyExists = True
            else:
                raise Exception
        emp.promise(_func=func_, _tooltip="check for emp.err_customerAlreadyExists", _tries=3, _delay=1)
        
        if(not emp.err_customerAlreadyExists):
            sleep(1)

            emp.mouse_scroll_down() #so that the add button is visible

            emp.click(element_customer_a3mal_add_btn, "click add btn")
            
            emp.click(element_customer_a3mal_next_btn2, "click next btn")

            emp.mouse_scroll_up() 

            emp.input_into(otp_sn, element_customer_a3mal_otp_sn_inpt, "input sequence number")

            sleep(0.4)

            emp.click(element_customer_a3mal_add_btn, "click add btn")

            def func_(emp):
                detected = emp.locate(element_error_otpNotAvailable)
                if(detected):
                    print("emp.err_otpNotAvailable")
                    emp.err_otpNotAvailable = True
                else:
                    raise Exception
            emp.promise(_func=func_, _tooltip="check for emp.err_otpNotAvailable", _tries=3, _delay=1)

            sleep(0.4)

            if(not emp.err_otpNotAvailable):

                emp.click(element_customer_a3mal_next_btn2, "click next btn")

                emp.click(element_customer_a3mal_customer_name_inpt, "insert customer name") 
                pyperclip.copy(customer_name)
                emp.keyboard_hotkey("ctrl", "v")
                emp.input_into(firstname, element_customer_a3mal_customer_firstname_inpt, "insert customer firstname") 
                emp.input_into(middlename, element_customer_a3mal_customer_middlename_inpt, "insert customer middlename") 
                emp.input_into(lastname, element_customer_a3mal_customer_lastname_inpt, "insert customer lastname") 
                emp.click(element_customer_a3mal_customer_gender_inpt, "click gender input") 
                types = [element_customer_a3mal_customer_gender_male, element_customer_a3mal_customer_gender_female]
                gender_type = types[_gender_type]
                emp.click(gender_type, "choose gender type") 
                emp.click(element_customer_a3mal_customer_mothername_inpt, "click mother name inpt")
                pyperclip.copy(mothername)
                emp.keyboard_hotkey("ctrl", "v") 
                emp.click(element_customer_a3mal_customer_birthplace_inpt, "click on birthplace input") 
                pyperclip.copy(birthplace)
                emp.keyboard_hotkey("ctrl", "v") 
                #
                emp.click(element_customer_a3mal_customer_birthdate_inpt, "click customer birthdate input") 
                
                emp.click(element_customer_a3mal_license_date_entry_btn, "click manual entry btn")
                        
                #
                emp.click(element_customer_a3mal_license_date_entry_inpt, "click on manual entry btn")
                emp.click(element_customer_a3mal_license_date_entry_btn)
                        
                emp.click(element_customer_a3mal_license_date_entry_inpt, "click on manual entry btn")

                emp.keyboard_hotkey("crtl", "a") #I probably should use an alternative for keyboard hotkeys
                emp.keyboard_press("backspace")

                for char in license_date:
                    emp.input_into(char)
                
                emp.click(element_customer_a3mal_hasanan)

                emp.keyboard_hotkey("crtl", "a") #I probably should use an alternative for keyboard hotkeys
                emp.keyboard_press("backspace")

                for char in license_date:
                    emp.input_into(char)
                
                emp.click(element_customer_a3mal_hasanan)
                #
                emp.click(element_customer_a3mal_customer_status_inpt) 
                types = [element_customer_a3mal_customer_status_single, element_customer_a3mal_customer_status_married, element_customer_a3mal_customer_status_divorced, element_customer_a3mal_customer_status_widowed]
                customer_status = types[customer_status]
                emp.click(customer_status) 
                emp.input_into(passport_number, element_customer_a3mal_customer_passport_number_inpt) 
                emp.click(element_customer_a3mal_customer_passport_publish_location_inpt, "click publish location input") 
                pyperclip.copy(publish_location)
                emp.keyboard_hotkey("ctrl", "v") 
                #
                emp.click(element_customer_a3mal_customer_passport_publish_date_inpt) 
                emp.click(element_customer_a3mal_license_date_entry_inpt, "click on manual entry btn")

                emp.keyboard_hotkey("crtl", "a") #I probably should use an alternative for keyboard hotkeys
                emp.keyboard_press("backspace")

                for char in license_date:
                    emp.input_into(char)
                
                emp.click(element_customer_a3mal_hasanan)

                emp.keyboard_hotkey("crtl", "a") #I probably should use an alternative for keyboard hotkeys
                emp.keyboard_press("backspace")

                for char in license_date:
                    emp.input_into(char)
                
                emp.click(element_customer_a3mal_hasanan)
                #
                emp.mouse_scroll_down() 
                #
                emp.click(element_customer_a3mal_customer_passport_expiration_date_inpt) 
                emp.click(element_customer_a3mal_license_date_entry_inpt, "click on manual entry btn")

                emp.keyboard_hotkey("crtl", "a") #I probably should use an alternative for keyboard hotkeys
                emp.keyboard_press("backspace")

                for char in license_date:
                    emp.input_into(char)
                
                emp.click(element_customer_a3mal_hasanan)

                emp.keyboard_hotkey("crtl", "a") #I probably should use an alternative for keyboard hotkeys
                emp.keyboard_press("backspace")

                for char in license_date:
                    emp.input_into(char)
                
                emp.click(element_customer_a3mal_hasanan)
                emp.mouse_move_relative(_xoffset=-20, _yoffset=-20, _seconds=0)
                #
                emp.input_into(passport_id, element_customer_a3mal_customer_passport_id_inpt) 
                emp.click(element_customer_a3mal_customer_familyhead_inpt) 
                types = [element_customer_a3mal_customer_familyhead_yes_option, element_customer_a3mal_customer_familyhead_no_option]
                familyhead_stat = types[familyhead_stat]
                emp.click(familyhead_stat) 

                emp.input_into(family_members_number, element_customer_a3mal_customer_family_members_number_inpt)

                emp.mouse_scroll_down() 

                emp.click(element_customer_a3mal_next_btn)

                emp.mouse_scroll_up() 
                emp.mouse_scroll_up() 

                emp.click(element_customer_branch_inpt)
                emp.click(branch)

                emp.input_into(email, element_customer_a3mal_customer_email_inpt)

                emp.click(element_customer_a3mal_customer_city_inpt)
                pyperclip.copy(city)
                emp.keyboard_hotkey("ctrl", "v") 

                emp.click(element_customer_a3mal_customer_area_inpt)
                pyperclip.copy(area)
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

                emp.click(element_customer_a3mal_customer_add_btn_2)

                success = emp.detect(element_customer_a3mal_customer_add_success)

                sleep(0.5)

                if(success):
                    emp.click(element_customer_a3mal_customer_ok_btn)
                    print("successfully added a3mal customer")
                    exit()
                else:
                    raise Exception("adding a3mal customer failed")











