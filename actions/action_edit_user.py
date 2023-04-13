from emploid import Emploid
from api import API
from time import sleep
from load_elements import *
import pyperclip


def action_edit_user(emp, _name, _username,_email, _mobile, _password, _type):
    sleep(0.5)

    user_list = emp.locate_all(element_user_edit_btn)

    if(user_list):
        emp.click(user_list[0], _tooltip="click on edit btn")
    else:
        raise Exception("could not detect btns")
    
    #choose type
    types = [element_user_type_branch_employee, element_user_type_bank_employee, element_user_type_system_admin]
    user_type = types[_type]

    emp.click(user_type, "choose user type")


    def func_(emp):
        import pyperclip
        name = pyperclip.copy(_name)
        emp.moveto(element_user_edit_name_input)
        emp.mouse_move_relative(_xoffset=0, _yoffset=50, _seconds=0)  
        emp.mouse_move_relative(_xoffset=-50, _yoffset=0, _seconds=0)  
        emp.press() #name
        emp.keyboard_hotkey("ctrl", "a")
        emp.keyboard_hotkey("ctrl", "v")
    emp.promise(_func=func_, _tooltip="input user name")

    #
    def func_(emp):
        elm = emp.locate(element_user_edit_username_input, _confidence=0.9)
        import pyperclip
        username = pyperclip.copy(_username)
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
        import pyperclip
        email = pyperclip.copy(_email)
        emp.moveto(elm)
        emp.mouse_move_relative(_xoffset=0, _yoffset=50, _seconds=0)  
        emp.mouse_move_relative(_xoffset=-50, _yoffset=0, _seconds=0)  
        emp.press() #name
        emp.keyboard_hotkey("ctrl", "a")
        emp.keyboard_hotkey("ctrl", "v")
    emp.promise(_func=func_, _tooltip="input user email")

    emp.mouse_scroll_down()
    emp.mouse_scroll_down()

    def func_(emp):
        elm = emp.locate(element_user_edit_mobile_input, _confidence=0.9)
        import pyperclip
        mobile = pyperclip.copy(_mobile)
        emp.moveto(elm)
        emp.mouse_move_relative(_xoffset=0, _yoffset=50, _seconds=0)  
        emp.mouse_move_relative(_xoffset=-50, _yoffset=0, _seconds=0)  
        emp.press() #name
        emp.keyboard_hotkey("ctrl", "a")
        emp.keyboard_hotkey("ctrl", "v")
    emp.promise(_func=func_, _tooltip="input user mobile")

    confidence = 0.9
    emp.click(element_user_edit_permission_inpt)

    #Permissions

    
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_1_insertAfrad, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_2_insertA3mal, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_3_activateBankAfrad, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_4_activateBankA3mal, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_5_confirmChangesAfrad, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_6_manageA3malActivsion, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_7_activateServiceAfrad, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_8_upgradeAfrad, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_9_afradEventTracking, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_10_Review, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_11_updateActiveA3mal, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_12_updateCustomerA3mal, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_13_changeActivisionAfrad, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_14_activateServicesA3mal, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_15_upgradeA3mal, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_16_reporting, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_17_payment, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_18_paymentReporting, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_19_a3malEventTracking, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_20_afradPinReminder, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_21_a3malPinReminder, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_22_afradSmsTracking, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_23_a3malSmsTracking, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_24_afradAppTracking, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_25_a3malAppTracking, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_26_viewCustomerManagement, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_27_viewA3malManagement, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_28_updateA3malAccounts, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_29_addA3malOtp, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_30_replaceA3malOtp, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_31_addA3malCompany, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_32_updateA3malCompany, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_33_a3malAddAccountToCompany, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_34_a3malUserChangeActivision, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_35_a3malUserUpdateAccounts, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_36_reviewPhone, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_37_showRejected, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_38_showRejected, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_39_checkBookManagement, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_40_problemTrackingAfrad, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_41_problemTrackingA3mal, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_42_registrationRequests, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_43_a3malUserResetId, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_44_activateA3malAccounts, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_45_insertMerchant, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_46_activateMerchant, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_47_issueSigninMethods, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)

    def func_(emp):
        elm = emp.locate(element_user_edit_permission_57_reIssueSigninMethods, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_48_reviewSigninMethods, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_49_reviewUpdateMerchantInformation, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)






    #----------------------------------------------------------------------------
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_50_updateMerchantInformation, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_51_remindMerchantId, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_52_remindMerchantPin, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_53_getMerchantInformation, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_54_activeDisActiveMerchant, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_55_updateBussinessInfo, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)
    
    def func_(emp):
        elm = emp.locate(element_user_edit_permission_56_reminderMerchantOnlineProviderId, _confidence=0.9)
        if(elm):
            emp.click(elm)
        else:
            emp.mouse_scroll_down()
            raise Exception
    emp.promise(_func=func_, _delay=0, _tries=20)

    # emp.click(element_user_edit_permission_ok_btn)

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

    # emp.mouse_scroll_down()
    # emp.mouse_scroll_down()
#     # emp.mouse_scroll_down() #so that the submit button is visible #so that the submit button is visible

    #
    def func_(emp):
        elm = emp.locate(element_user_edit_btn_2, _confidence=0.9)
        emp.click(elm) #confirm password
    emp.promise(_func=func_, _tooltip="click submit btn")

    #
    def func_(emp):
        elm = emp.locate(element_user_add_success_message, _confidence=0.9)
        if(elm):
            print("user added successfully")
        else:
            print("failed to add user")
    emp.promise(_func=func_, _tooltip="check for success message")

    #
    def func_(emp):
        elm = emp.locate(element_user_add_success, _confidence=0.9)
        emp.click(elm) #confirm password
    emp.promise(_func=func_, _tooltip="click ok btn")