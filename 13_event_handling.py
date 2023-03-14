# Description: Event Handling in PyQt6
#
# Event Handling is the process of responding to user actions such as mouse clicks, key presses, etc.
#
# PyQt6 provides a number of event handling methods that can be overridden in your custom widgets.
#
# The most commonly used event handling methods are:
#
# mousePressEvent() - This method is called when a mouse button is pressed.
# mouseReleaseEvent() - This method is called when a mouse button is released.
# mouseMoveEvent() - This method is called when the mouse is moved.
# keyPressEvent() - This method is called when a key is pressed.
# keyReleaseEvent() - This method is called when a key is released.
# closeEvent() - This method is called when the window is closed.
# resizeEvent() - This method is called when the window is resized.
# paintEvent() - This method is called when the window is repainted.

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
#set the window size
        self.setGeometry(100, 100, 700, 400)
        self.setWindowTitle("13 Event Handling")
        self.setWindowIcon(QIcon('images/icon_gui.png'))
        self.create_widget() 
    
    def create_widget(self):
        hbox = QHBoxLayout()
        button =QPushButton("change text")
        button.clicked.connect(self.clicked_btn)
        self.label = QLabel("Default Text")

        hbox.addWidget(button)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def clicked_btn(self):
        self.label.setText("New Text")
        self.label.setFont(QFont('Sanserif', 15, QFont.Weight.Bold))
        self.label.setStyleSheet("color: red")

app = QApplication(sys.argv)
window = Window()
#show the window
window.show()
#execute the app
sys.exit(app.exec())
