#INTERNAL IMPORTS
from emploid.constants import *
from emploid.configs import determine_driver_type

# #SELENIUM IMPORTS
from selenium import webdriver as SeleniumDriver
from selenium.webdriver.support import expected_conditions as SeleniumConditions
from selenium.webdriver.support.ui import WebDriverWait as SeleniumWait
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.remote_connection import ChromeRemoteConnection
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By as SeleniumBy
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import Select #used to deal with select HTML elements
import selenium.common.exceptions

#PYTHON LIBRARY IMPORTS
import re

def init_emploid_driver(_driver_type):

    parent_driver = determine_driver_type(_driver_type)

    class EmploidDriver(parent_driver):
        """This is the driver class for Emploid which makes sure to handle the different drivers for different platforms and exposes suitable methods to be used in the emploid class."""

        def __init__(
                self, 
                _driver_type=_driver_type, 
                _headless=False, 
                _incognito=False, 
                _vpn=None, 
                _browser_type=None, 
                _maximized=False, 
                _window_size=(500, 800), 
                _window_width=None, 
                _window_height=None,
                _auto_connect=False
            ):
            super().__init__()
            self.driver_type = _driver_type
            self.headless = _headless
            self.incognito = _incognito
            self.vpn = _vpn
            self.browser_type = _browser_type
            self.browser = self.determine_browser()
            self.maximized = _maximized
            self.browser_language="en-US"
            self.window_size = _window_size
            self.window_width = _window_width if _window_width else _window_size[0]
            self.window_height = _window_height if _window_height else _window_size[1]
            self.auto_connect = _auto_connect
            
            #APPIUM CONNECT--------------------------------------------
            if(self.auto_connect and self.driver_type==SETTINGS_USE_APPIUM):
                self.appium_connect() #should be migrated to driver class
            #----------------------------------------------------------
        
        def set_driver_type(self, _driver_type):
            self.driver_type = _driver_type
            return self
        def set_headless(self):
            self.headless = True
            return self
        def set_incognito(self):
            self.incognito = True
            return self
        def set_vpn(self):
            self.vpn = True
            return self
        def set_browser_type(self, _type):
            self.browser_type = _type
            return self
        def set_browser(self, _browser_type):
            self.browser = self.determine_browser(_browser_type)
            return self
        def set_maximize(self):
            self.maximized = True
            return self
        def set_browser_language(self, _lang):
            self.browser_language = _lang
            return self
        def set_window_size(self, _size):
            self.window_size = _size
            return self
        def set_window_width(self, _width):
            self.window_width = _width
            return self
        def set_window_height(self, _height):
            self.window_height = _height
            return self
        
        def back(self):
            method = self.determine_method(self.back)
            method()
            
        def get_by(self):
            return SeleniumBy
            
        def determine_method(self, _method1=None, _method2=None, _method3=None):
            if(self.driver_type==SETTINGS_USE_SELENIUM):
                if(_method1 != None):
                    return _method1
            elif(self.driver_type==SETTINGS_USE_APPIUM):
                if(_method2 != None):
                    return _method2
            elif(self.driver_type==SETTINGS_USE_PYAUTOGUI):
                if(_method3 != None):
                    return _method3
            
        def define_element(self, _ent):
            if(self.driver_type==SETTINGS_USE_PYAUTOGUI):
                is_element = isinstance(_ent, self.np.ndarray)
                if(not is_element):
                    print(f"entity {_ent} is not an element of type {self.np.ndarray}")
                return  self.pa.locateOnScreen(_ent) if is_element else None
            
            elif(self.driver_type==SETTINGS_USE_SELENIUM):
                from selenium.webdriver.remote.webelement import WebElement
                is_element = isinstance(_ent, WebElement)

            elif(self.driver_type==SETTINGS_USE_APPIUM):
                from appium.webdriver.webelement import WebElement
                is_element = isinstance(_ent, WebElement)
            
            return is_element
        
        def get_chrome_version(self, _filename):
            """gets version of chrome on the machine in windows"""
            from win32com.client import Dispatch
            filename = _filename
            parser = Dispatch("Scripting.FileSystemObject")
            try:
                version = parser.GetFileVersion(filename)
            except Exception:
                return None
            return version
        
        def install_chromedriver(self):
            """Check if chromedriver is installed, and if not, install a version that is suitable with the current browser version."""
            try:
                version = None
                paths = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
                version = list(filter(None, [self.get_chrome_version(p) for p in paths]))[0]
                return version
            except Exception as e:
                return e
        
        def determine_browser(self, _browser_type=None):
            """decides the browser to use and setup its configurations."""
            browser_type = _browser_type if _browser_type else self.browser_type
            try:
                if(browser_type==BROWSER_TYPE_CHROME):

                    #automatically update chromedriver
                    print("Checking for Chromedriver updates...")
                    self.install_chromedriver()
                    
                    if platform.system()=="Windows":
                        
                        from subprocess import CREATE_NO_WINDOW
                        # self.driver_path = "drivers/chromedriver.exe"
                        # print("chromedriver path:", self.driver_path )
                        self.service = Service()#executable_path=self.driver_path)#self.file_path+'..\s_py.exe') 
                        self.service.creationflags = CREATE_NO_WINDOW

                    #chrome options set up  --------------------------------------------------------------------------
                    self.chrome_options = chromeOptions()
                    # chrome_options.add_argument("user-data-dir=C:\\Users\\Zarqa Alyamama-2021\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

                    #run in incognito browser window---------------------------
                    if(self.incognito):
                        self.chrome_options.add_argument("--incognito")
                        print("running in INCOGNITO mode")
                    #----------------------------------------------------------

                    #whether to run in headless mode or with visible browser window
                    if(self.headless):
                        self.chrome_options.add_argument("--headless")
                        print("running in HEADLESS mode")
                    #----------------------------------------------------------
                    
                    self.chrome_options.add_argument(f"--lang={self.browser_language}") #make sure browser language is english so that text is recognized
                    if(self.maximized):
                        self.chrome_options.add_argument("--start-maximized")
                    else:
                        self.chrome_options.add_argument(f"--window-size={self.window_width},{self.window_height}") #set window size
                        
                    self.chrome_options.add_argument('--disable-gpu')  # og comment : Last I checked this was necessary.
                    # self.chrome_options.add_argument("--no-sandbox")
                    # self.chrome_options.add_argument('--window-position=400,000') #set window position on screen
                    # self.chrome_options.add_argument("--useAutomationExtension=false")
                    # self.chrome_options.add_argument("--enable-automation")
                    # self.chrome_options.add_argument("--test-type=browser")
                    # self.chrome_options.add_argument("--disable-plugins")
                    # self.chrome_options.add_argument("--disable-infobars")
                    self.chrome_options.add_argument("--extensions_install_verfication=false")
                    # self.chrome_options.add_argument("--disable_extensions=true")
                    #-----------------------------------------------------------------------------------------------

                    #USER PROFILE (CHROME):
                    if(BROWSER_USE_PROFILE and self.user_profile != None):
                        print("LOAD USER PROFILE")
                        # if(self.email):
                        #     # print("email is true")
                        #     # input()
                        #     user_profile = "lypybot_"+str(self.email)
                        # else:
                        #     user_profile = self.user_profile 
                        # print("user profile:", user_profile)
                        # # input()
                        user_profile = "lypybot_"+str(self.email)
                        self.chrome_options.add_argument(f"user-data-dir=C:\\Users\\lypybot\\AppData\\Local\\Google\\Chrome\\User Data\\{user_profile}") #will make a program that automatically deletes user profiles later
                        
                    if(self.vpn):

                        try:
                            extension_name = "freevpnExtension"
                            self.chrome_options.add_extension(f"extensions/{extension_name}.crx")
                            self.vpn_loaded = True
                            print("freevpnExtension loaded")
                            
                        except Exception as e:
                            self.vpn_loaded = False
                            print(e)

                    #----------------------------------------------------------
                    if platform.system() == "Linux":
                        raise Exception("LINUX is not supported at the moment.")
                        print("\n set to linux driver")
                        # self.driver = webdriver.Chrome(service= self.service, options= self.chrome_options, executable_path=os.environ.get("CHROMEDRIVER_PATH"))
                        self.driver = SeleniumDriver.Chrome()
                        
                    if platform.system() == "Windows":
                        print("set to windows driver.")
                        return SeleniumDriver.Chrome(options=self.chrome_options, service=self.service)
                    #----------------------------------------------------------

                elif(browser_type==BROWSER_TYPE_TOR):
                    raise Exception("TOR browser is not supported at the moment.")
                    print("USING TOR BROWSER")
                    #TOR BROWSER EXAMPLE
                    from selenium import webdriver
                    from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
                    from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

                    # binary = FirefoxBinary(r"C:\Users\<Windows User>\Desktop\Tor Browser\Browser\firefox.exe")
                    # profile = FirefoxProfile(r"C:\Users\<Windows User>\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")

                    # driver = webdriver.Firefox(profile, binary)
                    # driver.get("http://stackoverflow.com")

                elif(browser_type==BROWSER_TYPE_FIREFOX):
                    raise Exception("FIREFOX is not supported at the moment.")
                    print("USING FIREFOX BROWSER")
                    from subprocess import CREATE_NO_WINDOW
                    self.service = Service(getcwd()+"//drivers//geckodriver.exe") 
                    self.service.creationflags = CREATE_NO_WINDOW

                    #firefox options set up
                    self.firefox_options = FirefoxOptions()

                    #firefox preference reference http://kb.mozillazine.org/Category:Preferences
                    #firefox vepn extension https://addons.mozilla.org/en-US/firefox/addon/veepn-free-fast-security-vpn/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search

                    #run in incognito browser window
                    if(self.incognito):
                        self.firefox_options.add_argument("--incognito")

                    #whether to run in headless mode or with visible browser window
                    if(self.headless):
                        self.firefox_options.add_argument("--headless")

                    # self.firefox_options.set_preference("Browser.display.screen resolution", -1)
                    self.firefox_options.add_argument("--width=450")
                    self.firefox_options.add_argument("--height=600")

                    from selenium import webdriver
                    from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
                    from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

                    # binary = FirefoxBinary(r"C:\Users\<Windows User>\Desktop\Tor Browser\Browser\firefox.exe")

                    self.firefox_profile = FirefoxProfile(getcwd()+f"/fbb_data/browser_profiles/firefox/profile.default")#r"C:\Users\hp\AppData\Roaming\Mozilla\Firefox\Profiles")
                    self.firefox_binary = FirefoxBinary()

                    # Ensure mobile-friendly view for parsing
                    useragent = "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36"

                    firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
                    firefox_capabilities['marionette'] = True

                    #Firefox
                    self.firefox_profile.set_preference("general.useragent.override", useragent)

                    self.firefox_profile.DEFAULT_PREFERENCES["frozen"]["browser.link.open_newwindow"] = 3 #this fixes new tabs opening as new windows when using firefox profiles
                    self.driver = webdriver.Firefox(firefox_profile=self.firefox_profile, firefox_binary=self.firefox_binary, options=self.firefox_options)

                    try:
                        self.driver.install_addon(getcwd()+"/fbb_data/extensions/freevpnExtension.xpi", temporary=False)
                        self.vpn_loaded = True
                    except Exception as e:
                        print(e)
                        pause()

                    # self.driver.set_window_size(self.window_width, self.window_height)

            except selenium.common.exceptions.SessionNotCreatedException as e:
                print("Driver error:", e)

            return self
        
        def determine_entity(self, _ent):
            # Check if it's a package name
            if '.' in _ent:
                return ENTITY_TYPE_PACKAGE
            
            # Check if it's an XPath expression
            elif re.match(r'^//', _ent):
                return ENTITY_TYPE_XPATH
            
            # Check if it's a CSS selector
            elif re.match(r'^[.#]?[-_a-zA-Z0-9]+', _ent):
                return ENTITY_TYPE_CSS_SELECTOR
            
            return None
        
        def maximize_browser_window(self):
            return self.maximize_window()
            
        def minimize_browser_window(self):
            return self.minimize_window()
            
            
    return EmploidDriver()
