#!/usr/bin/python
# coding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class TextDrawing(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        # 设置绘制的字符
        self.text = "Лев Николаевич Толстой\nАнна Каренина"

        # window settings
        self.setGeometry(300, 300, 280, 170)

        self.setWindowTitle("TextDrawing")

        self.show()

    def paintEvent(self, event):
        """重构 painEvent , 并在该事件中完成绘画动作"""
        painter = QPainter()

        painter.begin(self)

        self.drawText(event, painter)

        painter.end()

    def drawText(self, event, painter):
        """自定义绘制参数"""
        painter.setPen(QColor(18, 134, 103))
        painter.setFont(QFont('Decorative', 10))
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    wind = TextDrawing()

    sys.exit(app.exec_())