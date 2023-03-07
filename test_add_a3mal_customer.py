from emploid import Emploid
from api import API
from time import sleep
from load_elements import *

emp = Emploid()
emp.set_failsafe(False)
emp.set_delay(0.2)
show = emp.show
show("started")

from modules.taskman.taskman import Taskman
taskman = Taskman()
task = taskman.start_task("record.py")

def func_(emp):
    emp.chrome_run(_url="http://10.10.20.44:4455/", _maximized=False)
emp.promise(_func=func_, _tooltip="open chrome window")

from actions.action_login import action_login
from actions.action_add_a3mal_customer import action_add_a3mal_customer
from actions.action_logout import action_logout

action_login(emp, _username="shewa", _password="11111111")

action_add_a3mal_customer(emp, 
    _nationality=0, 
    _national_id="119159599815", 
    _company_name="شركة", 
    _commerical_record="11119519515", 
    _license_number="11119519515", 
    _license_date="٢٠٢٣", _branch=0, 
    _branch_id="branch ID", 
    _account_desc="لقد إنه حيث أن سوف لن", 
    _type=0, 
    _account_number="123558755555", 
    _otp_sn="799788888", _gender_type=0, 
    _customer_name="الصندي", 
    _firstname="ayoub", 
    _middlename="meftah", 
    _lastname="almontaser", 
    _mothername="الوالدة", 
    _birthplace="طرابلس", 
    _customer_status=0, 
    _passport_number="12312315231231", 
    _publish_location="طرابلس",
    _familyhead_stat=0,
    _passport_id="394872789423",
    _family_members_number="5",
    _email="itameios@gmail.com",
    _city="طرابلس",
    _area="طريق المطار",
    _mobile="910999900",
    _mobile_confirm="910999900",
    _contract_number="19962023",
    _contract_number_confirm="19962023"
)
input()
action_logout(emp)

task.kill()
show("FINISHED")
exit()
