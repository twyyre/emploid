from constants import *
from driver import init_emploid
from emploid.emploid import Emploid


emp = Emploid(SETTINGS_USE_SELENIUM)
emp.get("https://google.com")
