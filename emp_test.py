from emploid import Emploid
from api import API
from time import sleep
from load_elements import *

import logging
logging.basicConfig(level=logging.INFO, filename="log_file.log")
logging.info("The application is running task number 5")

emp = Emploid()

emp.show("started")

# conf=0.3799999999999999

emp.chrome_run(_url="http://10.10.20.45:8001/app")

# # emp.input_into("shewa", element_username_input, _confidence=conf, _delay=1)
# # emp.input_into("11111111", element_password_input, _confidence=conf, _delay=1)
# # emp.click(element_signin_btn, _confidence=conf, _delay=1)

# # emp.load_elements()

# emp.click(element_windows_btn)


