#!/usr/bin/python
# conding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap


class LineEdit(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""
        # label 组件
        self.label = QLabel(self)
        # 创建行编辑器
        line_edit = QLineEdit(self)

        line_edit.move(60, 100)

        self.label.move(60, 40)

        line_edit.textChanged[str].connect(self.onChanged)

        # window settings
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("LineEdit")

        self.show()
    
    def onChanged(self, text):
        self.label.setText(text)
        self.label.adjustSize()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    check_box = LineEdit()

    sys.exit(app.exec_())