import win32gui, win32ui
from win32api import GetSystemMetrics

dc = win32gui.GetDC(0)
dcObj = win32ui.CreateDCFromHandle(dc)
hwnd = win32gui.WindowFromPoint((0,0))
monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))

while True:
    m = win32gui.GetCursorPos()
    dcObj.Rectangle((m[0], m[1], m[0]+30, m[1]+30))
    win32gui.InvalidateRect(hwnd, monitor, True) # Refresh the entire monitor