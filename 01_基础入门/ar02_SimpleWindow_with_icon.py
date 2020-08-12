#!/usr/bin/python3
# coding=utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class IconWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 200)

        self.setWindowTitle('Icon')

        self.setWindowIcon(QIcon('web.png'))

        self.show()



if __name__ == "__main__":

    app = QApplication(sys.argv)

    icon_wd = IconWindow()

    # 注意：这里app 调用的是退出方法。
    sys.exit(app.exec_())