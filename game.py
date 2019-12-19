from pygame import *
from pygame.sprite import *

from board import Board
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
walls = board.generateWalls()

# create player
player = Player(100, 100)
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
                player.changespeed(-4, 0)
            elif event.key == pygame.K_d:
                player.changespeed(4, 0)
            elif event.key == pygame.K_w:
                player.changespeed(0, -4)
            elif event.key == pygame.K_s:
                player.changespeed(0, 4)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.changespeed(4, 0)
            elif event.key == pygame.K_d:
                player.changespeed(-4, 0)
            elif event.key == pygame.K_w:
                player.changespeed(0, 4)
            elif event.key == pygame.K_s:
                player.changespeed(0, -4)

    if player.rect.y < 0:
        board.updatePositon('up')
        walls = board.generateWalls()
        player.rect.y = 50

    if player.rect.y + 40 > 600:
        board.updatePositon('down')
        walls = board.generateWalls()
        player.rect.y = 500

    if player.rect.x + 40 > 800:
        board.updatePositon('right')
        walls = board.generateWalls()
        player.rect.x = 700

    if player.rect.x < 0:
        board.updatePositon('left')
        walls = board.generateWalls()
        player.rect.x = 100
    
    
    # Update
    walls.update()
    playerGroup.update(walls)
    

    # Draw / render
    screen.fill((100, 100, 100))
    walls.draw(screen)
    playerGroup.draw(screen)

    display.update()