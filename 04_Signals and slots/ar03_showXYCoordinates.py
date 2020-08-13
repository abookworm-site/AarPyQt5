#!/usr/bin/bash
# coding = tf8-e


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel


class XYCoordinates(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        # 创建栅格对象
        grid = QGridLayout()
        grid.setSpacing(10)

        # 初始值
        x = 0
        y = 0

        self.text = "x: {0}, y: {1}".format(x, y)

        # 赋值 label 对象
        self.label = QLabel(self.text, self)

        # 对齐
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        # 设置鼠标追踪
        self.setMouseTracking(True)

        # 显示
        self.setLayout(grid)

        # windows settings
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Event Object")
        self.show()

    # 固定接口
    def mouseMoveEvent(self, e):
        """
        @Parm e: 表示事件对象
        """
        # 获取 x, y 的坐标值
        x = e.x()
        y = e.y()

        # 拼接字符串
        text = "x: {0}, y: {1}".format(x, y)

        # 输出到 QLabel 中
        self.label.setText(text)


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    ssw = XYCoordinates()

    sys.exit(app.exec_())