#!/usr/bin/python
# coding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class Button(QPushButton):

    def __init__(self, title, parent):

        super().__init__(title, parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class SimplePush(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""
        # 新建编辑
        edit = QLineEdit('', self)

        edit.setDragEnabled(True)

        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)
        
        # window settings
        self.setGeometry(800, 400, 500, 500)
        self.setWindowTitle("Simple drag and drop")
        self.show()



if __name__ == "__main__":

    app = QApplication(sys.argv)

    wid_obj = SimplePush()

    sys.exit(app.exec_())