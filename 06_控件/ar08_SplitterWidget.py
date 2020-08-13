#!/usr/bin/python
# conding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QFrame, QSplitter, QStyleFactory
from PyQt5.QtCore import Qt


class SplitterWidget(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        hbox = QHBoxLayout(self)

        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        # 创建 splitter1
        splitter1 = QSplitter(Qt.Horizontal)
        # 划分 splitter1
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        # 创建 splitter2
        splitter2 = QSplitter(Qt.Vertical)
        # 划分 splitter2
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        # add all to box
        hbox.addWidget(splitter2)

        # show box
        self.setLayout(hbox)

        # window settings
        self.setGeometry(800, 200, 300, 200)
        self.setWindowTitle("SplitterWidget")

        self.show()
    
    def onChanged(self, text):
        self.label.setText(text)
        self.label.adjustSize()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    check_box = SplitterWidget()

    sys.exit(app.exec_())