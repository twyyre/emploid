from emploid import Emploid
from api import API
from time import sleep
from load_elements import *

emp = Emploid()
emp.set_failsafe(False)
emp.set_delay(0.2)
show = emp.show
show("started")

from actions.action_login import action_login
from actions.action_logout import action_logout
from modules.taskman.taskman import Taskman
taskman = Taskman()

#1-GIVEN no username, no password
beholder = taskman.start_task("record.py")
sleep(0.5)
emp.chrome_run(_url="http://10.10.20.44:4455/")
action_login(emp, _username="", _password="")
action_logout(emp)

#2-GIVEN no username, correct password
beholder = taskman.start_task("record.py")
sleep(0.5)
emp.chrome_run(_url="http://10.10.20.44:4455/")
action_login(emp, _username="", _password="11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

#3-GIVEN existing username, no password
beholder = taskman.start_task("record.py")
sleep(0.5)
emp.chrome_run(_url="http://10.10.20.44:4455/")
action_login(emp, _username="shewa", _password="")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

#4-GIVEN non-existing username, correct password
beholder = taskman.start_task("record.py")
sleep(0.5)
emp.chrome_run(_url="http://10.10.20.44:4455/")
action_login(emp, _username="shnubbles", _password="11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

#5-GIVEN existing username, wrong password
beholder = taskman.start_task("record.py")
sleep(0.5)
emp.chrome_run(_url="http://10.10.20.44:4455/")
action_login(emp, _username="shnubbles", _password="99999999")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

#6-GIVEN invalid case username, correct password
beholder = taskman.start_task("record.py")
sleep(0.5)
emp.chrome_run(_url="http://10.10.20.44:4455/")
action_login(emp, _username="SheWa", _password="11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

#7-GIVEN existing username, invalid case password
beholder = taskman.start_task("record.py")
sleep(0.5)
emp.chrome_run(_url="http://10.10.20.44:4455/")
action_login(emp, _username="shnubbles", _password="11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

#8-GIVEN extended username, correct password
beholder = taskman.start_task("record.py")
sleep(0.5)
emp.chrome_run(_url="http://10.10.20.44:4455/")
action_login(emp, _username="shewa____", _password="11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

#9-GIVEN existing username, extended password
beholder = taskman.start_task("record.py")
sleep(0.5)
emp.chrome_run(_url="http://10.10.20.44:4455/")
action_login(emp, _username="shnubbles", _password="11111111____")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

#10-GIVEN padded username, correct password
beholder = taskman.start_task("record.py")
sleep(0.5)
emp.chrome_run(_url="http://10.10.20.44:4455/")
action_login(emp, _username="____shewa", _password="11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

#11-GIVEN existing username, padded password
beholder = taskman.start_task("record.py")
sleep(0.5)
emp.chrome_run(_url="http://10.10.20.44:4455/")
action_login(emp, _username="shnubbles", _password="____11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

#12-GIVEN existing username, space before password
beholder = taskman.start_task("record.py")
sleep(0.5)
emp.chrome_run(_url="http://10.10.20.44:4455/")
action_login(emp, _username="shnubbles", _password=" 11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

#13-GIVEN existing username, space after password
beholder = taskman.start_task("record.py")
sleep(0.5)
emp.chrome_run(_url="http://10.10.20.44:4455/")
action_login(emp, _username="shnubbles", _password="11111111 ")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

#14-GIVEN space after existing username, correct password
beholder = taskman.start_task("record.py")
sleep(0.5)
emp.chrome_run(_url="http://10.10.20.44:4455/")
action_login(emp, _username="shewa ", _password="11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

#15-GIVEN space before existing username, correct password
beholder = taskman.start_task("record.py")
sleep(0.5)
emp.chrome_run(_url="http://10.10.20.44:4455/")
action_login(emp, _username=" shewa", _password="11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)

#16-GIVEN arabic characters in username, correct password
# beholder = taskman.start_task("record.py")
# sleep(0.5)
# emp.chrome_run(_url="http://10.10.20.44:4455/")
# action_login(emp, _username="shewaعربي", _password="11111111")
# action_logout(emp)
# taskman.kill_task(beholder, _delay=2)

#17-GIVEN existing username, correct password
beholder = taskman.start_task("record.py")
sleep(0.5)
emp.chrome_run(_url="http://10.10.20.44:4455/")
action_login(emp, _username="shewa", _password="11111111")
action_logout(emp)
taskman.kill_task(beholder, _delay=2)