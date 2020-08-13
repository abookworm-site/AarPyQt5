#!/usr/bin/python
# coding = utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class AbsoluteWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        qtlb1 = QLabel("Zetcode", self)
        qtlb1.move(15, 10)

        qtlb2 = QLabel("Tutorial", self)
        qtlb2.move(35, 40)

        qtlb3 = QLabel("for programmers", self)
        qtlb3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)

        self.setWindowTitle('Absolute')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ab_window = AbsoluteWindow()

    sys.exit(app.exec_())