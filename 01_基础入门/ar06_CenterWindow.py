#!/usr/bin/python3
# coding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class CenterWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        self.resize(250, 150)

        self.center()

        self.setWindowTitle("Center Window")

        self.show()

    # 自定义方法
    def center(self):

        # 获得窗口对象
        qr = self.frameGeometry()

        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()

        # 显示到屏幕中心
        qr.moveCenter(cp)

        self.move(qr.topLeft())



if __name__ == "__main__":

    app = QApplication(sys.argv)

    center_window = CenterWindow()

    sys.exit(app.exec_())