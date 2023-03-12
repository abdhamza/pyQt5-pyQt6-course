from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
#set the window size
        self.setGeometry(100, 100, 700, 400)
#set the window title
        self.setWindowTitle("My PyQt6 App")
#set the window icon
        self.setWindowIcon(QIcon('images/icon_gui.png'))
#adding gif label usnig QTMovie class
        label = QLabel(self)
        movie = QMovie('images/animation.gif')
        #setting speed of animation
        movie.setSpeed(500)
        label.setMovie(movie)
        movie.start()

app = QApplication(sys.argv)
window = Window()
#show the window
window.show()
#execute the app
sys.exit(app.exec())
