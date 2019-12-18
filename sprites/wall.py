from pygame import *
from pygame.sprite import *

class HorizontalWall(Sprite):
    def __init__(self, x, y): # constructor
        Sprite.__init__(self)
        self.image =  image.load("res/sprites/wall_horizontal.png").convert()
        self.rect = Rect(x, y, 40, 8)

    def update(self):
        return

class VerticleWall(Sprite):
    def __init__(self, x, y): # constructor
        Sprite.__init__(self)
        self.image =  image.load("res/sprites/wall_verticle.png").convert()
        self.rect = self.image.get_rect().move(x, y)

    def update(self):
        return

class LeftCornerWall(Sprite):
    def __init__(self, x, y): # constructor
        Sprite.__init__(self)
        self.image =  image.load("res/sprites/wall_corner_left.png").convert()
        self.rect = self.rect = Rect(x, y, 40, 8)

    def update(self):
        return

class RightCornerWall(Sprite):
    def __init__(self, x, y): # constructor
        Sprite.__init__(self)
        self.image =  image.load("res/sprites/wall_corner_right.png").convert()
        self.rect = self.rect = Rect(x, y, 40, 8)

    def update(self):
        return