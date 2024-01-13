from constants import *
# import subprocess
# import os
# try:
#     # os.system(f"taskkill /im python.exe /f")
#     # os.system(f"taskkill /im py.exe /f")
#     subprocess.Popen(["C:\\Users\\a.almuntasir\\AppData\\Roaming\\npm\\appium.cmd"])
# except Exception as e:
#     print(e)
import subprocess
import os
try:
    # os.system(f"taskkill /im python.exe /f")
    # os.system(f"taskkill /im py.exe /f")
    subprocess.run([APPIUM_PATH])
except Exception as e:
    print(e)
