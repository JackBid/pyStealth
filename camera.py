from pygame import *
from pygame.sprite import *

class Camera:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.minX = 0
        self.minY = 0
        self.width = 800
        self.height = 600

    def changespeed(self, x, y):
        self.dx += x
        self.dy += y

    def update(self, player, tiles):

        tempRect = Rect(380 + self.dx, 280 + self.dy, 28, 40)


        tempRect = Rect(380 + self.dx, 280, 28, 40)
        wallCollision = False

        newLevel = ''

        for tile in tiles.sprites():
            if tempRect.colliderect(tile.rect):
                if type(tile).__name__ == 'Wall':
                    wallCollision = True
                elif type(tile).__name__ == 'Coin':
                    player.score += 1
                    tile.kill()
                elif type(tile).__name__ == 'LevelLoader':
                    newLevel = 'level_' + str(tile.levelToLoad)

        if not wallCollision:
            self.x += self.dx

        tempRect = Rect(380, 280 + self.dy, 28, 40)
        wallCollision = False

        for tile in tiles.sprites():
            if tempRect.colliderect(tile.rect):
                if type(tile).__name__ == 'Wall':
                    wallCollision = True
                elif type(tile).__name__ == 'Coin':
                    player.score += 1
                    tile.kill()
                elif type(tile).__name__ == 'LevelLoader':
                    newLevel = 'level_' + str(tile.levelToLoad)

        if not wallCollision:
            self.y += self.dy

        return newLevel
