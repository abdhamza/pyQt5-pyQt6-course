#In grid layout we can set the position of the widget
#We have to set the row and column number of the widget

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
#set the window size
        self.setGeometry(100, 100, 700, 400)
        self.setWindowTitle("My PyQt6 App")
        self.setWindowIcon(QIcon('images/icon_gui.png'))

        grid = QGridLayout()

        button1 = QPushButton("Press 1")
        button2 = QPushButton("Press 2")
        button3 = QPushButton("Press 3")
        button4 = QPushButton("Press 4")
        button5 = QPushButton("Press 5")
        button6 = QPushButton("Press 6")
        button7 = QPushButton("Press 7")
        button8 = QPushButton("Press 8")
        button9 = QPushButton("Press 9")

        grid.addWidget(button1, 0, 0)
        grid.addWidget(button2, 0, 1)
        grid.addWidget(button3, 0, 2)
        grid.addWidget(button4, 1, 0)
        grid.addWidget(button5, 1, 1)
        grid.addWidget(button6, 1, 2)
        grid.addWidget(button7, 2, 0)
        grid.addWidget(button8, 2, 1)
        grid.addWidget(button9, 2, 2)

        self.setLayout(grid)

app = QApplication(sys.argv)
window = Window()
#show the window
window.show()
#execute the app
sys.exit(app.exec())
