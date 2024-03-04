from PyQt5.QtWidgets import QApplication
from gui_elements import MainWindow, ZoneBorder, ZoneControls
import sys

def main():
    def test_print_zone():
        print(window.zone)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


def upon_launch():
    # Intro screen
    # choose the TTS option:
    # if Azure then choose voice and login
    # if free then choose option
    pass


if __name__ == '__main__':
    main()