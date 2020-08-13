#!/usr/bin/bash
# coding = tf8-e


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class EventHandler(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        # windows settings
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Event Handler")
        self.show()

    # 固定接口
    def keyPressEvent(self, e):

        # 设置 ESC 退出键
        if e.key() == Qt.Key_Escape:

            self.close()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    ssw = EventHandler()

    sys.exit(app.exec_())