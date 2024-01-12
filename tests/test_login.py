from emploid import Emploid
from api import API
from time import sleep
from load_elements import *

emp = Emploid()
emp.set_failsafe(False)
emp.set_delay(0.2)
show = emp.show
show("started")

def test_login(_username, _password):
    from modules.taskman.taskman import Taskman
    taskman = Taskman()
    beholder = taskman.start_task("record.py")

    emp.chrome_run(_url="http://10.10.20.45:8001/app")

    try:
        from actions.action_login import action_login
        action_login(emp, _username=_username, _password=_password)
    except Exception as e:
        print("login action failed")
        print(e)
        exit()

    taskman.kill_task(beholder, _delay=2)
    show("FINISHED")

test_login(_username="shewa", _password="22222222")
