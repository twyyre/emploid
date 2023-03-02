from emploid import Emploid
from api import API
from time import sleep
from load_elements import *

emp = Emploid()
emp.set_failsafe(False)
emp.set_delay(0.2)
show = emp.show
show("started")

if(emp.screen_get_size()!=(1920, 1080)):
    raise Exception("resolution is not supported.")

emp.chrome_run(_url="http://10.10.20.44:4455/")

#
try:
    from actions.action_login import action_login
    action_login(emp, _username="shewa", _password="11111111")
    pass
except Exception as e:
    print("login action failed")
    print(e)
    input()
    exit()
#
try:
    from actions.action_logout import action_logout
    action_logout(emp)
except Exception as e:
    print("login action failed")
    print(e)
    input()
    exit()

show("FINISHED")
exit()
