#!/usr/bin/python
# conding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap


class Pixmap(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""
        # 创建 box layout
        hbox = QHBoxLayout(self)

        # 添加本地图片对象
        pixmap = QPixmap('web.png')

        # label 组件
        label = QLabel(self)

        label.setPixmap(pixmap)

        hbox.addWidget(label)

        # 渲染 hbox layout
        self.setLayout(hbox)

        # window settings
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Pixmap")

        self.show()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    check_box = Pixmap()

    sys.exit(app.exec_())