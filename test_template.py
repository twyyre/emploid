from emploid import Emploid
from api import API
from time import sleep
from load_elements import *
from random import randint
emp = Emploid()

from modules.taskman.taskman import Taskman
testman = Taskman()

def func_(_name):
    sleep(randint(0, 2))
    print(f"hello {_name}")

for i in range(0, 5):
    thread = testman.thread_create(func_, "ayoub")
    testman.thread_start(thread)

emp.set_failsafe(False)
# emp.set_delay(0.2)
show = emp.show
show("started")

# #Activating and deactivating users proved to be a little complicated. There are two possible scenraios and that makes the ability to grab all elements into a list and choose the first element obsolete. We can't determine which type of element came first in the list, therefore I'm going to have to figure out how to look for an element in a certain part of the screen rather than its entirety.

# def func_(emp):
#     emp.chrome_run(_url="http://10.10.20.44:4455/", _maximized=False)
# emp.promise(_func=func_, _tooltip="open chrome window")

# from actions.action_login import action_login
# from actions.action_search_user import action_search_user
# from actions.action_activate_user import action_activate
# from actions.action_logout import action_logout

# action_login(emp, _username="shewa", _password="11111111")
# action_search_user(emp, _username="ayoub")
# action_activate(emp)
# # action_logout(emp)

show("FINISHED")
