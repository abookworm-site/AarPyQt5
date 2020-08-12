#!/usr/bin/python3
# coding=utf-8

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox


class MessageWindows(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 200)

        self.setWindowTitle("Message Box")

        self.show()
    
    # 固定的函数借口，触发退出事件
    def closeEvent(self, event):

        reply = QMessageBox.question(self, "Message", "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        # 处理返回值
        if reply == QMessageBox.Yes:

            event.accept()
            
        else:
            event.ignore()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    msg = MessageWindows()

    sys.exit(app.exec_())