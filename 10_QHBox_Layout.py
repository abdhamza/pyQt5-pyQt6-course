#Horizontal Box Layout
#Horizontal Box Layout is used to arrange widgets horizontally or in a row.

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
#set the window size
        self.setGeometry(100, 100, 700, 400)
        self.setWindowTitle("My PyQt6 App")
        self.setWindowIcon(QIcon('images/icon_gui.png'))

        hbox = QHBoxLayout()
        
        button1 = QPushButton("Press 1")
        button2 = QPushButton("Press 2")
        button3 = QPushButton("Press 3")
        button4 = QPushButton("Press 4")

        hbox.addWidget(button1)
        hbox.addWidget(button2)
        hbox.addWidget(button3)
        hbox.addWidget(button4)

        self.setLayout(hbox)
        hbox.addSpacing(100)


app = QApplication(sys.argv)
window = Window()
#show the window
window.show()
#execute the app
sys.exit(app.exec())
