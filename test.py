from emploid import Emploid
from api import API
from time import sleep
from load_elements import *

emp = Emploid()
emp.set_failsafe(False)
emp.set_delay(0.2)
show = emp.show
show("started")

# def func_(emp):
#     elm = emp.locate(element_windows_btn, _confidence=0.9)
#     sleep(1)
#     if(elm):
#         print("detected test element")
#         emp.click(elm)
#     else:
#         print("could not detect test element")
# emp.promise(_func=func_, _tooltip="click on windows button")

img = emp.import_image("elm2.png")

elm = emp.locate(img, _confidence=0.6)

if(emp):
    emp.moveto(elm)
    emp.click(elm)
else:
    print("could not detect element")