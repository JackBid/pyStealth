from pygame import *
from pygame.sprite import *

class Wall(Sprite):
    def __init__(self, leftX, topY): # constructor
        Sprite.__init__(self)
        self.image = Surface((40, 40))
        self.rect = Rect(leftX, topY, 40, 40)