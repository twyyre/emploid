from load_elements import *

def action_login(emp, _username, _password):
    user_name = _username
    user_password = _password
    
    check = emp.input_into(user_name, element_username_input, "input username")
    if(check):
        col = "btn-success"
        result = "success"
    else:
        col = "btn-danger"
        result = "failed"
    emp.scribe.insert_row(0, "login", "input username", result, col, _scribble=True)

    # emp.moveto(element_jumhuriya_logo) #move away from password input so that it is detectable again
    check = emp.input_into(user_password, element_password_input, "input password")
    if(check):
        col = "btn-success"
        result = "success"
    else:
        col = "btn-danger"
        result = "failed"
    emp.scribe.insert_row(0, "login", "input password", result, col, _scribble=True)

    check = emp.click(element_password_show_btn, "click on show password")
    if(check):
        col = "btn-success"
        result = "success"
    else:
        col = "btn-danger"
        result = "failed"
    emp.scribe.insert_row(0, "login", "click on show password btn", result, col, _scribble=True)

    check = emp.click(element_signin_btn, "click submit")
    if(check):
        col = "btn-success"
        result = "success"
    else:
        col = "btn-danger"
        result = "failed"
    emp.scribe.insert_row(0, "login", "click submit", result, col, _scribble=True)
