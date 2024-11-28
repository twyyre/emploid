import subprocess as sp
import sys
from time import sleep

class Taskman:
    def __init__(self):
        self.tasks = []

    def start_task(self, _taskname, _testcasename=""):

        SW_STATE = 6 #zero is headless, one is normal, six is minimized
        
        cf = sp.CREATE_NEW_CONSOLE
        # cf = sp.CREATE_NO_WINDOW

        info = sp.STARTUPINFO()
        info.dwFlags = sp.STARTF_USESHOWWINDOW
        info.wShowWindow = SW_STATE

        task = sp.Popen(
            [sys.executable, _taskname], 
            # creationflags=sp.CREATE_NEW_CONSOLE,
            creationflags=cf,
            startupinfo=info
            # stdin=sp.PIPE,
            # stdout=sp.PIPE,
            # stderr=sp.PIPE
        )

        self.tasks.append(task)
        return self.tasks[-1]
    
    def start_func(self, _func):
        pass
    
    def thread_create(self, _func, *args):
        import threading
        return threading.Thread(target=_func, args=args)
    
    def thread_start(self, _thread):
        _thread.start()

    def thread_wait(self, _thread):
        return _thread.join()
    
    def kill_task(self, _task, _delay=0):
        sleep(_delay)
        _task.kill()