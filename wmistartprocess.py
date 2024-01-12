import wmi, time
ip = '10.101.120.10'
SW_SHOWNORMAL = 1
from socket import *
print("Establishing connection to %s" %ip)
c = wmi.WMI(ip)
process_startup = c.Win32_ProcessStartup.new()
process_startup.ShowWindow = SW_SHOWNORMAL
process_id, result = c.Win32_Process.Create(CommandLine=r"C:\Users\a.almuntasir\Desktop\77873819-c6df-4048-b428-f3c0f45e00c6.png", ProcessStartupInformation=process_startup)
if result == 0:
  print("Process started successfully: %d" % process_id)
else:
  raise RuntimeError("Problem creating process: %d" % result)