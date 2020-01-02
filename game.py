from pygame import *
from pygame.sprite import *

from board import Board
from camera import Camera
from sprites.walls import *
from sprites.player import Player

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

# create player
player = Player(380, 280)
playerGroup = Group()
playerGroup.add(player)

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
    '''
    walls = Group()
    coins = Group()

    for sprite in tiles.sprites():
        if type(sprite).__name__ == 'Wall':
            walls.add(sprite)
        elif type(sprite).__name__ == 'Coin':
            coins.add(sprite)'''

    # Update
    tiles = board.generateScreenView(camera.x, camera.y)
    camera.update(player, tiles)
    

    # Draw / render
    screen.fill((100, 100, 100))
    tiles.draw(screen)
    playerGroup.draw(screen)

    display.update()