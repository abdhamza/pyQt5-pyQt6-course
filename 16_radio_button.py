#radio button is a widget that allows the user to choose one option from a list of mutually exclusive options.

from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My PyQt6 App")
        self.setGeometry(100, 100, 700, 400)
        self.setWindowIcon(QIcon('images/icon_gui.png'))
        self.create_radio()
        

    def create_radio(self):
        hbox = QHBoxLayout()
        #defining first radio button

        #defining first radio button
        rad1 = QRadioButton("Rainy Season")
        rad1.setIcon(QIcon('images/cloud-rain.svg'))
        rad1.setIconSize(QSize(50, 50))
        rad1.setFont(QFont('Sanserif', 20)) 
        #Setting initial state of the radio button
        rad1.setChecked(True)
        rad1.toggled.connect(self.radio_selected)

        #defining a second radio button
        rad2 = QRadioButton("Dizzling")
        rad2.setIcon(QIcon('images/cloud-drizzle.svg'))
        rad2.setIconSize(QSize(50, 50))
        rad2.setFont(QFont('Sanserif', 20)) 
        #Setting initial state of the radio button
        rad2.setChecked(False)
        rad2.toggled.connect(self.radio_selected)

        #defining a third radio button
        rad3 = QRadioButton("Clear Weather")
        rad3.setIcon(QIcon('images/cloud-off.svg'))
        rad3.setIconSize(QSize(50, 50))
        rad3.setFont(QFont('Sanserif', 20)) 
        #Setting initial state of the radio button
        rad3.setChecked(False)
        rad3.toggled.connect(self.radio_selected)

        #Setting initial state of the QLabel
        self.label = QLabel("Kindly select a weather condition")
        self.label.setFont(QFont("Sanserif", 20))

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        hbox.addWidget(rad1)
        hbox.addWidget(rad2)
        hbox.addWidget(rad3)

        self.setLayout(vbox)
    
    def radio_selected(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.label.setText(f"You have selected {radio_btn.text()}")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
