#!/usr/bin/python3
# coding = utf-8


import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtCore import QCoreApplication


class CloseWindows(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        qtbtn = QPushButton('Quit', self)

        qtbtn.clicked.connect(QCoreApplication.instance().quit)

        # qtbtn.resize(qtbtn, sizeHint())
        # 按钮大小
        qtbtn.resize(50, 20)
        # 按钮位置
        qtbtn.move(50, 50)

        # 窗口设置
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    wd = CloseWindows()

    sys.exit(app.exec_())