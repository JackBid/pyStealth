from pygame import *
from pygame.sprite import *

class Coin(Sprite):
    def __init__(self, x, y): # constructor
        Sprite.__init__(self)

        self.worldX = x
        self.worldY = y

        self.image = pygame.image.load('res/sprites/coin.png').convert()
        self.image.set_colorkey((255,255,255))

        self.rect = Rect(x, y, 40, 40)
    
    def updatePosition(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        return