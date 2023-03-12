from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(100, 100, 700, 400)
        self.setWindowTitle("My PyQt6 App")
        self.setWindowIcon(QIcon('images/icon_gui.png'))
#adding line edit widget
        line_edit = QLineEdit(self)
        line_edit.move(100, 100)
        line_edit.setFont(QFont('Arial', 20))
        line_edit.setStyleSheet("background-color: pink")
#adding default text
        #line_edit.setText("Type Here")
#adding placeholder text
        line_edit.setPlaceholderText("Enter your name")
#enable the line edit
        line_edit.setEnabled(True)
#disable the line edit
        #line_edit.setEnabled(False)
#to add password we can use echo mode
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)

app = QApplication(sys.argv)
window = Window()
#show the window
window.show()
#execute the app
sys.exit(app.exec())
