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

element_customer_account_number_inpt = emp.import_image(_dir="customer_management/customer_add/account_number_inpt.png")
element_customer_non_branch_inpt = emp.import_image(_dir="customer_management/customer_add/non_branch_inpt.png")

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