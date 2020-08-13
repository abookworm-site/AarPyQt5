#!/usr/bin/python
# coding = utf-8


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QAction
from PyQt5.QtGui import QIcon


class RightClickMenu(QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)


        self.toolbar = self.addToolBar('Exit')

        self.toolbar.addAction(exitAct)

        
        # window settings
        self.setGeometry(500, 500, 250, 150)
        self.setWindowTitle('Context menu')
        self.show()




if __name__ == "__main__":

    app = QApplication(sys.argv)

    ab_window = RightClickMenu()

    sys.exit(app.exec_())