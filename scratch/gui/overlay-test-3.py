import win32gui
import win32con
import win32api

wc = win32gui.WNDCLASS()
wc.hInstance = win32gui.GetModuleHandle(None)
wc.lpszClassName = 'MyWindowClass'
wc.lpfnWndProc = message_map