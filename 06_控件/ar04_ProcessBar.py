#!/usr/bin/python
# conding=utf-8


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton
from PyQt5.QtCore import QBasicTimer


class ProcessBar(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化UI界面"""

        # 创建进度条
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 50)

        # self.pbar.setFormat("%p")

        # 创建按钮
        self.btn = QPushButton('Start', self)

        self.btn.move(40, 80)

        self.btn.clicked.connect(self.doAction)

        # 创建计时器
        self.timer = QBasicTimer()
        self.step = 0

        # window settings
        self.setGeometry(500, 500, 500, 360)
        self.setWindowTitle("ProcessBar")
        self.show()
    
    # QObject 的事件处理函数
    def timerEvent(self, e):

        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        
        self.step = self.step + 1
        self.pbar.setValue(self.step)
        # print(self.step)

    def doAction(self):
        """按钮动作"""

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:  
            # start() : 过期时间 & 事件接受者
            self.timer.start(100, self)
            self.btn.setText('Stop')


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

    check_box = ProcessBar()

    sys.exit(app.exec_())