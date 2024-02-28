from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QRubberBand, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QRect, QPoint, QSize
import sys

class SnipWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowOpacity(0.3)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setCursor(Qt.CrossCursor)
        self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
        self.origin = QPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.origin = event.pos()
            self.rubberBand.setGeometry(QRect(self.origin, QSize()))
            self.rubberBand.show()

    def mouseMoveEvent(self, event):
        if not self.origin.isNull():
            self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.rubberBand.hide()
            self.rect_coordinates = self.rubberBand.geometry()
            print(self.rect_coordinates)
            self.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton('Start Snipping', self)
        self.button.clicked.connect(self.start_snipping)
        self.setCentralWidget(self.button)

    def start_snipping(self):
        self.snip_widget = SnipWidget()
        self.snip_widget.showFullScreen()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())