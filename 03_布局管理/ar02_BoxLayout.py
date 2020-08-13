#!/usr/bin/python
# coding = utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class BoxLayout(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        ok_btn = QPushButton("OK")
        cancle_btn = QPushButton("Cancle")


        hbox = QHBoxLayout()
        # 增加水平方向上的位置调整
        hbox.addStretch(1)

        hbox.addWidget(ok_btn)
        # 增加垂直方向上的位置调整
        hbox.addWidget(cancle_btn)

        # 创建框布局
        vbox = QVBoxLayout()
        vbox.addStretch(1)

        vbox.addLayout(hbox)

        self.setLayout(vbox)

        # window settings
        self.setGeometry(300, 300, 250, 150)

        self.setWindowTitle('Buttons')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ab_window = BoxLayout()

    sys.exit(app.exec_())