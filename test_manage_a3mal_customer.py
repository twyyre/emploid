from emploid import Emploid
from api import API
from time import sleep
from load_elements import *

emp = Emploid()
emp.set_failsafe(False)
emp.set_delay(0.2)
show = emp.show
show("started")

#
def func_(emp):
    emp.chrome_run(_url="http://10.10.20.44:4455/", _maximized=False)
emp.promise(_func=func_, _tooltip="open chrome window")

sleep(2)

from actions.action_login import action_login
from actions.action_manage_a3mal_customer import action_manage_a3mal_customer
from actions.action_logout import action_logout

action_login(emp, _username="shewa", _password="11111111")
action_manage_a3mal_customer(emp, _national_id="119555777555", _mobile="944986055")

# action_logout(emp)
show("FINISHED")
