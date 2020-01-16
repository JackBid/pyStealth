from pygame import *
from pygame.sprite import *

class Enemy(Sprite):
    def __init__(self, x, y, dx, dy, spritesheet): # constructor
        Sprite.__init__(self)

        self.image1 = spritesheet.image_at(Rect(0, 120, 40, 40))
        self.image1.set_colorkey((255,255,255))
        self.image2 = spritesheet.image_at(Rect(40, 120, 40, 40))
        self.image2.set_colorkey((255,255,255))

        self.image = self.image1
        #self.image.set_colorkey((255,255,255))

        self.rect = self.image.get_rect().move(x, y)

        self.dx = dx
        self.dy = dy

        self.worldX = x
        self.worldY = y

        self.sight = 200

        self.animationCounter = 0
        self.walk = False

    def updatePosition(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def handleWallCollision(self, walls):

        # Handle y axis movement
        tempRect = Rect(self.rect.x, self.rect.y + self.dy, 40, 40)
        collision = False

        for wall in walls.sprites():
            if tempRect.colliderect(wall.rect):
                collision = True

        if collision:
            self.dy = -1 * self.dy

        self.worldY += self.dy

        # Handle x axis movement
        tempRect = Rect(self.rect.x + self.dx, self.rect.y, 40, 40)
        collision = False

        for wall in walls.sprites():
            if tempRect.colliderect(wall.rect):
                collision = True

        if collision:
            self.dx = -1 * self.dx
            self.image = pygame.transform.flip(self.image, True, False)

        self.worldX += self.dx

    def animate(self, delay):

        self.animationCounter += 1

        if self.animationCounter == delay:

            if self.walk == False:
                self.image = self.image2
                self.walk = True
            else:
                self.image = self.image1
                self.walk = False


            if self.dx < 0:
                self.image = pygame.transform.flip(self.image, True, False)

            self.animationCounter = 0


    def update(self, walls, player, camera):
        self.handleWallCollision(walls)

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
            player.enemyCollision = True
        
        self.animate(10)

