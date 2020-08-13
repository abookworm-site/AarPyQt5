#!/usr/bin/python
# coding = utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout


class GridLayout(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        grid = QGridLayout()

        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue

            button = QPushButton(name)

            grid.addWidget(button, *position)    

        # window settings
        self.move(300, 150)

        self.setWindowTitle('Calculator')

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ab_window = GridLayout()

    sys.exit(app.exec_())