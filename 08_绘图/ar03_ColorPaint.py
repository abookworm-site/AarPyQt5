#!/usr/bin/python
# coding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QBrush


class ColorPaint(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        # window settings
        self.setGeometry(800, 300, 500, 500)

        self.setWindowTitle("ColorPaint")

        self.show()

    def paintEvent(self, event):
        """
        重构 painEvent
        1. 在该事件中完成绘画动作
        2. 一般固定在 begin() - end() 方法中间进行绘画动作        
        """
        painter = QPainter()

        painter.begin(self)

        self.drawRectangles(painter)

        painter.end()

    def drawRectangles(self, painter):
        """自定义绘制参数"""
        color = QColor(0, 0, 0)

        color.setNamedColor('#4d4d4')
        
        painter.setPen(color)

        # RGB 颜色
        painter.setBrush(QColor(255, 0, 0))
        # 绘制位置： x, y, w, h
        painter.drawRect(10, 15, 90, 60)

        # RGB + Alpha channel
        painter.setBrush(QColor(255, 80, 0, 160))
        # 绘制位置： x, y, w, h
        painter.drawRect(130, 15, 90, 60)

        # RGB + Alpha channel
        painter.setBrush(QColor(25, 0, 90, 200))
        # 绘制位置： x, y, w, h
        painter.drawRect(250, 15, 90, 60)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    wind = ColorPaint()

    sys.exit(app.exec_())