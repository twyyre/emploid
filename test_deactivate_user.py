from emploid import Emploid
from api import API
from time import sleep
from load_elements import *

emp = Emploid()
emp.set_failsafe(False)
# emp.set_delay(0.2)
show = emp.show
show("started")

#Activating and deactivating users proved to be a little complicated. There are two possible scenraios and that makes the ability to grab all elements into a list and choose the first element obsolete. We can't determine which type of element came first in the list, therefore I'm going to have to figure out how to look for an element in a certain part of the screen rather than its entirety.

#
def func_(emp):
    emp.chrome_run(_url="http://10.10.20.44:4455/", _maximized=False)
emp.promise(_func=func_, _tooltip="open chrome window")

sleep(2)

#
try:
    import action_login
    pass
except Exception as e:
    print("login action")
    print(e)
    input()
    exit()

#
try:
    import action_search_user
except Exception as e:
    print("add user action")
    print(e)
    input()
    exit()

#
try:
    import action_deactivate_user
except Exception as e:
    print("add user action")
    print(e)
    input()
    exit()

#
try:
    import action_logout
except Exception as e:
    print("add user action")
    print(e)
    input()
    exit()

show("FINISHED")
exit()