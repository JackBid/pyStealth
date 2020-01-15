from pygame import *
from pygame.sprite import *

class Wall(Sprite):
    def __init__(self, spritesheet, position, x, y): # constructor
        Sprite.__init__(self)
        
        self.ss = spritesheet
        self.worldX = x
        self.worldY = y

        if position == 'horizontal':
            self.image =  self.ss.image_at(Rect(40, 0, 40, 40))
            self.rect = Rect(x, y, 40, 12)
        elif position == 'verticle':
            self.image = self.ss.image_at(Rect(120, 0, 12, 40))
            self.rect = Rect(x, y, 12, 40)
        elif position == 'top left corner':
            self.image = self.ss.image_at(Rect(0, 0, 40, 40))
            self.rect = Rect(x, y, 40, 12)
        elif position == 'top right corner':
            self.image = self.ss.image_at(Rect(80, 0, 40, 40))
            self.rect = Rect(x, y, 40, 12)
        elif position == 'bottom right corner':
            self.image = self.ss.image_at(Rect(80, 40, 40, 40))
            self.rect = Rect(x, y, 40, 12)
        elif position == 'bottom left corner':
            self.image = self.ss.image_at(Rect(0, 40, 40, 40))
            self.rect = Rect(x, y, 40, 12)
    
    def updatePosition(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        return