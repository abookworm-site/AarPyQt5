#!/usr/bin/python
# coding = utf-8


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        self.statusBar().showMessage('Ready')

        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ab_window = MainWindow()

    sys.exit(app.exec_())