#!/usr/bin/python
# coding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QPainterPath
from PyQt5.QtCore import Qt


class BezierCurve(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        # window settings
        self.setGeometry(800, 300, 500, 500)

        self.setWindowTitle("BezierCurve")

        self.show()

    def paintEvent(self, event):
        """
        重构 painEvent
        1. 在该事件中完成绘画动作
        2. 一般固定在 begin() - end() 方法中间进行绘画动作        
        """
        painter = QPainter()

        painter.begin(self)

        painter.setRenderHint(QPainter.Antialiasing)

        self.drawBezierCurve(painter)

        painter.end()

    def drawBezierCurve(self, painter):
        """自定义绘制参数"""
        path = QPainterPath()

        path.moveTo(30, 30)

        # cubicTo: 启始点，控制点，终止点
        path.cubicTo(30, 30, 200, 350, 350, 30)

        painter.drawPath(path)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    wind = BezierCurve()

    sys.exit(app.exec_())