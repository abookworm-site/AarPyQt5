#!/usr/bin/python
# conding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame
from PyQt5.QtGui import QColor


class ToggleButton(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""
        # 设置初始值
        self.col = QColor(0, 0, 0)

        red_btn = QPushButton('Red', self)
        # 设置按纽为切换按钮
        red_btn.setCheckable(True)
        red_btn.move(10, 10)
        # 设置切换方法
        red_btn.clicked[bool].connect(self.setColor)

        green_btn = QPushButton('Green', self)
        # 设置按纽为切换按钮
        green_btn.setCheckable(True)
        green_btn.move(10, 60)
        green_btn.clicked[bool].connect(self.setColor)

        blue_btn = QPushButton('Blue', self)
        # 设置按纽为切换按钮
        blue_btn.setCheckable(True)
        blue_btn.move(10, 110)
        blue_btn.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)

        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())

        # window settings
        self.setGeometry(500, 500, 280, 200)
        self.setWindowTitle("ToggleButton")
        self.show()
    
    def setColor(self, pressed):
        """设置颜色"""
        # 获取点击的按钮
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0
        
        # 判断按钮文字，分别进行不同的设置
        if source.text() == "Red":
            self.col.setRed(val)

        elif source.text() == "Green":
            self.col.setGreen(val)

        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" % self.col.name())


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    check_box = ToggleButton()

    sys.exit(app.exec_())