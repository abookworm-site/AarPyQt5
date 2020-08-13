#!/usr/bin/python
# coding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5.QtCore import Qt


class Pen(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        # window settings
        self.setGeometry(800, 300, 500, 500)

        self.setWindowTitle("Pen")

        self.show()

    def paintEvent(self, event):
        """
        重构 painEvent
        1. 在该事件中完成绘画动作
        2. 一般固定在 begin() - end() 方法中间进行绘画动作        
        """
        painter = QPainter()

        painter.begin(self)

        self.drawLines(painter)

        painter.end()

    def drawLines(self, painter):
        """自定义绘制参数"""
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        painter.setPen(pen)
        painter.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.CustomDashLine)
        # 线 + 空格 + 线 + 空格 ： 单位像素
        pen.setDashPattern([1, 4, 5, 4])
        painter.setPen(pen)
        painter.drawLine(20, 240, 250, 240)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    wind = Pen()

    sys.exit(app.exec_())