#!/usr/bin/python3
# coding=utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main():
    app = QApplication(sys.argv)


    window = QWidget()

    # 改变窗口大小
    window.resize(500, 500)

    # 改变窗口位置
    window.move(600, 300)

    # 改变标题
    window.setWindowTitle('AarOCR')

    # 窗口显示
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()