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

    def generateTiles(self, cameraX, cameraY):
        y = 0
        x = 0
        walls = Group()

        for row in self.board:
            for item in row:
                if x <= -40 or x > 800 or y <= -40 or y > 600:
                    x += 40
                    continue
                if item == '-':
                    walls.add(Wall(self.spritesheet, 'horizontal', x - cameraX, y - cameraY))
                elif item == '\\':
                    walls.add(Wall(self.spritesheet, 'verticle', x - cameraX, y - cameraY))
                elif item == '/':
                    walls.add(Wall(self.spritesheet, 'verticle', x+32 - cameraX, y - cameraY))
                elif item == '[':
                    walls.add(Wall(self.spritesheet, 'left corner', x - cameraX, y - cameraY))
                elif item == ']':
                    walls.add(Wall(self.spritesheet, 'right corner', x - cameraX, y - cameraY))
                x += 40
            y += 40
            x = 0
        
        return walls

    def __init__(self, path):
        self.board = self.readBoardFromFile(path)
        self.spritesheet = Spritesheet("res/sprites/walls.png")
