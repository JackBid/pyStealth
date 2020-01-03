from pygame import *
from pygame.sprite import *

from board import Board
from camera import Camera
from sprites.walls import *
from sprites.player import Player
from sprites.enemy import Enemy

# 20 x 15
WIDTH = 800
HEIGHT = 600
running = True

# pygame setup
pygame.init()
screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption("window title")
clock = pygame.time.Clock()

# get board from .txt and convert to sprites
board = Board('res/boards/board.txt')
camera = Camera()
tiles = board.generateScreenView(camera.x, camera.y)

walls = Group()
enemies = Group()

for tile in tiles:
    if type(tile).__name__ == 'Wall':
        walls.add(tile)
    if type(tile).__name__ == 'Enemy':
        enemies.add(tile)

# create player
player = Player(380, 280)
playerGroup = Group()
playerGroup.add(player)


font = pygame.font.Font('freesansbold.ttf', 28)

# the overall event loop
while running:

    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                camera.changespeed(-4, 0)
                player.image = player.leftImage
            elif event.key == pygame.K_d:
                camera.changespeed(4, 0)
                player.image = player.rightImage
            elif event.key == pygame.K_w:
                camera.changespeed(0, -4)
                player.image = player.backImage
            elif event.key == pygame.K_s:
                camera.changespeed(0, 4)
                player.image = player.frontImage

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                camera.changespeed(4, 0)
            elif event.key == pygame.K_d:
                camera.changespeed(-4, 0)
            elif event.key == pygame.K_w:
                camera.changespeed(0, 4)
            elif event.key == pygame.K_s:
                camera.changespeed(0, -4)

    # Update
    tiles = board.generateScreenView(camera.x, camera.y)
    enemies.update(walls, camera)
    camera.update(player, tiles)


    text = font.render('Score: ' + str(player.score), True, (255,0,0))
    textRect = text.get_rect()
    textRect.x = 0
    textRect.y = 0


    # Draw / render
    screen.fill((100, 100, 100))
    tiles.draw(screen)
    playerGroup.draw(screen)
    #enemies.draw(screen)
    screen.blit(text, textRect)

    display.update()
