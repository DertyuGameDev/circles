import sys
import random
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.circles = []
        uic.loadUi('ui.ui', self)
        self.pushButton.clicked.connect(self.add_circle)

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            painter.setBrush(QColor(255, 255, 0))  # Желтый цвет
            painter.drawEllipse(circle[0], circle[1], circle[2], circle[2])  # Рисуем окружность

    def add_circle(self):
        diameter = random.randint(10, 50)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
