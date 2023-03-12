from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont
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
#setting fixed window size
        self.setFixedWidth(500)
        self.setFixedHeight(500)
#set background color to blue
        self.setStyleSheet("background-color: pink")
#setting opacity of window
        self.setWindowOpacity(1)
#creating a label
        label = QLabel("Gui Development", self)
#text of label can also be set using setText() method
        label.setText("Gui Development learning")
        #setting position of label
        label.move(100, 100)
        #setting font of label
        label.setFont(QFont("Times", 20))
        #setting color of label
        label.setStyleSheet("color: blue")

app = QApplication(sys.argv)
window = Window()
#show the window
window.show()
#execute the app
sys.exit(app.exec())
