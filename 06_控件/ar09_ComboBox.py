#!/usr/bin/python
# conding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox
from PyQt5.QtCore import Qt

class ComboBox(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""
        self.label = QLabel('Ubuntu', self)

        combox = QComboBox(self)

        combox.addItem("Ubuntu")
        combox.addItem("Mandriva")
        combox.addItem("Fedora")
        combox.addItem("Arch")
        combox.addItem("Gentoo")

        combox.move(50, 50)

        self.label.move(50, 150)

        combox.activated[str].connect(self.onActivated)


        # window settings
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("ComboBox")

        self.show()
    
    def onActivated(self, text):
        self.label.setText(text)
        self.label.adjustSize()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    check_box = ComboBox()

    sys.exit(app.exec_())