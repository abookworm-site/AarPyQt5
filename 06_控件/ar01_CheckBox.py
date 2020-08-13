#!/usr/bin/python
# conding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt


class CheckBox(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        # 创建 QCheckBox 对象
        ckbox = QCheckBox('Show Title', self)

        ckbox.move(20, 20)

        # checkbox 构造器
        ckbox.toggle()

        ckbox.stateChanged.connect(self.change_title)

        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle("CheckBox")
        self.show()
    
    def change_title(self, state):

        if state == Qt.Checked:
            self.setWindowTitle('CheckBox')

        else:
            self.setWindowTitle('  ')


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    check_box = CheckBox()

    sys.exit(app.exec_())