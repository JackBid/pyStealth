from pygame import *
from pygame.sprite import *

class Player(Sprite):
    def __init__(self, x, y): # constructor
        Sprite.__init__(self)
        self.velocity = 4
        self.image =  Surface((40, 40))
        self.rect = Rect(x, y, 40, 40)

    def update(self, keys):
        
        if keys[pygame.K_w]: 
            self.rect.y -= self.velocity

        if keys[pygame.K_a]: 
            self.rect.x -= self.velocity

        if keys[pygame.K_s]: 
            self.rect.y += self.velocity
        
        if keys[pygame.K_d]: 
            self.rect.x += self.velocity