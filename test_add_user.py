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
beholder = taskman.start_task("record.py")

#
def func_(emp):
    chrome = emp.chrome_run(_url="http://10.10.20.44:4455/", _maximized=False)
emp.promise(_func=func_, _tooltip="open chrome window")


from actions.action_login import action_login
from actions.action_add_user import action_add_user
from actions.action_logout import action_logout


action_login(emp, _username="shewa", _password="11111111")

#
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="ayoubalmontaser01", 
    _email="ab@gmail.com", 
    _mobile="0910953021", 
    _password="09090909", 
    _type=1
)

#
action_logout(emp)

taskman.kill_task(beholder, _delay=2)
show("FINISHED")
exit()