from pygame import *
from pygame.sprite import *

class LevelLoader(Sprite):
    def __init__(self, x, y, spritesheet, direction, level): # constructor

        self.worldX = x
        self.worldY = y
        self.direction = direction

        if self.direction == 'up':
            self.image = spritesheet.image_at(Rect(0, 120, 40, 40))
        else:
            self.image = spritesheet.image_at(Rect(0, 120, 40, 40))
        
        self.rect = Rect(x, y, 40, 40)

        self.levelToLoad = level

        Sprite.__init__(self)
    
    def updatePosition(self, x, y):
        self.rect.x = x
        self.rect.y = y