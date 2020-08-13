#!/usr/bin/python
# coding = utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout


class MessageBox(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)

        # 此处，显示有问题
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        # window settings
        self.setGeometry(300, 300, 350, 300)

        self.setWindowTitle('Review')

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ab_window = MessageBox()

    sys.exit(app.exec_())