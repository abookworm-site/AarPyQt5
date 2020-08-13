#!/usr/bin/python
# coding = utf-8


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QMenu


class RightClickMenu(QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""
        # window settings
        self.setGeometry(500, 500, 250, 150)
        self.setWindowTitle('Context menu')
        self.show()

    def contextMenuEvent(self, event):

        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    ab_window = RightClickMenu()

    sys.exit(app.exec_())