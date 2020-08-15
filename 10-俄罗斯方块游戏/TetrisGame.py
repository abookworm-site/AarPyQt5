#!/usr/bin/python
# coding=utf-8


import sys, random
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QFrame
from PyQt5.QtCore import Qt, pyqtSignal, QBasicTimer
from PyQt5.QtGui import QPainter, QColor


class Tetris(QMainWindow):
    """创建游戏"""

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        """初始化 UI 界面"""

        self.tboard = Board(self)

        self.setCentralWidget(self.tboard)

        self.statusbar = self.statusBar()

        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)

        self.tboard.start()

        self.resize(180, 380)
        # 对中屏幕
        self.center()
        self.setWindowTitle("Tetris")
        self.show()

    def center(self):
        """将游戏窗口放置于屏幕中央"""

        screen = QDesktopWidget().screenGeometry()

        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)


class Board(QFrame):
    """主要逻辑框架"""
    msg2Statusbar = pyqtSignal(str)

    BoardWidth = 10
    BoardHeight = 22

    Speed = 300

    def __init__(self, parent):

        super().__init__(parent)

        self.initBoard()

    def initBoard(self):
        
        # 创建游戏循环
        self.timer = QBasicTimer()

        # 初始化参数
        self.isWaitingAfterLine = False

        self.curX = 0
        self.curY = 0

        self.numLinesRemoved = 0
        self.board = []

        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()

    def shapeAt(self, x, y):
        """获取形状的屏幕位置"""
        return self.board[(y * Board.BoardWidth) + x]

    def setShapeAt(self, x, y, shape):
        """设置形状的屏幕位置"""
        self.board[(y * Board.BoardWidth) + x] = shape

    def squareWidth(self):
        """获取一个形状的宽度"""
        return self.contentsRect().width() // Board.BoardWidth

    def squareHeight(self):
        """获取一个形状的高度"""
        return self.contentsRect().height() // Board.BoardHeight

    def start(self):
        """开始游戏"""

        if self.isPaused:
            return
        
        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()

        self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.newPiece()

        self.timer.start(Board.Speed, self)

    def pause(self):
        """暂停游戏"""
        if not self.isStarted:
            return
        
        self.isPaused = not self.isPaused

        if self.isPaused:
            self.timer.stop()
            self.msg2Statusbar.emit("paused")

        else:
            self.timer.start(Board.Speed, self)
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.update()


    def paintEvent(self, event):
        """paints all shapes of the game"""

        painter = QPainter(self)

        rect = self.contentsRect()
        
        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()
        
        for i in range(Board.BoardHeight):

            for j in range(Board.BoardWidth):

                shape = self.shapeAt(j, Board.BoardHeight - i - 1)

                if shape != Tetrominoe.NoShape:

                    self.drawSquare(painter, rect.left() + j * self.squareWidth(), boardTop + i * self.squareHeight(), shape)

        if self.curPiece.shape() != Tetrominoe.NoShape:

            for i in range(4):

                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)

                self.drawSquare(painter, rect.left() + x * self.squareWidth(), boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(), self.curPiece.shape())


    def keyPressEvent(self, event):
        """定义按键事件"""
        if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
            super(Board, self).keyPressEvent(event)
            return

        key = event.key()

        # 暂停键：P
        if key == Qt.Key_P:
            self.pause()
            return
        
        # 暂停 
        if self.isPaused:
           return
        # 左移键
        elif key == Qt.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)
        # 右移键
        elif key == Qt.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)
        # 右旋转：下键
        elif key == Qt.Key_Down:
            self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)
        # 左旋转：上键
        elif key == Qt.Key_Up:
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)
        # 直接到底：空格键
        elif key == Qt.Key_Space:
            self.dropDown()
        # 直线降落：D键
        elif key == Qt.Key_D:
            self.oneLineDown()

        else:
            super(Board, self).keyPressEvent(event)

    def timerEvent(self, event):
        """时间事件"""
        if event.timerId() == self.timer.timerId():

            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            
            else:
                self.oneLineDown()
            
        else:
            super(Board, self).timerEvent(event)

    def clearBoard(self):
        """clear shapes form the board"""
        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Tetrominoe.NoShape)

    def dropDown(self):
        """将一个形状直接降落到底"""
        newY = self.curY

        while newY > 0:

            if not self.tryMove(self.curPiece, self.curX, newY - 1):
                break

            newY -= 1

        self.pieceDropped()

    def oneLineDown(self):
        """默认的直线下降，或者按键D直线下降"""
        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped()

    def pieceDropped(self):
        """after dropping shape, remove full lines and create new shape"""

        for i in range(4):

            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.shape())

        self.removeFullLines()

        if not self.isWaitingAfterLine:
            self.newPiece()

    def removeFullLines(self):
        """"removes all full lines from the board"""

        numFullLines = 0

        rowsToRemove = []

        for i in range(Board.BoardHeight):

            n = 0
            for j in range(Board.BoardWidth):

                if not self.shapeAt(j, i) == Tetrominoe.NoShape:
                    n = n + 1

            if n == 10:

                rowsToRemove.append(i)

        rowsToRemove.reverse()

        for m in rowsToRemove:

            for k in range(m, Board.BoardHeight):

                for l in range(Board.BoardWidth):

                        self.setShapeAt(l, k, self.shapeAt(l, k + 1))

        numFullLines = numFullLines + len(rowsToRemove)

        if numFullLines > 0:

            self.numLinesRemoved = self.numLinesRemoved + numFullLines

            self.msg2Statusbar.emit(str(self.numLinesRemoved))

            self.isWaitingAfterLine = True

            self.curPiece.setShape(Tetrominoe.NoShape)

            self.update()

    def newPiece(self):
        """创建一个新方块"""

        self.curPiece = Shape()
        self.curPiece.setRandomShape()
        self.curX = Board.BoardWidth // 2 + 1
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY()

        if not self.tryMove(self.curPiece, self.curX, self.curY):

            self.curPiece.setShape(Tetrominoe.NoShape)
            self.timer.stop()
            self.isStarted = False
            self.msg2Statusbar.emit("Game over")

    def tryMove(self, newPiece, newX, newY):
        """循环移动"""

        for i in range(4):

            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)

            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False

            if self.shapeAt(x, y) != Tetrominoe.NoShape:
                return False

        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()

        return True

    def drawSquare(self, painter, x, y, shape):
        """绘制方块图形"""

        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QColor(colorTable[shape])

        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2, self.squareHeight() - 2, color)

        painter.setPen(color.lighter())

        painter.drawLine(x, y + self.squareHeight() - 1, x, y)

        painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.darker())

        painter.drawLine(x + 1, y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        
        painter.drawLine(x + self.squareWidth() - 1, y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)        


class Tetrominoe(object):
    """所有砖块编码"""
    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7

class Shape(object):
    """所有砖块形状"""

    coordsTable = (
        ((0, 0),     (0, 0),     (0, 0),     (0, 0)),
        ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),
        ((0, -1),    (0, 0),     (1, 0),     (1, 1)),
        ((0, -1),    (0, 0),     (0, 1),     (0, 2)),
        ((-1, 0),    (0, 0),     (1, 0),     (0, 1)),
        ((0, 0),     (1, 0),     (0, 1),     (1, 1)),
        ((-1, -1),   (0, -1),    (0, 0),     (0, 1)),
        ((1, -1),    (0, -1),    (0, 0),     (0, 1))
    )

    def __init__(self):

        self.coords = [[0,0] for i in range(4)]

        self.pieceShape = Tetrominoe.NoShape

        self.setShape(Tetrominoe.NoShape)

    def shape(self):
        """获取形状"""
        return self.pieceShape
    
    def setShape(self, shape):
        """设置形状"""

        # table = self.coordsTable[shape]
        table = Shape.coordsTable[shape]

        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]
        
        self.pieceShape = shape

    def setRandomShape(self):
        """随机形状"""
        self.setShape(random.randint(1, 7))

    def x(self, index):
        return self.coords[index][0]

    def y(self, index):
        return self.coords[index][1]

    def setX(self, index, x):
        self.coords[index][0] = x

    def setY(self, index, y):
        self.coords[index][1] = y

    def minX(self):

        m = self.coords[0][0]

        for i in range(4):
            m = min(m, self.coords[i][0])
        
        return m
    
    def maxX(self):
        m = self.coords[0][0]

        for i in range(4):
            m = max(m, self.coords[i][0])
        
        return m

    def minY(self):

        m = self.coords[0][1]

        for i in range(4):
            m = min(m, self.coords[i][1])
        
        return m
    
    def maxY(self):
        m = self.coords[0][1]

        for i in range(4):
            m = max(m, self.coords[i][1])
        
        return m

    def rotateLeft(self):
        """左旋转"""
        # 方块不变
        if self.pieceShape == Tetrominoe.SquareShape:
            return self
        
        result = Shape()

        result.pieceShape = self.pieceShape

        for i in range(4):

            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))

        return result

    def rotateRight(self):
        """右旋转"""
        # 方块不变
        if self.pieceShape == Tetrominoe.SquareShape:
            return self
        
        result = Shape()

        result.pieceShape = self.pieceShape

        for i in range(4):

            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))

        return result


if __name__ == "__main__":
    """Running Game"""
    
    app = QApplication([])

    tetris = Tetris()

    sys.exit(app.exec_())