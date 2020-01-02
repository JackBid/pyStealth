from pygame import *
from pygame.sprite import *
from sprites.coin import Coin

class Player(Sprite):
    def __init__(self, x, y): # constructor
        Sprite.__init__(self)

        self.leftImage = image.load('res/sprites/player_left.png').convert()
        self.leftImage.set_colorkey((255,255,255))

        self.rightImage = image.load("res/sprites/player_right.png").convert()
        self.rightImage.set_colorkey((255,255,255))

        self.frontImage = image.load('res/sprites/player_front.png').convert()
        self.frontImage.set_colorkey((255,255,255))

        self.backImage = image.load("res/sprites/player_back.png").convert()
        self.backImage.set_colorkey((255,255,255))

        self.image = self.leftImage
        self.rect = self.image.get_rect().move(x, y)

        self.score = 0


    def update(self, walls, camera):
        return
