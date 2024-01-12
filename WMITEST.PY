import wmi
import os
import sys
import cpuinfo as cinfo
import socket as sk
import platform as plt
import subprocess as sp
from time import sleep

cf = sp.CREATE_NEW_CONSOLE
SW_STATE = 1 #zero is headless, one is normal, six is minimized
info = sp.STARTUPINFO()
info.dwFlags = sp.STARTF_USESHOWWINDOW
info.wShowWindow = SW_STATE

c = wmi.WMI()

# processes = c.Win32_process()

# for process in processes:
#     # print(processes.index(process), process.name, process.id)
#     if("joplin".lower() in process.name.lower()):
#         os.kill(process.processid, 1)
#         print("joplin process killed")

process = sp.Popen(
    [sys.executable, r"test_process.py"], 
    startupinfo=info, 
    creationflags=sp.CREATE_NEW_CONSOLE, 
    stdout=sp.PIPE,
    stdin=sp.PIPE,
    stderr=sp.PIPE
)

# process = sp.run(
#     [sys.executable, r"test_process.py"], 
#     startupinfo=info, 
#     creationflags=sp.CREATE_NEW_CONSOLE, 
#     stdout=sp.PIPE, 
#     stdin=sp.PIPE, 
#     stderr=sp.PIPE
#     )
# process.stdin.write("hello world".encode())
# process.stdin.flush()
stdout, stderr = process.communicate("get_information".lower().encode())#"Hello World".encode())
print(stdout.decode('utf-8')) 

# result = str(process.communicate('message'.encode()))
# print("result:", str(result))
# 