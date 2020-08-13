#!/usr/bin/bash
# coding = tf8-e


import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow


class Communicate(QObject):
    """"""
    # 创建属性对象
    closeApp = pyqtSignal()


class CustomSignal(QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        # 创建实例
        self.c = Communicate()

        # 调用实例属性，关联窗口的关闭
        self.c.closeApp.connect(self.close)
      
        # windows settings
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle("Event Sender")
        self.show()

    # 重构
    def mousePressEvent(self, event):

        self.c.closeApp.emit()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    ssw = CustomSignal()

    sys.exit(app.exec_())