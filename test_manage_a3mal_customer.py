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
    import actions.action_login
    pass
except Exception as e:
    print("login action failed")
    print(e)
    input()
    exit()

#
try:
    import actions.action_manage_a3mal_customer
except Exception as e:
    print("add user action failed")
    print(e)
    input()
    exit()

#
try:
    import actions.action_logout
except Exception as e:
    print("add user action failed")
    print(e)
    input()
    exit()
show("FINISHED")
exit()
