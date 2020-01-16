from pygame import *
from pygame.sprite import *

from sprites.walls import *
from sprites.coin import Coin
from sprites.enemy import Enemy
from spritesheet import Spritesheet

class Board():

    def __init__(self, path):
        self.board = self.readBoardFromFile(path)
        self.spritesheet = Spritesheet("res/sprites/spritesheet.png")
        self.numberOfCoins = 0
        self.startPosition = (0, 0)
        self.worldView = self.generateWorldView()

    def numberOfCoinsLeft(self):
        coinsLeft = 0

        for tile in self.worldView:
            if type(tile).__name__ == 'Coin':
                coinsLeft += 1

        return coinsLeft

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

    def generateWorldView(self):
        y = 0
        x = 0
        tiles = Group()

        for row in self.board:
            for item in row:
                if item == '-':
                    tiles.add(Wall(self.spritesheet, 'horizontal', x, y))
                elif item == '\\':
                    tiles.add(Wall(self.spritesheet, 'verticle', x, y))
                elif item == '/':
                    tiles.add(Wall(self.spritesheet, 'verticle', x+28, y))
                elif item == '[':
                    tiles.add(Wall(self.spritesheet, 'top left corner', x, y))
                elif item == ']':
                    tiles.add(Wall(self.spritesheet, 'top right corner', x, y))
                elif item == '}':
                    tiles.add(Wall(self.spritesheet, 'bottom right corner', x, y))
                elif item == '{':
                    tiles.add(Wall(self.spritesheet, 'bottom left corner', x, y))
                elif item == 'C':
                    tiles.add(Coin(x, y, self.spritesheet))
                    self.numberOfCoins += 1
                elif item == 'E':
                    tiles.add(Enemy(x, y, 0, 1, self.spritesheet))
                elif item == 'e':
                    tiles.add(Enemy(x, y, 4, 0, self.spritesheet))
                elif item == 'S':
                    self.startPosition = (x-400, y-300)
                    print(self.startPosition)
                x += 40
            y += 40
            x = 0

        return tiles

    def generateScreenView(self, cameraX, cameraY):
        tiles = Group()

        for tile in self.worldView:

            screenX = tile.worldX - cameraX
            screenY = tile.worldY - cameraY

            # If within the screen view
            if screenX > -40 or screenX < 800 or screenY > -40 or screenY < 600:
                tile.updatePosition(screenX, screenY)
                tiles.add(tile)

        return tiles
