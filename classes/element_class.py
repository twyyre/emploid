from constants import SETTINGS_USE_APPIUM
from emploid import Emploid
class EmploidElement:
    def __init__(self, _driver, _locator):
        self.locator = _locator