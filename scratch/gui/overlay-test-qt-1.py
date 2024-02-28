import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QColor

def test_print():
    print("complete")

class TransparentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_TranslucentBackground)  # Transparent background
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # No title bar, always on top
        self.setAttribute(Qt.WA_TransparentForMouseEvents)  # Make window click-through
        self.setGeometry(100, 100, 400, 400)  # Position and size

    def paintEvent(self, event=None):
        painter = QPainter(self)
        # Draw a green border without filling the center
        painter.setPen(QColor(0, 255, 0))  # Green color
        painter.setBrush(Qt.transparent)  # No fill
        border_width = 10
        painter.drawRect(border_width // 2, border_width // 2, 400 - border_width, 400 - border_width)  # Adjusted for border width

class ButtonWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Tool | Qt.FramelessWindowHint)  # Always on top, no title bar
        self.setGeometry(510, 150, 100, 50)  # Position and size, adjusted to appear near the first window
        
        btn = QPushButton('Test', self)
        btn.clicked.connect(test_print)
        btn.resize(btn.sizeHint())
        btn.move(0, 0)  # Position inside the button window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    transWindow = TransparentWindow()
    buttonWindow = ButtonWindow()
    
    # Show windows
    transWindow.show()
    buttonWindow.show()

    sys.exit(app.exec_())
