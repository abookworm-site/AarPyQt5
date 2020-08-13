#!/usr/bin/python
# coding = utf-8


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtGui import QIcon


class CheckMenuBar(QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        self.statusbar = self.statusBar()

        self.statusbar.showMessage('Ready')


        menubar = self.menuBar()

        viewMenu = menubar.addMenu("View")


        viewStatAct = QAction('View statusbar', self, checkable=True)

        viewStatAct.setStatusTip('View statusbar')

        viewStatAct.setChecked(True)

        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        # window settings
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Simple menu')
        self.show()

    def toggleMenu(self, state):

        if state:
            self.statusbar.show()

        else:
            self.statusbar.hide()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    ab_window = CheckMenuBar()

    sys.exit(app.exec_())