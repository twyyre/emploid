#import from parent directory
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from load_elements import *
from emploid import Emploid
from time import sleep
from constants import *

emp = Emploid()
emp.set_failsafe(False)
emp.set_delay(0.2)
show = emp.show
show("started")

from modules.taskman.taskman import Taskman
from actions.action_login import action_login
from actions.action_add_user import action_add_user
from actions.action_logout import action_logout

taskman = Taskman()

test_url = TEST_URL

testcasename = "GIVEN empty username"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب", 
    _username="", 
    _email="ab@gmail.com", 
    _mobile="944860551", 
    _password="09090909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN username starting with a number"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="1testcase02", 
    _email="ab@gmail.com", 
    _mobile="944860551", 
    _password="09090909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN space before username"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username=" testcase03", 
    _email="ab@gmail.com", 
    _mobile="944860551", 
    _password="09090909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN space after username"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="testcase04 ", 
    _email="ab@gmail.com", 
    _mobile="944860551", 
    _password="09090909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN extended username"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="testcase055aabaaaaaaaaacaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaafaaaaaaaataaaaaaaaaaaaaaaaaaGaaaaaHDA", #extended with a single character beyond validation
    _email="ab@gmail.com", 
    _mobile="944860551", 
    _password="09090909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN existing username missing last character"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="testcase0",
    _email="ab@gmail.com", 
    _mobile="944860551", 
    _password="09090909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN existing username missing first character"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="estcase05",
    _email="ab@gmail.com", 
    _mobile="944860551", 
    _password="09090909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN username consisting of only underscores"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="______",
    _email="ab@gmail.com", 
    _mobile="944860551", 
    _password="09090909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN username consisting of only numbers"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="1213456",
    _email="ab@gmail.com", 
    _mobile="944860551", 
    _password="09090909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN username consisting of uppercase and lower case"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="AYouB",
    _email="ab@gmail.com", 
    _mobile="944860551", 
    _password="09090909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN username consisting of uppercase only"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="AYOUB",
    _email="ab@gmail.com", 
    _mobile="944860551", 
    _password="09090909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN invalid email (missing @)"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="estcase05",
    _email="abgmail.com", 
    _mobile="944860551", 
    _password="09090909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN invalid email (missing .)"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="estcase05",
    _email="ab@gmailcom", 
    _mobile="944860551", 
    _password="09090909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN email starts with a number"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="estcase05",
    _email="1a@g.g", 
    _mobile="944860551", 
    _password="09090909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN mobile number containing letters"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="estcase010",
    _email="ab@gmail.com", 
    _mobile="949999aaa", 
    _password="09090909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN mobile number has more than 9 numbers"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="estcase010",
    _email="ab@gmail.com", 
    _mobile="949888777666555444333222111", 
    _password="09090909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN mobile number has less than 9 numbers"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="estcase010",
    _email="ab@gmail.com", 
    _mobile="94999999", 
    _password="09090909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN mobile number is empty"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="estcase010",
    _email="ab@gmail.com", 
    _mobile="", 
    _password="09090909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN extended password"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="estcase010",
    _email="ab@gmail.com", 
    _mobile="94999999", 
    _password="0909090923432", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN padded password"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="estcase010",
    _email="ab@gmail.com", 
    _mobile="94999999", 
    _password="3453453409090909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN space before password"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="estcase010",
    _email="ab@gmail.com", 
    _mobile="94999999", 
    _password=" 09090909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN space after password"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="estcase010",
    _email="ab@gmail.com", 
    _mobile="94999999", 
    _password="09090909 ", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN space in middle of password"
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="estcase010",
    _email="ab@gmail.com", 
    _mobile="94999999", 
    _password="0909 0909", 
    _type=1
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN user type is admin "
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="estcase010",
    _email="ab@gmail.com", 
    _mobile="94999999",
    _password="09090909", 
    _type=2
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

testcasename = "GIVEN user type is branch user "
beholder = taskman.start_task("record.py", testcasename)
chrome = emp.chrome_run(_url=test_url, _maximized=False)
action_login(emp, _username="protester", _password="11111111")
action_add_user(
    emp,
    _name="أيوب المنتصر", 
    _username="estcase0105",
    _email="ab@gmail.com", 
    _mobile="940953021", 
    _password="09090909", 
    _type=0
)
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

show("FINISHED")
exit()