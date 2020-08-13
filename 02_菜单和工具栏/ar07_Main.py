#!/usr/bin/python
# coding = utf-8


import sys
from PyQt5.QtWidgets import QApplication, qApp, QMenu, QMainWindow, QTextEdit, QAction
from PyQt5.QtGui import QIcon


class Main(QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        textEdit = QTextEdit()

        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit Application')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        newMenu = menubar.addMenu('&New')

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)

        self.setGeometry(500, 500, 350, 250)

        self.setWindowTitle("Main Windows")

        self.show()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    main = Main()

    sys.exit(app.exec_())