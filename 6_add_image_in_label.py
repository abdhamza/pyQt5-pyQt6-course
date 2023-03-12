from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
#set the window size
        self.setGeometry(100, 100, 700, 400)
#set the window title
        self.setWindowTitle("My PyQt6 App")
#set the window icon
        self.setWindowIcon(QIcon('images/icon_gui.png'))
#adding picture as label
        label = QLabel(self)
        pix = QPixmap('images/icon_gui.png')
        label.setPixmap(pix)

app = QApplication(sys.argv)
window = Window()
#show the window
window.show()
#execute the app
sys.exit(app.exec())
