from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.button = QPushButton("Open New Window", self)
        self.button.clicked.connect(self.open_new_window)
        self.setCentralWidget(self.button)

    def open_new_window(self):
        self.new_window = NewWindow()
        self.new_window.show()

class NewWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Window")

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()