#!/usr/bin/python
# coding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon


class FileDialog(QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.statusBar()


        ofile = QAction(QIcon('open.png'), 'Open', self)
        ofile.setShortcut('Ctrl+O')
        ofile.setStatusTip('Open new File')

        ofile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')

        file_menu.addAction(ofile)

        # window settings 
        self.setGeometry(500, 500, 250, 180)
        self.setWindowTitle("Color Dialog")
        self.show()
    
    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '.')

        if fname[0]:
            f = open(fname[0], 'r')
        
            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    file_dialog = FileDialog()

    sys.exit(app.exec_())