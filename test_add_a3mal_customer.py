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
from actions.action_add_a3mal_customer import action_add_a3mal_customer
from actions.action_logout import action_logout

action_login(emp, _username="shewa", _password="11111111")
action_add_a3mal_customer(emp, _nationality=0, _national_id="11919519515", _company_name="شركة", _commerical_record="11119519515", _license_number="11119519515", _license_date="٢٠٢٣", _branch="branch", _branch_id="branch ID", _account_desc="account description")
action_logout(emp)

show("FINISHED")
exit()
