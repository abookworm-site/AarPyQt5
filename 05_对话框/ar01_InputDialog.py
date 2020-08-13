#!/usr/bin/python
# coding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QInputDialog


class InputDialog(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        # 创建按钮
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        # 创建编辑栏
        self.le = QLineEdit(self)
        self.le.move(130, 22)

        # window settings
        self.setGeometry(300, 300, 200, 180)
        self.setWindowTitle("Input Dialog")
        self.show()
    
    def showDialog(self):

        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.le.setText(str(text))


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    input_dialog = InputDialog()

    sys.exit(app.exec_())