#!/usr/bin/python
# coding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5.QtCore import Qt


class BrushPaint(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        # window settings
        self.setGeometry(800, 300, 500, 500)

        self.setWindowTitle("BrushPaint")

        self.show()

    def paintEvent(self, event):
        """
        重构 painEvent
        1. 在该事件中完成绘画动作
        2. 一般固定在 begin() - end() 方法中间进行绘画动作        
        """
        painter = QPainter()

        painter.begin(self)

        self.drawBrushes(painter)

        painter.end()

    def drawBrushes(self, painter):
        """自定义绘制参数"""
        brush = QBrush(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(10, 15, 90, 60)

        brush = QBrush(Qt.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRect(130, 15, 90, 60)

        brush = QBrush(Qt.Dense2Pattern)
        painter.setBrush(brush)
        painter.drawRect(250, 15, 90, 60)

        brush = QBrush(Qt.DiagCrossPattern)
        painter.setBrush(brush)
        painter.drawRect(10, 105, 90, 60)

        brush = QBrush(Qt.Dense5Pattern)
        painter.setBrush(brush)
        painter.drawRect(130, 105, 90, 60)

        brush = QBrush(Qt.Dense6Pattern)
        painter.setBrush(brush)
        painter.drawRect(250, 105, 90, 60)

        brush = QBrush(Qt.HorPattern)
        painter.setBrush(brush)
        painter.drawRect(10, 195, 90, 60)

        brush = QBrush(Qt.VerPattern)
        painter.setBrush(brush)
        painter.drawRect(130, 195, 90, 60)

        brush = QBrush(Qt.BDiagPattern)
        painter.setBrush(brush)
        painter.drawRect(250, 195, 90, 60)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    wind = BrushPaint()

    sys.exit(app.exec_())