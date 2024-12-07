import logging
from random import randint
from time import sleep
       
def pause():
    input("press any key to continue...")

def f_write(_filename, _content, _encoding="utf-8-sig"):
    with open(_filename, "w", encoding=_encoding) as file:
        file.write(str(_content))

def f_append(filename, content, encoding="utf-8-sig"):
    with open(filename, "a", encoding=encoding) as file:
        file.write(str(content))

def f_read(filename, encoding="utf-8-sig"):
    with open(filename, "r", encoding=encoding) as file:
        content = file.read()
    return content

def f_read_int(filename):
    with open(filename, "r") as file:
        content = int(file.read())
    return content

def f_read_once(filename):
    with open(filename, "r") as file:
        content = file.read()
    return content

def f_read_lines(filename):
    with open(str(filename)) as file:
        lines = file.readlines()
        for line in lines:
            lines[lines.index(line)] = line.replace("\n", "")
    return lines

def get_time(arg=None):
    import datetime
    return f" {datetime.date.today().year}-{datetime.date.today().month}-{datetime.date.today().day}-{datetime.datetime.now().hour}-{datetime.datetime.now().minute}-{datetime.datetime.now().second}"

def log(*args, _heading=False):
    logging.debug(*args)
    if(_heading):
        print()
        print("----------------", *args, "----------------")
        print()
    else:
        print("--------", *args)

def wait(_seconds):
    i = 0
    while i < _seconds:
        log(f"waiting...({i})")
        sleep(1)
        i+=1

def get_builtins():
    import builtins
    return dir(builtins)

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

    

