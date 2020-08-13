#!/usr/bin/bash
# coding = tf8-e


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class EventSender(QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        # 匿名状态栏对象
        self.statusBar()

        # windows settings
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle("Event Sender")
        self.show()

    def buttonClicked(self):

        sender = self.sender()

        self.statusBar().showMessage(sender.text() + " was pressed!")


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    ssw = EventSender()

    sys.exit(app.exec_())