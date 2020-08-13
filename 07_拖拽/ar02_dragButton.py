#!/usr/bin/python
# coding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag


class Button(QPushButton):

    def __init__(self, title, parent):

        super().__init__(title, parent)

    def mouseMoveEvent(self, e):
        
        if e.buttons() != Qt.RightButton:
            return
        
        mimeData = QMimeData()

        drag = QDrag(self)

        drag.setMimeData(mimeData)

        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):

        super().mouseMoveEvent(e)

        if e.button() == Qt.LeftButton:
            print("press")


class ButtonDrag(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        self.setAcceptDrops(True)

        self.button = Button("Button", self)
        self.button.move(100, 65)
        
        # window settings
        self.setGeometry(800, 400, 500, 500)
        self.setWindowTitle("Simple drag and drop")
        # self.show()

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()

        self.button.move(position)
        e.setDropAction(Qt.MoveAction)
        e.accept()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    wid_obj = ButtonDrag()

    wid_obj.show()

    app.exec_()
