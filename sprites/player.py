from pygame import *
from pygame.sprite import *

class Player(Sprite):
    def __init__(self, x, y): # constructor
        Sprite.__init__(self)
        self.dx = 0
        self.dy = 0
        self.worldX = x
        self.worldY = y
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

    def changespeed(self, x, y):
        self.dx += x
        self.dy += y

    def update(self, walls, cameraX, cameraY):

        self.worldX += self.dx
        self.rect.x = self.worldX - cameraX
        
        # Did moving left or right cause a collision?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.dx > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        
        self.worldY += self.dy
        self.rect.y = self.worldY - cameraY

        # Did moving up or down cause a collision?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.dy > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        
