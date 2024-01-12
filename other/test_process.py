import cpuinfo
import platform
import wmi
import psutil
import subprocess as sp
import sys



# Listen on stdin.
while True:
    line = sys.stdin.readline()

    if("hello".lower() in line.lower()):
        print("HI THERE")
    if("get_information".lower()):
        print("available RAM:", str(psutil.virtual_memory().available / 1024 / 1024 / 1024)[:4], "/", str(psutil.virtual_memory().total / 1024 / 1024 / 1024)[:4])
        print("CPU Brand:", cpuinfo.get_cpu_info()['brand_raw'])
        print("CPU frequency:", cpuinfo.get_cpu_info()['hz_actual_friendly'])
        # print("CPU usage:", psutil.cpu_percent())
        for card in wmi.WMI().Win32_VideoController():
            print(f"GPU {wmi.WMI().Win32_VideoController().index(card)}:", card.Caption )
        if(sp.PIPE):
            print("output:", sp.PIPE)
        break
    else:
        print("I did not get any messages.")
    # Check if the end of the file has been reached.
    if not line:
        break
