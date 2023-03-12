#Creating a simple PyQt6 application with dialog box

from PyQt6.QtWidgets import QApplication, QDialog
import sys

#app object controls the flow of application and its widgets
app = QApplication(sys.argv)

window = QDialog()
window.setWindowTitle("PyQt6 App")

window.show()
sys.exit(app.exec())
