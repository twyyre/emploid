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

test_url = "http://10.10.20.45:8001/"

testcasename="GIVEN no username, no password"
beholder = taskman.start_task("record.py", testcasename)
emp.chrome_run(_url=test_url, _use_selenium=SETTINGS_USE_SELENIUM)
logged_in = action_login(emp, _username="", _password="11111111")
emp.scribe.insert_row(0, "login", "True", "success", "btn-success", _scribble=True)
action_logout(emp)
emp.scribe.insert_row(0, "logout", "True", "success", "btn-success", _scribble=True)
taskman.kill_task(beholder, _delay=2)
exit()
testcasename="GIVEN no username, correct password"
beholder = taskman.start_task("record.py", testcasename)
sleep(0.5)
emp.chrome_run(_url=test_url, _use_selenium=SETTINGS_USE_SELENIUM)
action_login(emp, _username="", _password="11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename="GIVEN existing username, no password"
beholder = taskman.start_task("record.py", testcasename)
sleep(0.5)
emp.chrome_run(_url=test_url, _use_selenium=SETTINGS_USE_SELENIUM)
action_login(emp, _username="ayoubqa", _password="")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename="GIVEN non-existing username, correct password"
beholder = taskman.start_task("record.py", testcasename)
sleep(0.5)
emp.chrome_run(_url=test_url, _use_selenium=SETTINGS_USE_SELENIUM)
action_login(emp, _username="shnubbles", _password="11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename="GIVEN existing username, wrong password"
beholder = taskman.start_task("record.py", testcasename)
sleep(0.5)
emp.chrome_run(_url=test_url, _use_selenium=SETTINGS_USE_SELENIUM)
action_login(emp, _username="shnubbles", _password="99999999")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename="GIVEN invalid case username, correct password"
beholder = taskman.start_task("record.py", testcasename)
sleep(0.5)
emp.chrome_run(_url=test_url, _use_selenium=SETTINGS_USE_SELENIUM)
action_login(emp, _username="ayoubQA", _password="11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename="GIVEN existing username, invalid case password"
beholder = taskman.start_task("record.py", testcasename)
sleep(0.5)
emp.chrome_run(_url=test_url, _use_selenium=SETTINGS_USE_SELENIUM)
action_login(emp, _username="shnubbles", _password="11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename="GIVEN extended username, correct password"
beholder = taskman.start_task("record.py", testcasename)
sleep(0.5)
emp.chrome_run(_url=test_url, _use_selenium=SETTINGS_USE_SELENIUM)
action_login(emp, _username="ayoubqa____", _password="11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename="GIVEN existing username, extended password"
beholder = taskman.start_task("record.py", testcasename)
sleep(0.5)
emp.chrome_run(_url=test_url, _use_selenium=SETTINGS_USE_SELENIUM)
action_login(emp, _username="shnubbles", _password="11111111____")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename="0-GIVEN padded username, correct password"
beholder = taskman.start_task("record.py", testcasename)
sleep(0.5)
emp.chrome_run(_url=test_url, _use_selenium=SETTINGS_USE_SELENIUM)
action_login(emp, _username="____ayoubqa", _password="11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename="1-GIVEN existing username, padded password"
beholder = taskman.start_task("record.py", testcasename)
sleep(0.5)
emp.chrome_run(_url=test_url, _use_selenium=SETTINGS_USE_SELENIUM)
action_login(emp, _username="shnubbles", _password="____11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename="2-GIVEN existing username, space before password"
beholder = taskman.start_task("record.py", testcasename)
sleep(0.5)
emp.chrome_run(_url=test_url, _use_selenium=SETTINGS_USE_SELENIUM)
action_login(emp, _username="shnubbles", _password=" 11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename="3-GIVEN existing username, space after password"
beholder = taskman.start_task("record.py", testcasename)
sleep(0.5)
emp.chrome_run(_url=test_url, _use_selenium=SETTINGS_USE_SELENIUM)
action_login(emp, _username="shnubbles", _password="11111111 ")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename="4-GIVEN space after existing username, correct password"
beholder = taskman.start_task("record.py", testcasename)
sleep(0.5)
emp.chrome_run(_url=test_url, _use_selenium=SETTINGS_USE_SELENIUM)
action_login(emp, _username="ayoubqa ", _password="11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename="5-GIVEN space before existing username, correct password"
beholder = taskman.start_task("record.py", testcasename)
sleep(0.5)
emp.chrome_run(_url=test_url, _use_selenium=SETTINGS_USE_SELENIUM)
action_login(emp, _username=" ayoubqa", _password="11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename="16-GIVEN arabic characters in username, correct password"
beholder = taskman.start_task("record.py", testcasename)
sleep(0.5)
emp.chrome_run(_url=test_url, _use_selenium=SETTINGS_USE_SELENIUM)
action_login(emp, _username="ayoubqaعربي", _password="11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename="17-GIVEN existing username, correct password"
# beholder = taskman.start_task("record.py", testcasename)
# sleep(0.5)
# emp.chrome_run(_url=test_url, _use_selenium=SETTINGS_USE_SELENIUM)
# action_login(emp, _username="ayoubqa", _password="11111111")
# action_logout(emp)
# taskman.kill_task(beholder, _delay=2)