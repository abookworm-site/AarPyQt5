#!/usr/bin/python
# coding = utf-8


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu
from PyQt5.QtGui import QIcon


class SonMenuBar(QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        # 菜单栏
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')

        impMenu = QMenu('Import', self)

        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        # 退出键 设置
        # exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        # exitAct.setShortcut('Ctrl+Q')

        # exitAct.setStatusTip('Exit application')

        # exitAct.triggered.connect(qApp.quit)

        # # 添加状态栏
        # self.statusBar()

        # # 菜单栏
        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('&File')
        # fileMenu.addAction(exitAct)
        
        # window settings
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Simple menu')
        self.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    ab_window = SonMenuBar()

    sys.exit(app.exec_())