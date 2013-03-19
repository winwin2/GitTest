import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Simple_drawing_window3(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QImage("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        
        p.setPen(QColor(5,5,0))
        p.setBrush(QColor(0,127,0))
        
        p.drawPolygon([
            QPoint( 70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150),
            QPoint(100,200)
        ])
        p.end()
        
def main():
    app = QApplication(sys.argv)
    
    w = Simple_drawing_window3()
    w.show()
    
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())