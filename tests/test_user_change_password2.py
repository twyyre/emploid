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

#
try:
    from actions.action_login import action_login
    pass
except Exception as e:
    print("login action")
    print(e)
    input()
    exit()
#
try:
    from actions.action_search_user import action_search_user
except Exception as e:
    print("add user action")
    print(e)
    input()
    exit()
#
try:
    from actions.action_change_password_2 import action_change_password
except Exception as e:
    print("add user action")
    print(e)
    input()
    exit()

show("FINISHED")
exit()