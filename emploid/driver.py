from emploid.constants import *
from emploid.configs import determine_driver_type

def init_emploid_driver(_driver_type):

    driver_type = determine_driver_type(_driver_type)

    class EmploidDriver(driver_type):

        def __init__(self, _driver_type=None, _headless=None, _incognito=None, _vpn=None, _browser_type=None):
            super().__init__()
            self.driver_type = _driver_type
            self.headless = _headless
            self.incognito = _incognito
            self.vpn = _vpn
            self.browser_type = _browser_type
            self.driver = self
            self.browser = self.determine_browser() 
        
        def determine_browser(self):
            import selenium.common.exceptions

            try:
                
                if(self.browser_type==BROWSER_TYPE_CHROME):

                    #automatically update chromedriver
                    # self.show("Checking for Chromedriver updates...")

                    # try:
                    #     import chromedriver_autoinstaller
                    #     chromedriver_autoinstaller.install()
                    # except Exception as e:
                    #     print("could not check for chromedriver updates.")
                    
                    if platform.system()=="Windows":
                        
                        from subprocess import CREATE_NO_WINDOW
                        # self.driver_path = "drivers/chromedriver.exe"
                        # self.show("chromedriver path:", self.driver_path )
                        self.service = Service()#executable_path=self.driver_path)#self.file_path+'..\s_py.exe') 
                        self.service.creationflags = CREATE_NO_WINDOW

                    #chrome options set up  --------------------------------------------------------------------------
                    self.chrome_options = chromeOptions()
                    # chrome_options.add_argument("user-data-dir=C:\\Users\\Zarqa Alyamama-2021\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

                    #run in incognito browser window---------------------------
                    if(self.incognito):
                        self.chrome_options.add_argument("--incognito")
                        self.show("incognito mode activated")
                    #----------------------------------------------------------


                    #whether to run in headless mode or with visible browser window
                    if(self.headless):
                        self.chrome_options.add_argument("--headless")
                        self.show("incognito mode activated")

                    #----------------------------------------------------------
                    

                    self.chrome_options.add_argument('--disable-gpu')  # og comment : Last I checked this was necessary.
                    # self.chrome_options.add_argument("--no-sandbox")
                    self.chrome_options.add_argument("--lang=en-US") #make sure browser language is english so that text is recognized
                    self.chrome_options.add_argument(f"--window-size={self.window_width},{self.window_height}") #set window size
                    self.chrome_options.add_argument('--window-position=400,000') #set window position on screen
                    # self.chrome_options.add_argument("--useAutomationExtension=false")
                    # self.chrome_options.add_argument("--enable-automation")
                    # self.chrome_options.add_argument("--test-type=browser")
                    # self.chrome_options.add_argument("--disable-plugins")
                    # self.chrome_options.add_argument("--disable-infobars")
                    self.chrome_options.add_argument("--extensions_install_verfication=false")
                    # self.chrome_options.add_argument("--disable_extensions=true")
                    #-----------------------------------------------------------------------------------------------


                    #USER PROFILE (CHROME):
                    # self.user_profile = True
                    # if(self.user_profile != False and self.user_profile != None):

                    
                    #     self.show("LOAD USER PROFILE")

                    #     # if(self.email):
                    #     #     # print("email is true")
                    #     #     # input()
                    #     #     user_profile = "lypybot_"+str(self.email)
                    #     # else:
                    #     #     user_profile = self.user_profile 
                        
                    #     # print("user profile:", user_profile)
                    #     # # input()

                    #     user_profile = "lypybot_"+str(self.email)
                    #     self.chrome_options.add_argument(f"user-data-dir=C:\\Users\\lypybot\\AppData\\Local\\Google\\Chrome\\User Data\\{user_profile}") #will make a program that automatically deletes user profiles later
                        
                    if(self.vpn):

                        try:
                            extension_name = "freevpnExtension"
                            self.chrome_options.add_extension(f"extensions/{extension_name}.crx")
                            self.vpn_loaded = True
                            self.show("freevpnExtension loaded")
                            
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

                        self.show("set to windows driver.")
                        return SeleniumDriver.Chrome(options=self.chrome_options, service=self.service)
                    #----------------------------------------------------------

                elif(self.browser_type==BROWSER_TYPE_TOR):
                    raise Exception("tor is not supported at the moment.")
                    print("USING TOR BROWSER")
                    #TOR BROWSER EXAMPLE
                    from selenium import webdriver
                    from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
                    from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

                    # binary = FirefoxBinary(r"C:\Users\<Windows User>\Desktop\Tor Browser\Browser\firefox.exe")
                    # profile = FirefoxProfile(r"C:\Users\<Windows User>\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")

                    # driver = webdriver.Firefox(profile, binary)
                    # driver.get("http://stackoverflow.com")


                elif(self.browser_type==BROWSER_TYPE_FIREFOX):

                    raise Exception("Firefox is not supported at the moment.")
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

                self.show("Driver error")
                self.show(e)

            return self.driver
    return EmploidDriver()
