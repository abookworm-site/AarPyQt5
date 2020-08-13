#!/usr/bin/python
# conding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Slider(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""
        # 创建水平的滑块模块
        slider = QSlider(Qt.Horizontal, self)

        slider.setFocusPolicy(Qt.NoFocus)

        slider.setGeometry(30, 40, 100, 30)

        slider.valueChanged[int].connect(self.changeValue)

        # self 指本身名称
        self.label = QLabel(self)

        # 提前在本地准备 mute.png
        self.label.setPixmap(QPixmap('mute.png'))

        self.label.setGeometry(160, 40, 80, 30)

        # window settings
        self.setGeometry(500, 500, 280, 200)
        self.setWindowTitle("Slider")
        self.show()

    def changeValue(self, value):

        if value == 0:
            self.label.setPixmap(QPixmap('mute.png'))

        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('min.png'))
        
        elif value > 30 and value < 60:
            self.label.setPixmap(QPixmap('med.png'))
        
        else:
            self.label.setPixmap(QPixmap('max.png'))

    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    check_box = Slider()

    sys.exit(app.exec_())