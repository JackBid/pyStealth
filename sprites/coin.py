from pygame import *
from pygame.sprite import *

class Coin(Sprite):
    def __init__(self, x, y, spritesheet): # constructor
        Sprite.__init__(self)

        self.worldX = x
        self.worldY = y

        self.counter = 0
        self.imageCounter = 1
        self.change = 1

        #self.image = pygame.image.load('res/sprites/coin.png').convert()
        self.image1 = spritesheet.image_at(Rect(0, 80, 40, 40))
        self.image2 = spritesheet.image_at(Rect(40, 80, 40, 40))
        self.image3 = spritesheet.image_at(Rect(80, 80, 40, 40))

        self.image = self.image1
        self.image.set_colorkey((255,255,255))

        self.rect = Rect(x, y, 40, 40)
    
    def updatePosition(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):

        self.counter += 1

        if self.counter == 10:
        
            self.imageCounter += self.change

            if self.imageCounter == 3 or self.imageCounter == 1:
                self.change *= -1

            if self.imageCounter == 1:
                self.image = self.image1
                self.image.set_colorkey((255,255,255))
            elif self.imageCounter == 2:
                self.image = self.image2
                self.image.set_colorkey((255,255,255))
            elif self.imageCounter == 3: 
                self.image = self.image3
                self.image.set_colorkey((255,255,255))

            self.counter = 0