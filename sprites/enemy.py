from pygame import *
from pygame.sprite import *

class Enemy(Sprite):
    def __init__(self, x, y, dx, dy): # constructor
        Sprite.__init__(self)

        self.image = image.load('res/sprites/player_front.png').convert()
        self.image.set_colorkey((255,255,255))

        self.rect = self.image.get_rect().move(x, y)

        self.dx = dx
        self.dy = dy

        self.worldX = x
        self.worldY = y

    def updatePosition(self, x, y):
        self.rect.x = x
        self.rect.y = y


    def update(self, walls, camera):

        tempRect = Rect(self.rect.x, self.rect.y + self.dy, 40, 40)
        collision = False

        for wall in walls.sprites():
            if tempRect.colliderect(wall.rect):
                collision = True

        if collision:
            self.dy = -1 * self.dy

        self.worldY += self.dy

        tempRect = Rect(self.rect.x + self.dx, self.rect.y, 40, 40)
        collision = False

        for wall in walls.sprites():
            if tempRect.colliderect(wall.rect):
                collision = True

        if collision:
            self.dx = -1 * self.dx

        self.worldX += self.dx
