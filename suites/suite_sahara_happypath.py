#import from parent directory
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from emploid import Emploid
from time import sleep
from load_elements import *
from constants import *

emp = Emploid()
emp.set_failsafe(False)
emp.set_delay(0.2)
show = emp.show
show("started")

from actions.action_login import action_login
from actions.action_logout import action_logout
from modules.taskman.taskman import Taskman
taskman = Taskman()

testcasename="first time login"
beholder = taskman.start_task("record.py", testcasename)
emp.chrome_run(_url=TEST_URL, _use_selenium=SETTINGS_USE_SELENIUM)
logged_in = action_login(emp, _username=TEST_USERNAME, _password=TEST_PASSWORD)
emp.scribe.insert_row(0, "login", "True", "success", "btn-success", _scribble=True)
action_logout(emp)
emp.scribe.insert_row(0, "logout", "True", "success", "btn-success", _scribble=True)
taskman.kill_task(beholder, _delay=2)

testcasename="login with deactivated user"
beholder = taskman.start_task("record.py", testcasename)
emp.chrome_run(_url=TEST_URL, _use_selenium=SETTINGS_USE_SELENIUM)
logged_in = action_login(emp, _username="deactivateduser", _password="44444444")
emp.scribe.insert_row(0, "login", "True", "success", "btn-success", _scribble=True)
action_logout(emp)
emp.scribe.insert_row(0, "logout", "True", "success", "btn-success", _scribble=True)
taskman.kill_task(beholder, _delay=2)