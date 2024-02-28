import win32gui
import win32con
import win32api

def create_transparent_window(title, width, height):
    # Define window class
    wc = win32gui.WNDCLASS()
    wc.hInstance = win32gui.GetModuleHandle(None)
    wc.lpszClassName = 'MyTransparentWindow'
    wc.lpfnWndProc = {win32con.WM_DESTROY: lambda h, m, w, l: win32gui.PostQuitMessage(0)}

    # Register window class
    class_atom = win32gui.RegisterClass(wc)

    # Create window
    style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
    ex_style = win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT | win32con.WS_EX_TOPMOST
    hwnd = win32gui.CreateWindowEx(
        ex_style,
        class_atom,
        title,
        style,
        0, 0, width, height,
        0, 0, wc.hInstance, None)

    # Set transparency (alpha=0: fully transparent, alpha=255: fully opaque)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0,0,0), 200, win32con.LWA_ALPHA)

    # Show window
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    win32gui.UpdateWindow(hwnd)

    # Create button as a separate top-level window
    button_style = win32con.WS_VISIBLE | win32con.BS_PUSHBUTTON
    button = win32gui.CreateWindow(
        'Button',
        'My Button',
        button_style,
        10, 10, 100, 30,
        None, None, wc.hInstance, None)

    # Make button always on top
    win32gui.SetWindowPos(button, win32con.HWND_TOPMOST, 0, 0, 0, 0,
        win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)

    # Enter message loop
    win32gui.PumpMessages()

create_transparent_window('Transparent Click-Through Window', 800, 600)