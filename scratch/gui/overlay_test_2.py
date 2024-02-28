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

    # Create border window
    border_style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
    border_ex_style = win32con.WS_EX_LAYERED | win32con.WS_EX_TOPMOST
    border_hwnd = win32gui.CreateWindowEx(
        border_ex_style,
        class_atom,
        title,
        border_style,
        -8, -8, width+16, height+16,  # Adjust size and position to create a border effect
        0, 0, wc.hInstance, None)
    win32gui.SetLayeredWindowAttributes(border_hwnd, win32api.RGB(0,0,0), 255, win32con.LWA_ALPHA)  # Fully opaque

    # Create main transparent window
    main_style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
    main_ex_style = win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT | win32con.WS_EX_TOPMOST
    main_hwnd = win32gui.CreateWindowEx(
        main_ex_style,
        class_atom,
        title,
        main_style,
        0, 0, width, height,
        0, 0, wc.hInstance, None)
    win32gui.SetLayeredWindowAttributes(main_hwnd, win32api.RGB(0,0,0), 200, win32con.LWA_ALPHA)  # Semi-transparent

    # Show windows
    win32gui.ShowWindow(border_hwnd, win32con.SW_SHOW)
    win32gui.ShowWindow(main_hwnd, win32con.SW_SHOW)
    win32gui.UpdateWindow(border_hwnd)
    win32gui.UpdateWindow(main_hwnd)

    # Enter message loop
    win32gui.PumpMessages()

create_transparent_window('Transparent Click-Through Window', 800, 600)