#Vertical Box Layout
#Vertical Box Layout is used to arrange widgets vertically or in a column.

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
#set the window size
        self.setGeometry(100, 100, 700, 400)
        self.setWindowTitle("My PyQt6 App")
        self.setWindowIcon(QIcon('images/icon_gui.png'))

        vbox = QVBoxLayout()
        
        button1 = QPushButton("Press 1")
        button1.setGeometry(50,50, 50,50)
        button1.setFont(QFont('Sanserif', 15, QFont.Weight.Bold))

        button2 = QPushButton("Press 2")
        button2.setGeometry(50,50, 50,50)
        button2.setFont(QFont('Sanserif', 15, QFont.Weight.Bold))

        button3 = QPushButton("Press 3")
        button3.setGeometry(50,50, 50,50)
        button3.setFont(QFont('Sanserif', 15, QFont.Weight.Bold))

        button4 = QPushButton("Press 4")
        button4.setGeometry(50,50, 50,50)
        button4.setFont(QFont('Sanserif', 15, QFont.Weight.Bold))

        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)
        vbox.addWidget(button4)

        self.setLayout(vbox)
        vbox.addSpacing(100)


app = QApplication(sys.argv)
window = Window()
#show the window
window.show()
#execute the app
sys.exit(app.exec())
