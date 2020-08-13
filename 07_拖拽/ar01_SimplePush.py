#!/usr/bin/python
# coding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget


class SimplePush(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        




        # window settings
        self.setGeometry(800, 400, 500, 500)
        self.setWindowTitle("SimplePush")
        self.show()



if __name__ == "__main__":

    app = QApplication(sys.argv)

    wid_obj = SimplePush()

    sys.exit(app.exec_())