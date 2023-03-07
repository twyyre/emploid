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
    return f" {datetime.date.today().year}-{datetime.date.today().month}-{datetime.date.today().day}-{datetime.datetime.now().hour}-{datetime.datetime.now().minute}-{datetime.datetime.now().second}"
