import json
import requests
from emploid import Emploid
from api import API
from time import sleep
from load_elements import *
from tools import log
from modules.testman.testman import Testman
from constants import *
from tools import wait
testman = Testman()
testman.delete_user(_username=ADMIN_USERNAME)
testman.create_user(_username=ADMIN_USERNAME, _password=ADMIN_PASSWORD)
user_id = testman.get_user_id(_username=ADMIN_USERNAME)
testman.set_sn_state(_sn=SN, _state=1)
OTP = testman.get_otp(_sn=SN)
JWT = testman.user_signin(_username=ADMIN_USERNAME, _password=ADMIN_PASSWORD, _otp=OTP)
testman.set_user_sn(_userid=user_id, _sn=SN, _token=JWT)
# testman.replace_user_sn(_userid=user_id, _sn=SN, _token=JWT)
# exit()
# wait(60)

OTP = testman.get_otp(_sn=SN)
testman.otp_signin(_userid=user_id, _otp=OTP, _token=JWT)
# testman.get_merchant_by_name(_account_no=127207000000100, _account_type=1, _branch_id=1, _token=JWT)
testman.set_sn_state(_sn=SN, _state=0)
# testman.delete_user(_username=ADMIN_USERNAME)
testman.test_event(_userid=user_id)
print("finished")
exit()

emp = Emploid()
emp.set_failsafe(False)
emp.set_delay(0.2)
show = emp.show
show("started")

from modules.taskman.taskman import Taskman
taskman = Taskman()
beholder = taskman.start_task("record.py")

#
def func_(emp):
    chrome = emp.chrome_run(_url=front_url)
emp.promise(_func=func_, _tooltip="open chrome window")

from actions.action_login import action_login
from actions.action_add_user import action_add_user
from actions.action_logout import action_logout

action_login(emp, _username="ayoubqa", _password="11111111")

#
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="ayoubalmontaser01", 
    _email="ab@gmail.com", 
    _mobile="910953021", 
    _password="09090909", 
    _type=1
)

#
action_logout(emp)

taskman.kill_task(beholder, _delay=2)
show("FINISHED")
exit()