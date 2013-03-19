import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QImage("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([
            QPoint( 70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150),
        ])

        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        p.drawPolygon([
            QPoint(50, 200), QPoint(150, 200), QPoint(100, 400),
        ])

        p.drawImage(QRect(200, 100, 320, 320), self.rabbit)
        p.end()
        
class Simple_drawing_window3(Simple_drawing_window):
    def __init__(self):
        Simple_drawing_window.__init__(self)
    
    def paintEvent(self,e):
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