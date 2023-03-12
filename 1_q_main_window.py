#Creating a simple PyQt6 application with main window

from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

#app object controls the flow of application and its widgets
app = QApplication(sys.argv)

window = QMainWindow()
window.statusBar().showMessage("Hello World")

#adding meny bar
window.menuBar().addMenu("File")
window.setWindowTitle("PyQt6 App")

window.show()
sys.exit(app.exec())
