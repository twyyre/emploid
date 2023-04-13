from emploid import Emploid
from api import API
from time import sleep
from load_elements import *

emp = Emploid()
emp.set_failsafe(False)
emp.set_delay(0.2)
show = emp.show
show("started")

def func_(emp):
    emp.chrome_run(_url="http://10.10.20.44:4455/", _maximized=False)
emp.promise(_func=func_, _tooltip="open chrome window")

from actions.action_login import action_login
from actions.action_manage_data_customer import action_manage_data_customer
from actions.action_logout import action_logout

action_login(emp, _username="shewa", _password="11111111")
action_manage_data_customer(emp, _account_number="1191111111")
# action_logout(emp)

show("FINISHED")
exit()