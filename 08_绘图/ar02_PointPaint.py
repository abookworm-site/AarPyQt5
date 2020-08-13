#!/usr/bin/python
# coding=utf-8


import sys, random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class PointPaint(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        # window settings
        self.setGeometry(300, 300, 280, 170)

        self.setWindowTitle("PointPaint")

        self.show()

    def paintEvent(self, event):
        """重构 painEvent , 并在该事件中完成绘画动作"""
        painter = QPainter()

        painter.begin(self)

        self.drawPoints(painter)

        painter.end()

    def drawPoints(self, painter):
        """自定义绘制参数"""
        painter.setPen(Qt.black)

        size = self.size()

        for i in range(1000):

            x = random.randint(1, size.width() - 1)

            y = random.randint(1, size.height() - 1)

            painter.drawPoint(x, y)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    wind = PointPaint()

    sys.exit(app.exec_())