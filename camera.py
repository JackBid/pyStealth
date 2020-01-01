from pygame import *
from pygame.sprite import *

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
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

        tempRect = Rect(380 + self.dx, 280, 40, 40)
        noCollision = True
        
        for tile in tiles.sprites():
            if tempRect.colliderect(tile.rect):
                noCollision = False
        
        if noCollision:
            self.x += self.dx

        tempRect = Rect(380, 280 + self.dy, 40, 40)
        noCollision = True

        for tile in tiles.sprites():
            if tempRect.colliderect(tile.rect):
                noCollision = False
        
        if noCollision:
            self.y += self.dy

    
