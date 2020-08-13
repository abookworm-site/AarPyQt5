#!/usr/bin/python
# coding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizePolicy, QLabel, QFontDialog, QPushButton


class FontDialog(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        vbox = QVBoxLayout()

        # 按钮
        self.btn = QPushButton('Dialog', self)

        self.btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.btn.move(20, 20)

        vbox.addWidget(self.btn)

        self.btn.clicked.connect(self.showDialog)

        self.label = QLabel("Knowledge only matters", self)

        self.label.move(130, 20)

        vbox.addWidget(self.label)

        self.setLayout(vbox)

        # window settings 
        self.setGeometry(500, 500, 250, 180)
        self.setWindowTitle("Color Dialog")
        self.show()
    
    def showDialog(self):

        font, ok = QFontDialog.getFont()

        if ok:
            self.label.setFont(font)


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    input_dialog = FontDialog()

    sys.exit(app.exec_())