from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint
import UI
import sys


class YellowCircles(QMainWindow, UI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.paint = None
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_click)

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        qp.setBrush(QColor('yellow'))
        count = randint(3, 10)
        for i in range(count):
            x, y = randint(0, self.size().width()), randint(0, self.size().height())
            w = h = randint(5, 200)
            qp.drawEllipse(x, y, w, h)

    def btn_click(self):
        self.paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec_())
