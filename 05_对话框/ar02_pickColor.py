#!/usr/bin/python
# coding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog, QPushButton, QFrame
from PyQt5.QtGui import QColor


class ColorDialog(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        # 初始背景颜色
        col = QColor(0, 0, 0)

        # 创建
        self.frm = QFrame(self)
        # print(self.frm)

        # 这里的 QWidget background-color 均是属性字段
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())

        self.frm.setGeometry(130, 22, 100, 100)

        # 按钮
        self.btn = QPushButton('Dialog', self)

        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        # window settings 
        self.setGeometry(500, 500, 250, 180)
        self.setWindowTitle("Color Dialog")
        self.show()
    
    def showDialog(self):

        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    input_dialog = ColorDialog()

    sys.exit(app.exec_())