from pygame import *
from pygame.sprite import *
from sprites.coin import Coin

class Player(Sprite):
    def __init__(self, x, y, spritesheet): # constructor
        Sprite.__init__(self)

    
        self.image1 = spritesheet.image_at(Rect(0, 160, 28, 40))
        self.image1.set_colorkey((255,255,255))

        self.image1_flipped = pygame.transform.flip(self.image1, True, False)

        self.image2 = spritesheet.image_at(Rect(40, 160, 28, 40))
        self.image2.set_colorkey((255,255,255))

        self.image2_flipped = pygame.transform.flip(self.image2, True, False)

        self.image = self.image1
        self.image_flipped = self.image1_flipped
        self.rect = self.image.get_rect().move(x, y)

        self.direction = 'right'
        self.flipped = False
        self.score = 0

        self.enemyCollision = False

        self.animationCounter = 0
        self.imageCounter = 0

    def changeDirection(self, direction):
        if direction != self.direction:
            self.image = pygame.transform.flip(self.image, True, False)
            self.direction = direction

    def animate(self, delay):
        self.animationCounter += 1
        
        if self.animationCounter == delay:

            if self.imageCounter == 0:
                self.image = self.image2
                self.image_flipped = self.image2_flipped
                self.imageCounter = 1
            elif self.imageCounter == 1:
                self.image = self.image1
                self.image_flipped = self.image1_flipped
                self.imageCounter = 0

            self.animationCounter = 0

    def update(self, camera):
        if camera.dx != 0:
            self.animate(10)

        if self.direction == 'left':
            self.image = self.image_flipped

        
