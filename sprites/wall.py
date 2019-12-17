from pygame import *
from pygame.sprite import *

class Wall(Sprite):
    def __init__(self, x, y): # constructor
        Sprite.__init__(self)
        self.image =  image.load("res/sprites/wall.png").convert()
        self.rect = self.image.get_rect().move(x, y)

    def update(self):
        return