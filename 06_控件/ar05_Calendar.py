#!/usr/bin/python
# conding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QLabel
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QFont


class Calendar(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""
        # 创建 box layout
        vbox = QVBoxLayout(self)

        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)

        vbox.addWidget(cal)

        self.label = QLabel(self)

        date = cal.selectedDate()

        self.label.setText(date.toString())

        vbox.addWidget(self.label)

        self.setLayout(vbox)

        # window settings
        self.setGeometry(500, 500, 500, 360)
        self.setWindowTitle("Calendar")

        self.show()
    
    def showDate(self, date):

        self.label.setText(date.toString())


"""
20200813 Debug：
Q: 由于中文系统显示香港英文。同时日期显示为香港中文。导致了程序显示的进度百分比字体或编码有问题。
A: 排查过后，将系统日期格式更改为香港英文，即可恢复正常
环境信息：
- 系统：简体中文
- 地区：中国
- 语言：香港英文（显示美国英文时，可能导致字体错乱）
- 日期：香港英文
"""
if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    check_box = Calendar()

    sys.exit(app.exec_())