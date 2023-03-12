#Creating a simple PyQt6 application with qwidget

from PyQt6.QtWidgets import QApplication, QWidget
import sys

#app object controls the flow of application and its widgets
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PyQt6 App")

window.show()
sys.exit(app.exec())
