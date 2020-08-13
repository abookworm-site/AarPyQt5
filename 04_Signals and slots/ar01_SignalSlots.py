#!/usr/bin/bash
# coding = tf8-e


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLCDNumber


class SignalSlots(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        # 创建显示对象
        lcd = QLCDNumber(self)
        # 创建滑块对象
        sld = QSlider(Qt.Horizontal, self)

        # 创建框布局
        vbox = QVBoxLayout()

        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)

        # 连接显示与滑块
        sld.valueChanged.connect(lcd.display)

        # windows settings
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Signal and slot")
        self.show()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    ssw = SignalSlots()

    sys.exit(app.exec_())