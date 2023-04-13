from emploid import Emploid
from api import API
from time import sleep
from load_elements import *

emp = Emploid()
emp.set_failsafe(False)
# emp.set_delay(0.2)
show = emp.show
show("started")

from modules.taskman.taskman import Taskman
taskman = Taskman()
beholder = taskman.start_task("record.py")

def func_(emp):
    emp.chrome_run(_url="http://10.10.20.44:4455/", _maximized=False)
emp.promise(_func=func_, _tooltip="open chrome window")

sleep(2)

from actions. action_login import action_login
from actions. action_search_user import action_search_user
from actions. action_get_user_info import action_get_user_info
from actions. action_logout import action_logout

action_login(emp, _username="shewa", _password="11111111")
action_search_user(emp, _username="ayoub")
action_logout(emp)

taskman.kill_task(beholder, _delay=2)
show("FINISHED")
exit()
