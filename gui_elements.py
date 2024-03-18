import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRubberBand
from PyQt5.QtCore import Qt, QRect, QPoint, QSize, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QIcon, QGuiApplication

from PIL import ImageQt

from ocr_tts import Reader


class MainWindow(QWidget):
    zone_set = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.zonemanager = ZoneManager()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setGeometry(QRect(100, 100, 300, 200))
        # self.setAttribute(Qt.WA_TranslucentBackground)
        

        settings = QPushButton('Settings', self)
        settings.setGeometry(QRect(10, 10, 80, 30))
        settings.setToolTip('[<b>PLACEHOLDER<b>]')
        settings.clicked.connect(self.function1)

        quit = QPushButton('Quit', self)
        quit.setGeometry(QRect(110, 10, 80, 30))
        quit.setToolTip('[PLACEHOLDER]')
        quit.clicked.connect(self.close_application)

        set_zone = QPushButton('Set Zone', self)
        set_zone.setGeometry(QRect(10, 60, 80, 30))
        set_zone.setToolTip('[PLACEHOLDER]')
        set_zone.clicked.connect(self.start_snipping)

        quick_read = QPushButton('Quick Read', self)
        quick_read.setGeometry(QRect(110, 60, 80, 30))
        quick_read.setToolTip('[PLACEHOLDER]')
        quick_read.clicked.connect(self.function2)

        showhide = QPushButton('Show / Hide Zones', self)
        showhide.setGeometry(QRect(10, 120, 120, 30))
        showhide.setToolTip('[PLACEHOLDER]')
        showhide.clicked.connect(self.function2)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.m_drag:
            self.move(event.globalPos() - self.m_DragPosition)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.m_drag = False

    # Zone selector functions
    def start_snipping(self):
        self.snip_widget = ZoneSelector()
        self.snip_widget.showFullScreen()
        # self.snip_widget.zone_set.connect(self.get_zone_coordinates)
        self.snip_widget.zone_set.connect(self.spawn_zone)

    def spawn_zone(self):
        zone_coordinates = self.snip_widget.rect_coordinates
        zone_coordinates = (zone_coordinates.x(), zone_coordinates.y(), zone_coordinates.width(), zone_coordinates.height())
        self.zonemanager.create_zone_package(zone_coordinates)

    def _get_zone_coordinates(self):
        self.zone = self.snip_widget.rect_coordinates
        self.zone_box = ZoneBorder(self.zone.x(), self.zone.y(), self.zone.width(), self.zone.height())
        self.zone_box.show()
        # print(self.zone)
        self.zone_set.emit()

    def close_application(self):
        QApplication.quit()
    

    def function1(self):
        # Placeholder for your function 1
        pass

    def function2(self):
        # Placeholder for your function 2
        pass


class ZoneSelector(QWidget):
    zone_set = pyqtSignal()

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
            # print(self.rect_coordinates)
            self.close()
            self.zone_set.emit()


class ZoneManager:

    def __init__(self):
        self.zone_list = []

    def create_zone_package(self, zone_coordinates):
        self.determine_zone_clash()
        zone_package = ZonePackage(zone_coordinates)
        zone_package.show()
        self.zone_list.append(zone_package)

    def determine_zone_clash(self):
        pass


class ZonePackage:
    DISTANCE = 70

    def __init__(self, zone_coordinates: tuple):
        self.zone = ZoneBorder(zone_coordinates)
        # controls_coordinates = self.calculate_controls_spawn_location(zone_coordinates)
        controls_coordinates = self._simple_controls_location(zone_coordinates)
        self.controls = ZoneControls(controls_coordinates, zone_coordinates)

    def _simple_controls_location(self, zone_coordinates):
        x, y, w, h = zone_coordinates
        X = x
        Y = y - self.DISTANCE
        return (X, Y)

    def calculate_controls_spawn_location(self, zone_coordinates):
        screen = QGuiApplication.primaryScreen()
        screen_rect = screen.geometry()
        _, _, W, H = screen_rect
        x, y, w, h = zone_coordinates
        # TOP, BOTTOM, LEFT, RIGHT spawn logic
        return

    def show(self):
        self.zone.show()
        self.controls.show()

    def destroy(self):
        pass


class ZoneBorder(QWidget):
    def __init__(self, zone_coordinates):
        super().__init__()
        self.x, self.y, self.w, self.h = zone_coordinates
        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_TranslucentBackground)  # Transparent background
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)  # No title bar, always on top
        self.setAttribute(Qt.WA_TransparentForMouseEvents)  # Make window click-through
        self.setGeometry(self.x, self.y, self.w, self.h)  # Position and size

    def paintEvent(self, event=None):
        painter = QPainter(self)
        # Draw a green border without filling the center
        painter.setPen(QColor(0, 255, 0))  # Green color
        painter.setBrush(Qt.transparent)  # No fill
        border_width = 10
        painter.drawRect(border_width // 2, border_width // 2, self.w - border_width, self.h - border_width)  # Adjusted for border width


class ZoneControls(QWidget):
    def __init__(self, spawn_coordinates, zone_coordinates):
        super().__init__()
        self.x, self.y = spawn_coordinates
        self.reader = Reader(zone_coordinates)
        self.initScreen()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Tool | Qt.FramelessWindowHint)  # Always on top, no title bar
        self.setGeometry(self.x, self.y, 100, 50)  # Position and size, adjusted to appear near the first window
        
        self.play_pause = QPushButton(self)
        self.play_pause.setIcon(QIcon('assets/play-icon.png'))
        self.play_pause.setGeometry(QRect(10, 10, 30, 30))
        self.play_pause.setIconSize(QSize(16,16))
        self.play_pause.clicked.connect(self.play_button_rotation)
        self.play_pause.setToolTip('[<b>PLACEHOLDER<b>]')
        # btn.resize(btn.sizeHint())
        # btn.move(0, 0)  # Position inside the button window

        # self.add_stop = QPushButton('Add to Queue', self)
        # self.add_stop.clicked.connect(self.stop_button_rotation)

        # self.add_stop = QPushButton('Remove Zone', self)
        # self.add_stop.clicked.connect(self.remove_zone)
        
    def initScreen(self, zone_coordinates):
        self.screen = app.primaryScreen()
        self.x, self.y, self.w, self.h = zone_coordinates
        
    def play_button_rotation(self):
        if self.play_pause.text() == 'Play':
            self.play()
            self.play_pause.setText('Pause')
            self.add_stop.setText('Stop')
        else:
            self.pause()
            self.play_pause.setText('Play')
            self.add_stop.setText('Add to Queue')

    def screenshot(self):
        screenshot = self.screen.grabWindow(0, self.x, self.y, self.w, self.h)
        screenshot = ImageQt.fromqpixmap(screenshot)
        return screenshot

    def play(self):
        screenshot = self.screenshot()
        self.reader.play(screenshot)

    def pause(self):
        self.reader.pause()
    
    def stop_button_rotation(self):
        pass

    def remove_zone(self):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())