from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(100, 100, 700, 400)
        self.setWindowTitle("My PyQt6 App")
        self.setWindowIcon(QIcon('images/icon_gui.png'))
        self.create_button()

#defining push button
    def create_button(self):
        btn = QPushButton('Click Me', self)
        btn.setGeometry(100,100, 180,180)
        btn.setFont(QFont('Sanserif', 15, QFont.Weight.Bold))
        btn.setIcon(QIcon('images/icon_gui.png'))
        btn.setIconSize(QSize(40,40))
        #popup menu
        menu = QMenu()
        #setting font for menu
        menu.setFont(QFont('Sanserif', 15, QFont.Weight.Bold))
        menu.setStyleSheet("background-color: pink")
        menu.addAction(QIcon('images/icon_gui.png'), 'Copy')
        menu.addAction(QIcon('images/icon_gui.png'), 'Paste')
        menu.addAction(QIcon('images/icon_gui.png'), 'Cut')
        btn.setMenu(menu)

app = QApplication(sys.argv)
window = Window()
#show the window
window.show()
#execute the app
sys.exit(app.exec())
