from load_elements import *

def action_login(emp, _username, _password):
    user_name = _username
    user_password = _password
    emp.input_into(user_name, element_username_input, "input username")
    emp.input_into(user_password, element_password_input, "input password")
    emp.click(element_signin_btn, "click submit")




