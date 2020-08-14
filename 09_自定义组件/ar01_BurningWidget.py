#!/usr/bin/python
# coding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtGui import QPainter, QFont, QColor, QPen


class Communicate(QObject):

    updateBW = pyqtSignal(int)


class BurningWidget(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        # 修改默认进度条高度
        self.setMinimumSize(1, 30)

        self.value = 75

        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]

    def setValue(self, value):

        self.value = value
    
    def paintEvent(self, e):

        painter = QPainter()

        painter.begin(self)

        self.drawWidgets(painter)

        painter.end()

    def drawWidgets(self, painter):
        """自定义绘制"""

        MAX_CAPACITY = 700
        OVER_CAPACITY = 750

        # 设置字体，大小
        font = QFont('Serif', 7, QFont.Light)

        painter.setFont(font)

        # 设置动态渲染组件，随窗口大小而变化
        size = self.size()

        w = size.width()

        h = size.height()

        step = int(round(w/10))

        till = int((w/OVER_CAPACITY) * self.value)
        full = int((w/OVER_CAPACITY) * MAX_CAPACITY)
        
        # 设置颜色矩形
        if self.value >= MAX_CAPACITY:

            painter.setPen(QColor(255, 255, 255))
            painter.setBrush(QColor(255, 255, 184))

            painter.drawRect(0, 0, full, h)

            painter.setPen(QColor(255, 175, 175))
            painter.setBrush(QColor(255, 175, 175))
            painter.drawRect(full, 0, till-full, h)
        else:
            painter.setPen(QColor(255, 255, 255))

            painter.setBrush(QColor(255, 255, 184))

            painter.drawRect(0, 0, till, h)

        # 设置分隔线
        pen = QPen(QColor(20, 20, 20), 1, Qt.SolidLine)

        painter.setPen(pen)

        painter.setBrush(Qt.NoBrush)

        painter.drawRect(0, 0, w-1, h-1)

        # 设置容量数字
        j = 0

        for i in range(step, 10 * step, step):

            # print(i)
            # print(j)

            # 绘制竖线
            painter.drawLine(i, 0, i, 5)

            metrics = painter.fontMetrics()
            # 获取数字的宽度
            fw = metrics.width(str(self.num[j]))
            # 文本对中竖线绘制
            painter.drawText(i-fw/2, h/2, str(self.num[j]))

            j = j + 1


class Burning(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        # 设置滑块
        OVER_CAPACITY = 750

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setRange(1, OVER_CAPACITY)
        sld.setValue(75)
        # 位置
        sld.setGeometry(30, 40, 150, 30)

        self.c = Communicate()

        self.wid = BurningWidget()
        
        self.c.updateBW[int].connect(self.wid.setValue)

        sld.valueChanged[int].connect(self.changeValue)

        hbox = QHBoxLayout()

        hbox.addWidget(self.wid)

        vbox = QVBoxLayout()

        vbox.addStretch(1)

        vbox.addLayout(hbox)
        # 渲染
        self.setLayout(vbox)

        # window settings
        self.setGeometry(800, 300, 390, 210)

        self.setWindowTitle("Burning")

        self.show()


    def changeValue(self, value):

        self.c.updateBW.emit(value)

        self.wid.repaint()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    custom_widget = Burning()

    sys.exit(app.exec_())