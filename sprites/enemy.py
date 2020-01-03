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

        self.sight = 200

    def updatePosition(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def handleCollision(self, walls):
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

    def update(self, walls, player, camera):
        self.handleCollision(walls)

        playerSeen = False

        visibleRect = Rect(0,0,1,1)

        if self.dx > 0:
            visibleRect = Rect(self.rect.x, self.rect.y, 40 + self.sight, 40)
        elif self.dx < 0:
            visibleRect = Rect(self.rect.x - self.sight, self.rect.y, self.sight, 40)
        elif self.dy > 0:
            visibleRect = Rect(self.rect.x, self.rect.y, 40, 40 + self.sight)
        elif self.dy < 0:
            visibleRect = Rect(self.rect.x, self.rect.y - self.sight, 40, self.sight)


        for wall in walls:
            if visibleRect.colliderect(wall.rect):
                if self.dx > 0:
                    visibleRect.width -= visibleRect.right - wall.rect.x
                elif self.dx < 0:
                    sight = self.rect.x - wall.rect.x
                    visibleRect.x = wall.rect.right
                    visibleRect.width = sight
                elif self.dy > 0:
                    visibleRect.height -= visibleRect.bottom - wall.rect.y
                elif self.dy < 0:
                    sight = self.rect.y - wall.rect.y
                    visibleRect.y = wall.rect.bottom
                    visibleRect.height = sight


        if player.rect.colliderect(visibleRect):
            camera.x = 0
            camera.y = 100

        return visibleRect
