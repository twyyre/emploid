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
element_password_show_btn = emp.import_image(_dir='password_show_btn.png')

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
element_user_add_branch_option_one = emp.import_image(_dir='user_management/user_add/user_add_branch_option_one.png')

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
element_user_edit_success = emp.import_image(_dir="user_management/user_edit/success.png")
element_user_edit_branch_inpt = emp.import_image(_dir="user_management/user_edit/branch_inpt.png")
element_user_edit_branch_option_one = emp.import_image(_dir="user_management/user_edit/branch_option_one.png")
element_user_edit_branch_option_two = emp.import_image(_dir="user_management/user_edit/branch_option_two.png")
element_user_edit_branch_option_three = emp.import_image(_dir="user_management/user_edit/branch_option_three.png")
element_user_edit_permission_inpt = emp.import_image(_dir="user_management/user_edit/permission_inpt.png")

#permissions on edit screen input
element_user_edit_permission_ok_btn = emp.import_image(_dir="user_management/user_edit/permission_ok_btn.png")
element_user_edit_permission_inpt = emp.import_image(_dir="user_management/user_edit/permission_inpt.png")

element_user_edit_permission_1_insertAfrad = emp.import_image(_dir="user_management/user_edit/permissions/permission_1_insertAfrad.png")
element_user_edit_permission_2_insertA3mal = emp.import_image(_dir="user_management/user_edit/permissions/permission_2_insertA3mal.png")
element_user_edit_permission_3_activateBankAfrad = emp.import_image(_dir="user_management/user_edit/permissions/permission_3_activateBankAfrad.png")
element_user_edit_permission_4_activateBankA3mal = emp.import_image(_dir="user_management/user_edit/permissions/permission_4_activateBankA3mal.png")
element_user_edit_permission_5_confirmChangesAfrad = emp.import_image(_dir="user_management/user_edit/permissions/permission_5_confirmChangesAfrad.png")
element_user_edit_permission_6_manageA3malActivsion = emp.import_image(_dir="user_management/user_edit/permissions/permission_6_manageA3malActivsion.png")
element_user_edit_permission_7_activateServiceAfrad = emp.import_image(_dir="user_management/user_edit/permissions/permission_7_activateServiceAfrad.png")
element_user_edit_permission_8_upgradeAfrad = emp.import_image(_dir="user_management/user_edit/permissions/permission_8_upgradeAfrad.png")
element_user_edit_permission_9_afradEventTracking = emp.import_image(_dir="user_management/user_edit/permissions/permission_9_afradEventTracking.png")
element_user_edit_permission_10_Review = emp.import_image(_dir="user_management/user_edit/permissions/permission_10_Review.png")
element_user_edit_permission_11_updateActiveA3mal = emp.import_image(_dir="user_management/user_edit/permissions/permission_11_updateActiveA3mal.png")
element_user_edit_permission_12_updateCustomerA3mal = emp.import_image(_dir="user_management/user_edit/permissions/permission_12_updateCustomerA3mal.png")
element_user_edit_permission_13_changeActivisionAfrad = emp.import_image(_dir="user_management/user_edit/permissions/permission_13_changeActivisionAfrad.png")
element_user_edit_permission_14_activateServicesA3mal = emp.import_image(_dir="user_management/user_edit/permissions/permission_14_activateServicesA3mal.png")
element_user_edit_permission_15_upgradeA3mal = emp.import_image(_dir="user_management/user_edit/permissions/permission_15_upgradeA3mal.png")
element_user_edit_permission_16_reporting = emp.import_image(_dir="user_management/user_edit/permissions/permission_16_reporting.png")
element_user_edit_permission_17_payment = emp.import_image(_dir="user_management/user_edit/permissions/permission_17_payment.png")
element_user_edit_permission_18_paymentReporting = emp.import_image(_dir="user_management/user_edit/permissions/permission_18_paymentReporting.png")
element_user_edit_permission_19_a3malEventTracking = emp.import_image(_dir="user_management/user_edit/permissions/permission_19_a3malEventTracking.png")
element_user_edit_permission_20_afradPinReminder = emp.import_image(_dir="user_management/user_edit/permissions/permission_20_afradPinReminder.png")
element_user_edit_permission_21_a3malPinReminder = emp.import_image(_dir="user_management/user_edit/permissions/permission_21_a3malPinReminder.png")
element_user_edit_permission_22_afradSmsTracking = emp.import_image(_dir="user_management/user_edit/permissions/permission_22_afradSmsTracking.png")
element_user_edit_permission_23_a3malSmsTracking = emp.import_image(_dir="user_management/user_edit/permissions/permission_23_a3malSmsTracking.png")
element_user_edit_permission_24_afradAppTracking = emp.import_image(_dir="user_management/user_edit/permissions/permission_24_afradAppTracking.png")
element_user_edit_permission_25_a3malAppTracking = emp.import_image(_dir="user_management/user_edit/permissions/permission_25_a3malAppTracking.png")
element_user_edit_permission_26_viewCustomerManagement = emp.import_image(_dir="user_management/user_edit/permissions/permission_26_viewCustomerManagement.png")
element_user_edit_permission_27_viewA3malManagement = emp.import_image(_dir="user_management/user_edit/permissions/permission_27_viewA3malManagement.png")
element_user_edit_permission_28_updateA3malAccounts = emp.import_image(_dir="user_management/user_edit/permissions/permission_28_updateA3malAccounts.png")
element_user_edit_permission_29_addA3malOtp = emp.import_image(_dir="user_management/user_edit/permissions/permission_29_addA3malOtp.png")
element_user_edit_permission_30_replaceA3malOtp = emp.import_image(_dir="user_management/user_edit/permissions/permission_30_replaceA3malOtp.png")
element_user_edit_permission_31_addA3malCompany = emp.import_image(_dir="user_management/user_edit/permissions/permission_31_addA3malCompany.png")
element_user_edit_permission_32_updateA3malCompany = emp.import_image(_dir="user_management/user_edit/permissions/permission_32_updateA3malCompany.png")
element_user_edit_permission_33_a3malAddAccountToCompany = emp.import_image(_dir="user_management/user_edit/permissions/permission_33_a3malAddAccountToCompany.png")
element_user_edit_permission_34_a3malUserChangeActivision = emp.import_image(_dir="user_management/user_edit/permissions/permission_34_a3malUserChangeActivision.png")
element_user_edit_permission_35_a3malUserUpdateAccounts = emp.import_image(_dir="user_management/user_edit/permissions/permission_35_a3malUserUpdateAccounts.png")
element_user_edit_permission_36_reviewPhone = emp.import_image(_dir="user_management/user_edit/permissions/permission_36_reviewPhone.png")
element_user_edit_permission_37_showRejected = emp.import_image(_dir="user_management/user_edit/permissions/permission_37_showRejected.png")
element_user_edit_permission_38_showRejected = emp.import_image(_dir="user_management/user_edit/permissions/permission_38_showRejected.png")
element_user_edit_permission_39_checkBookManagement = emp.import_image(_dir="user_management/user_edit/permissions/permission_39_checkBookManagement.png")
element_user_edit_permission_40_problemTrackingAfrad = emp.import_image(_dir="user_management/user_edit/permissions/permission_40_problemTrackingAfrad.png")
element_user_edit_permission_41_problemTrackingA3mal = emp.import_image(_dir="user_management/user_edit/permissions/permission_41_problemTrackingA3mal.png")
element_user_edit_permission_42_registrationRequests = emp.import_image(_dir="user_management/user_edit/permissions/permission_42_registrationRequests.png")
element_user_edit_permission_43_a3malUserResetId = emp.import_image(_dir="user_management/user_edit/permissions/permission_43_a3malUserResetId.png")
element_user_edit_permission_44_activateA3malAccounts = emp.import_image(_dir="user_management/user_edit/permissions/permission_44_activateA3malAccounts.png")
element_user_edit_permission_45_insertMerchant = emp.import_image(_dir="user_management/user_edit/permissions/permission_45_insertMerchant.png")
element_user_edit_permission_46_activateMerchant = emp.import_image(_dir="user_management/user_edit/permissions/permission_46_activateMerchant.png")
element_user_edit_permission_47_issueSigninMethods = emp.import_image(_dir="user_management/user_edit/permissions/permission_47_issueSigninMethods.png")
element_user_edit_permission_48_reviewSigninMethods = emp.import_image(_dir="user_management/user_edit/permissions/permission_48_reviewSigninMethods.png")
element_user_edit_permission_49_reviewUpdateMerchantInformation = emp.import_image(_dir="user_management/user_edit/permissions/permission_49_reviewUpdateMerchantInformation.png")
element_user_edit_permission_50_updateMerchantInformation = emp.import_image(_dir="user_management/user_edit/permissions/permission_50_updateMerchantInformation.png")
element_user_edit_permission_51_remindMerchantId = emp.import_image(_dir="user_management/user_edit/permissions/permission_51_remindMerchantId.png")
element_user_edit_permission_52_remindMerchantPin = emp.import_image(_dir="user_management/user_edit/permissions/permission_52_remindMerchantPin.png")
element_user_edit_permission_53_getMerchantInformation = emp.import_image(_dir="user_management/user_edit/permissions/permission_53_getMerchantInformation.png")
element_user_edit_permission_54_activeDisActiveMerchant = emp.import_image(_dir="user_management/user_edit/permissions/permission_54_activeDisActiveMerchant.png")
element_user_edit_permission_55_updateBussinessInfo = emp.import_image(_dir="user_management/user_edit/permissions/permission_55_updateBussinessInfo.png")
element_user_edit_permission_56_reminderMerchantOnlineProviderId = emp.import_image(_dir="user_management/user_edit/permissions/permission_56_reminderMerchantOnlineProviderId.png")
element_user_edit_permission_57_reIssueSigninMethods = emp.import_image(_dir="user_management/user_edit/permissions/permission_57_reIssueSigninMethods.png")
element_user_edit_permission_58_updateMerchantInformation = emp.import_image(_dir="user_management/user_edit/permissions/permission_58_updateMerchantInformation.png")
element_user_edit_permission_59_getMerchantInformation = emp.import_image(_dir="user_management/user_edit/permissions/permission_59_getMerchantInformation.png")

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
element_customer_customer_add_success1 = emp.import_image(_dir="customer_management/customer_add/customer_add_success1.png")
element_customer_lastname_inpt2 = emp.import_image(_dir="customer_management/customer_add/lastname_inpt2.png")
element_customer_hasanan2 = emp.import_image(_dir="customer_management/customer_add/hasanan2.png")
element_customer_gender_inpt2 = emp.import_image(_dir="customer_management/customer_add/gender_inpt2.png")
element_customer_nationality_inpt2 = emp.import_image(_dir="customer_management/customer_add/nationality_inpt2.png")
element_customer_status_inpt2 = emp.import_image(_dir="customer_management/customer_add/customer_status_inpt2.png")
element_customer_contract_number_inpt2 = emp.import_image(_dir="customer_management/customer_add/contract_number_inpt2.png")
element_customer_national_id_inpt2 = emp.import_image(_dir="customer_management/customer_add/national_id_inpt2.png")
element_customer_familyhead_inpt2 = emp.import_image(_dir="customer_management/customer_add/familyhead_inpt2.png")
element_customer_familyhead_yes_option2  = emp.import_image(_dir="customer_management/customer_add/familyhead_yes_option2.png")
element_customer_familyhead_no_option2  = emp.import_image(_dir="customer_management/customer_add/familyhead_no_option2.png")
element_customer_address_inpt  = emp.import_image(_dir="customer_management/customer_add/address_inpt.png")

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

element_customer_a3mal_manage_national_id_inpt = emp.import_image(_dir="customer_management/customer_a3mal_manage/national_id_inpt.png")
element_customer_a3mal_manage_mobile_inpt = emp.import_image(_dir="customer_management/customer_a3mal_manage/mobile_inpt.png")
element_customer_a3mal_manage_search_btn = emp.import_image(_dir="customer_management/customer_a3mal_manage/search_btn.png")

#customer manage data
element_customer_manage_data_branch_inpt = emp.import_image(_dir="customer_management/customer_data_management/customer_manage_data/branch_inpt.png")
element_customer_manage_data_account_number_inpt = emp.import_image(_dir="customer_management/customer_data_management/customer_manage_data/account_number_inpt.png")
element_customer_manage_data_search_btn = emp.import_image(_dir="customer_management/customer_data_management/customer_manage_data/search_btn.png")

#errors
element_error_noDataToShow = emp.import_image(_dir="error/noDataToShow.png")
element_error_nationalIdAlreadyUsed = emp.import_image(_dir="error/nationalIdAlreadyUsed.png")
element_error_customerAlreadyExists = emp.import_image(_dir="error/customerAlreadyExists.png")
element_error_otpNotAvailable = emp.import_image(_dir="error/otpNotAvailable.png")
element_error_customerAlreadyExists2 = emp.import_image(_dir="error/customerAlreadyExists2.png")
element_error_itemAlreadyExists = emp.import_image(_dir="error/itemAlreadyExists.png")