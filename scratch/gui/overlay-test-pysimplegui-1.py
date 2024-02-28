import PySimpleGUI as sg

def create_transparent_window(title, width, height):
    # Create main transparent window
    layout = [[sg.Text('', size=(width, height))]]
    window = sg.Window(title, layout, alpha_channel=0.5, no_titlebar=True, grab_anywhere=True)

    # Create border window
    border_layout = [[sg.Text('', size=(width+2, height+2))]]  # Adjust size to create a border effect
    border_window = sg.Window(title, border_layout, alpha_channel=1, no_titlebar=True, grab_anywhere=True)

    # Position windows
    border_window.finalize()
    window.finalize()
    border_window.move(-8, -8)  # Adjust position to create a border effect
    window.move(0, 0)

    # Event loop
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

    window.close()
    border_window.close()

create_transparent_window('Transparent Click-Through Window', 80, 60)