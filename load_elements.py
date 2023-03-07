from emploid import Emploid
from api import API
from time import sleep

emp = Emploid()

element_goto_management = emp.import_image("goto_management/goto_management.png")
element_jumhuriya_logo = emp.import_image(_dir='logo/jumhuriya_logo.png')

#main section section btns
element_customer_management = emp.import_image(_dir='customer_management/customer_management.png')

#login
element_username_input = emp.import_image(_dir='username_input/username_input.png')
element_password_input = emp.import_image(_dir='password_input/password_input.png')
element_signin_btn = emp.import_image(_dir='signin_btn/signin_btn.png')

#logout
element_logout = emp.import_image(_dir='logout/logout.png')
element_logout_yes = emp.import_image(_dir='logout_yes/logout_yes.png')

#change password
element_change_password = emp.import_image(_dir='change_password/change_password.png')
element_change_password_input = emp.import_image(_dir='change_password/change_password_input.png')
element_change_password_confirm = emp.import_image(_dir='change_password/change_password_confirm.png')
element_change_password_success = emp.import_image(_dir='change_password/success.png')

#user management
#user add
element_user_add = emp.import_image(_dir='user_management/user_add/user_add.png')
element_user_type_system_admin = emp.import_image(_dir='user_management/user_add/user_type_system_admin.png')
element_user_type_bank_employee = emp.import_image(_dir='user_management/user_add/user_type_bank_employee.png')
element_user_type_branch_employee = emp.import_image(_dir='user_management/user_add/user_type_branch_employee.png')

#add user inputs
element_user_add_name_input = emp.import_image(_dir='user_management/user_add/user_add_name_input.png')
element_user_add_username_input = emp.import_image(_dir='user_management/user_add/user_add_username_input.png')
element_user_add_email_input = emp.import_image(_dir='user_management/user_add/user_add_email_input.png')
element_user_add_mobile_input = emp.import_image(_dir='user_management/user_add/user_add_mobile_input.png')
element_user_add_password_input = emp.import_image(_dir='user_management/user_add/user_add_password_input.png')
element_user_add_password_confirm_input = emp.import_image(_dir='user_management/user_add/user_add_password_confirm_input.png')
element_user_add_add = emp.import_image(_dir='user_management/user_add/user_add_add.png')
element_user_add_success_message = emp.import_image(_dir='user_management/user_add/user_add_success_message.png')
element_user_add_success = emp.import_image(_dir='user_management/user_add/user_add_success.png')

#
element_dashboard_btns = emp.import_image(_dir="user_tracking/user_tracking_management_btns/user_tracking_management_btns.png")

#
element_user_search_input = emp.import_image(_dir='user_management/user_search/user_search_input.png')
element_user_edit_btn = emp.import_image(_dir='user_management/user_search/user_edit_btn.png')

#windows button
element_windows_btn = emp.import_image(_dir='elm.png')

#testing------------------------------------------------------------------
elm_test_1 = emp.import_image(_dir='abc.png')

#user edit
element_user_edit_name_input = emp.import_image(_dir="user_management/user_edit/user_name_inpt.png")
element_user_edit_username_input = emp.import_image(_dir="user_management/user_edit/user_username_inpt.png")
element_user_edit_email_input = emp.import_image(_dir="user_management/user_edit/user_email_inpt.png")
element_user_edit_mobile_input = emp.import_image(_dir="user_management/user_edit/user_mobile_inpt.png")
element_user_edit_btn_2 = emp.import_image(_dir="user_management/user_edit/user_edit_btn_2.png")
element_user_exit_edit_screen = emp.import_image(_dir="user_management/user_edit/user_exit_edit_screen.png")

#user change password 2
element_user_change_password_btn = emp.import_image(_dir="user_management/user_change_password/user_change_password_btn.png")
element_user_change_password_confirm_btn = emp.import_image(_dir="user_management/user_change_password/user_change_password.png")
element_user_copy_new_password = emp.import_image(_dir="user_management/user_change_password/user_copy_new_password.png")

#user activate
element_user_activate_btn = emp.import_image(_dir="user_management/user_activate/activate_btn.png")
element_user_deactivate_btn = emp.import_image(_dir="user_management/user_activate/deactivate_btn.png")
element_user_activate_accept = emp.import_image(_dir="user_management/user_activate/accept.png")
element_user_activision_state = emp.import_image(_dir="user_management/user_activate/activision_state.png")
element_user_activate_note_inpt = emp.import_image(_dir="user_management/user_activate/note_inpt.png")

#customer add 
element_customer_branch_inpt = emp.import_image(_dir="customer_management/customer_add/branch_inpt.png")
element_customer_account_number_inpt = emp.import_image(_dir="customer_management/customer_add/account_number_inpt.png")
element_customer_next_btn = emp.import_image(_dir="customer_management/customer_add/next_btn.png")

element_customer_branch_one_inpt_option = emp.import_image(_dir="customer_management/customer_add/branch_one_inpt_option.png")
element_customer_branch_two_inpt_option = emp.import_image(_dir="customer_management/customer_add/branch_two_inpt_option.png")
element_customer_branch_three_inpt_option = emp.import_image(_dir="customer_management/customer_add/branch_three_inpt_option.png")

#customer a3mal add
element_customer_a3mal_national_id_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/national_id_inpt.png")
element_customer_a3mal_nationality_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/nationality_inpt.png")
element_customer_a3mal_next_btn = emp.import_image(_dir="customer_management/customer_a3mal_add/next.png")

element_customer_a3mal_citizen_inpt_option = emp.import_image(_dir="customer_management/customer_a3mal_add/citizen_inpt_option.png")
element_customer_a3mal_non_citizen_inpt_option = emp.import_image(_dir="customer_management/customer_a3mal_add/non_citizen_inpt_option.png")
element_customer_a3mal_account_number_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/account_number_inpt.png")

element_customer_account_number_inpt = emp.import_image(_dir="customer_management/customer_add/account_number_inpt.png") #duplicate

# element_customer_non_branch_inpt = emp.import_image(_dir="customer_management/customer_add/non_branch_inpt.png")

element_customer_error_account_number_is_not_valid = emp.import_image(_dir="customer_management/customer_add/errors/accountNumberIsNotValid.png")

element_customer_a3mal_company_name_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/company_name_inpt.png")

element_customer_a3mal_commercial_record_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/commerical_record_inpt.png")

element_customer_a3mal_license_number_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/license_number_inpt.png")

element_customer_a3mal_license_date_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/license_date_inpt.png")

element_customer_a3mal_account_type_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/account_type_inpt.png")

element_customer_a3mal_branch_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/branch_inpt.png")

element_customer_a3mal_branch_id_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/branch_id_inpt.png")

element_customer_a3mal_account_desc_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/account_desc_inpt.png")

element_customer_a3mal_add_btn = emp.import_image(_dir="customer_management/customer_a3mal_add/add_btn.png")

element_customer_a3mal_next_btn2 = emp.import_image(_dir="customer_management/customer_a3mal_add/next_btn.png")

element_customer_a3mal_license_date_entry_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/license_date_entry_inpt.png")

element_customer_a3mal_license_date_entry_btn = emp.import_image(_dir="customer_management/customer_a3mal_add/license_date_entry_btn.png")

element_customer_a3mal_hasanan = emp.import_image(_dir="customer_management/customer_a3mal_add/hasanan.png")

element_customer_a3mal_account_type_option_current = emp.import_image(_dir="customer_management/customer_a3mal_add/current_account_option.png")

element_customer_a3mal_account_type_option_aggregate = emp.import_image(_dir="customer_management/customer_a3mal_add/aggregate_account_option.png")
element_customer_a3mal_otp_sn_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/otp_sn_inpt.png")

element_customer_a3mal_customer_name_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_name_inpt.png")
element_customer_a3mal_customer_firstname_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_firstname_inpt.png")
element_customer_a3mal_customer_middlename_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_middlename_inpt.png")
element_customer_a3mal_customer_lastname_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_lastname_inpt.png")
element_customer_a3mal_customer_gender_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_gender_inpt.png")
element_customer_a3mal_customer_gender_male = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_gender_male.png")
element_customer_a3mal_customer_gender_female = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_gender_female.png")
element_customer_a3mal_customer_mothername_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_mothername_inpt.png")
element_customer_a3mal_customer_birthplace_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_birthplace_inpt.png")
element_customer_a3mal_customer_birthdate_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_birthdate_inpt.png")
element_customer_a3mal_customer_status_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_status_inpt.png")
element_customer_a3mal_customer_status_single = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_status_single.png")
element_customer_a3mal_customer_status_widowed = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_status_widowed.png")
element_customer_a3mal_customer_status_married = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_status_married.png")
element_customer_a3mal_customer_status_divorced = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_status_divorced.png")
element_customer_a3mal_customer_passport_number_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_passport_number_inpt.png")
element_customer_a3mal_customer_passport_publish_location_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_publish_location_inpt.png")
element_customer_a3mal_customer_passport_publish_date_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_publish_date_inpt.png")
element_customer_a3mal_customer_passport_expiration_date_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_expiration_date_inpt.png")
element_customer_a3mal_customer_familyhead_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_familyhead_inpt.png")
element_customer_a3mal_customer_familyhead_yes_option = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_familyhead_yes_option.png")
element_customer_a3mal_customer_familyhead_no_option = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_familyhead_no_option.png")
element_customer_a3mal_customer_passport_id_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_passport_id_inpt.png")
element_customer_a3mal_customer_family_members_number_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_family_members_number.png")
element_customer_a3mal_customer_email_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_email_inpt.png")
element_customer_a3mal_customer_city_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_city_inpt.png")
element_customer_a3mal_customer_area_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_area_inpt.png")
element_customer_a3mal_customer_mobile_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_mobile_inpt.png")
element_customer_a3mal_customer_mobile_confirm_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_mobile_confirm_inpt.png")
element_customer_a3mal_customer_add_btn = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_add_btn.png")
element_customer_a3mal_customer_contract_number_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/contract_number_inpt.png")
element_customer_a3mal_customer_contract_number_confirm_inpt = emp.import_image(_dir="customer_management/customer_a3mal_add/contract_number_confirm_inpt.png")
element_customer_a3mal_customer_next_btn_3 = emp.import_image(_dir="customer_management/customer_a3mal_add/next_btn_3.png")
element_customer_a3mal_customer_confirm_btn_3 = emp.import_image(_dir="customer_management/customer_a3mal_add/confirm_btn_3.png")
element_customer_a3mal_customer_add_btn_2 = emp.import_image(_dir="customer_management/customer_a3mal_add/customer_add_btn_2.png")
element_customer_a3mal_customer_add_success = emp.import_image(_dir="customer_management/customer_a3mal_add/success.png")
element_customer_a3mal_customer_ok_btn = emp.import_image(_dir="customer_management/customer_a3mal_add/ok.png")

#customer manage data
element_customer_manage_data_branch_inpt = emp.import_image(_dir="customer_management/customer_data_management/customer_manage_data/branch_inpt.png")
element_customer_manage_data_account_number_inpt = emp.import_image(_dir="customer_management/customer_data_management/customer_manage_data/account_number_inpt.png")
element_customer_manage_data_search_btn = emp.import_image(_dir="customer_management/customer_data_management/customer_manage_data/search_btn.png")

#errors
element_error_noDataToShow = emp.import_image(_dir="error/noDataToShow.png")
element_error_nationalIdAlreadyUsed = emp.import_image(_dir="error/nationalIdAlreadyUsed.png")
element_error_customerAlreadyExists = emp.import_image(_dir="error/customerAlreadyExists.png")
element_error_otpNotAvailable = emp.import_image(_dir="error/otpNotAvailable.png")



