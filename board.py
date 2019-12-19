from pygame import *
from pygame.sprite import *

from sprites.walls import *
from spritesheet import Spritesheet

class Board():

    def readBoardFromFile(self, path):
        board = []
        f = open(path, 'r')

        text = f.readlines()
        for line in text:
            row = []
            for char in line:
                if char != '\n':
                    row.append(char)
            board.append(row)
        
        return board

    def generateWalls(self):
        y = 0
        x = 0
        walls = Group()

        for row in self.boardScreen:
            for item in row:
                if item == '-':
                    walls.add(Wall(self.spritesheet, 'horizontal', x, y))
                elif item == '\\':
                    walls.add(Wall(self.spritesheet, 'verticle', x, y))
                elif item == '/':
                    walls.add(Wall(self.spritesheet, 'verticle', x+32, y))
                elif item == '[':
                    walls.add(Wall(self.spritesheet, 'left corner', x, y))
                elif item == ']':
                    walls.add(Wall(self.spritesheet, 'right corner', x, y))
                x += 40
            y += 40
            x = 0
        
        return walls

    def adjustBoardScreenWidth(self):
        
        newBoard = []

        for row in self.boardScreen:
            smallRow = row[self.leftIndex:self.leftIndex+20]
            newBoard.append(smallRow)

        return newBoard
    
    def updatePositon(self, direction):
        
        if direction == 'up':
            self.topIndex = max(self.topIndex-1, 0)

        if direction == 'down':
            self.topIndex += 1
        
        if direction == 'right':
            self.leftIndex += 1
        
        if direction == 'left':
            self.leftIndex -= 1

        self.boardScreen = self.board[self.topIndex:self.topIndex+15]
        self.boardScreen = self.adjustBoardScreenWidth()

    def __init__(self, path):
        self.board = self.readBoardFromFile(path)
        self.topIndex = 0
        self.leftIndex = 0
        self.boardScreen = self.board[self.topIndex:self.topIndex+15]
        self.boardScreen = self.adjustBoardScreenWidth()
        self.spritesheet = Spritesheet("res/sprites/walls.png")
