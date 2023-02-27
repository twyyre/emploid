from random import randint
from time import sleep

from numpy import choose

def loop(self, _func=None, _tooltip="<no tooltip>", _tries=5, _delay=2, _fullerror=True, _noerror=False, _noprint=False):

    show(_tooltip)

    if(_tooltip==""):
        _tooltip="<no tooltip>"

    state = True

    trigger = False

    while ((trigger == False) and (_tries > 0)):

        _tries -= 1

        try:
            _func(self)
            trigger = True
            state = True

        except Exception as e:

            if(_fullerror):
                _str = "\nwith Exception:\n" + str(e)
                pass
            else:
                _str = ""

            if(not _noprint):
                if(_noerror):
                    print(_tooltip)
                else:
                    print(_tooltip + " failed ("+str(_tries)+f". . .) {_str}")

            # self.driver.save_screenshot(self.screenshot_name)
            sleep(_delay)
            state = False
    return state
        

def f_write(_filename, _content, _encoding="utf-8-sig"):
    file = open(_filename, "w", encoding=_encoding)
    file.write(str(_content))
    file.close()

def f_append(filename, content, encoding="utf-8-sig"):
    file = open(filename, "a", encoding=encoding)
    file.write(str(content))
    file.close()

def f_read(filename, encoding="utf-8-sig"):
    file = open(filename, "r", encoding=encoding)
    content = file.read()
    file.close()
    return content

def f_read_int(filename):
    file = open(filename, "r")
    content = int(file.read())
    file.close()
    return content

def f_read_once(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

def f_read_lines(filename):
    file = open(str(filename))
    lines = file.readlines()
    for line in lines:
        lines[lines.index(line)] = line.replace("\n", "")
    return lines

def get_time(arg=None):
    import datetime

    if(arg is None):
        arg = "str"
        
    tyme = datetime.datetime.now()
    tyme_y = tyme.year
    tyme_month = tyme.month
    tyme_d = tyme.day
    tyme_wkd = tyme.strftime("%A") 
    tyme_pa = "AM"
    tyme_h = tyme.hour
    if(tyme_h>12):
        tyme_h -= 12
        tyme_pa = "PM"
    if(tyme_h==0):
        tyme_h = 12

    tyme_m = tyme.minute
    tyme_s = tyme.second

    tyme_str = f"{tyme_h}:{tyme_m}:{tyme_s}{tyme_pa}\n{tyme_y}-{tyme_month}-{tyme_d}\n{tyme_wkd}"

    if arg == "h" : return tyme_h
    if arg == "m" : return tyme_m
    if arg == "s" : return tyme_s
    if arg == "y" : return tyme_y
    if arg == "month" : return tyme_month
    if arg == "d" : return tyme_d
    if arg == "pa" : return tyme_pa
    if arg == "str" : return tyme_str


def act_logIn(driver, username, password):
        
    print("\n------------------------------\nopened website\n------------------------------")
    driver.get("https://mbasic.facebook.com/")

    print("\n------------------------------\nfind the username input element and pass it our username\n------------------------------")
    
    func_ = lambda driver : driver.find_element_by_xpath('//input[@name=\"email\"]')\
        .send_keys(username) #find the username input element and pass it our username
    loop(driver, func_, """find the username input element and pass it our username""")

    print("\n------------------------------\nfind the password input element and pass it our password\n------------------------------")
    
    func_ = lambda driver : driver.find_element_by_xpath('//input[@name="pass"]')\
        .send_keys(password) #find the password input element and pass it our password
    loop(driver, func_, """find the password input element and pass it our password""")

    print("\n------------------------------\nfind the submit button with the submit property and click it\n------------------------------")

    func_ = lambda driver : driver.find_element_by_xpath('//input[@type="submit"]')\
        .click() #find the submit button with the submit property and click it
    loop(driver, func_, """find the submit button with the submit property and click it""")

    print("\n------------------------------\ncheck if logged in successfully\n------------------------------")
    def func_(driver):

        text = driver.find_element_by_xpath("//h3[@class='o']").text

        if "Log in with one tap" in text:
            print("logged in successfully.")

    loop(driver, func_, """check if logged in successfully""")

def highlight(self, elm, color="red"):
    self.driver.execute_script("""
        arguments[0].style.background = arguments[1];
    """, elm, color)

def get_latest_message(self): #deprecated

    from fbb_data.webdriver.common.by import By

    self.msg_list = self.driver.find_elements(By.XPATH, "//div[@class='oo9gr5id ii04i59q']")#"//div[@class='oo9gr5id']")
    
    
    strr = self.driver.execute_script("""
    for(i=0; i<arguments[0].length; i++){
        arguments[0][i].style.background = "red";
    }
    return arguments[0][arguments[0].length -1].innerHTML;
    """, self.msg_list)

    #get message and date of message
    substr = "sent Today at"
    str_index = strr.find(substr)  + len(substr)
    end_index = str_index + 6
    strr = strr.lower()
    return strr#[end_index:len(strr)]

def get_latest_date(self): #deprecated
    if len(self.msg_list) > 0:
        strr = self.driver.execute_script("""
        for(i=0; i<arguments[0].length; i++){
            arguments[0][i].style.background = "red";
        }
        return arguments[0][arguments[0].length -1].textContent;
        """, self.msg_list)
        #get message and date of message
        substr = "sent Today at"
        str_index = strr.find(substr)  + len(substr)
        end_index = str_index + 6
        return strr[str_index:end_index]
       

def send_message(self, stR="!"): #deprecated
    
    from fbb_data.webdriver.common.by import By
    from fbb_data.webdriver.common.keys import Keys
    
    
    self.msg_post_area = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div")
    self.msg_post_area.click()
    self.msg_post_area.send_keys(stR)
    self.msg_post_area.send_keys(Keys.ENTER)

def purify_message(message):
    return message

def randomize_string(strr): 
 
    strr2 = ""
    arr = list(strr)
    arr2 = []

    while (len(arr) > 0):
        # print(arr[len(arr)-1])
        i = randint(0, len(arr)-1)
        arr2.append(arr[i])
        arr.remove(arr[i])
    
    for char in arr2:
        strr2 += char
    
    return strr2
        
def show(_content):
    bar = "\n----------------------------\n"
    print(bar, str(_content), bar)

def random_string(_length=20, _letters=True, _numbers=True, _characters=True):

    letters = "abcdefghijklmnopqrstuvwzyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    characters = "_-.@"

    string = ""

    if(_letters):
        string += letters 

    if(_numbers):
        string += numbers 

    if(_characters):
        string += characters 

    random_str = ""

    while len(random_str) < _length:
        random_str += string[randint(0, len(string)-1)]

    return random_str

    #function from https://www.educative.io/edpresso/how-to-generate-a-random-string-in-python
    
    # import random
    # import string

    # # printing lowercase
    # letters = string.ascii_lowercase
    # print ( ''.join(random.choice(letters) for i in range(10)) )

    # # printing uppercase
    # letters = string.ascii_uppercase
    # print ( ''.join(random.choice(letters) for i in range(10)) )

    # # printing letters
    # letters = string.ascii_letters
    # print ( ''.join(random.choice(letters) for i in range(10)) )

    # # printing digits
    # letters = string.digits
    # print ( ''.join(random.choice(letters) for i in range(10)) )

    # # printing punctuation
    # letters = string.punctuation
    # print ( ''.join(random.choice(letters) for i in range(10)) )

    




    


