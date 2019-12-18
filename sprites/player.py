from pygame import *
from pygame.sprite import *

class Player(Sprite):
    def __init__(self, x, y): # constructor
        Sprite.__init__(self)
        self.dx = 0
        self.dy = 0
        self.velocity = 4
        self.image = Surface((40, 40))
        self.rect = Rect(x, y, 40, 40)

    def changespeed(self, x, y):
        self.dx += x
        self.dy += y
 

    def update(self, walls):
        
        self.rect.x += self.dx
        
        # Did moving left or right cause a collision?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.dx > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        
        self.rect.y += self.dy

        # Did moving up or down cause a collision?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.dy > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        
