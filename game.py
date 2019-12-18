from pygame import *
from pygame.sprite import *

from sprites.wall import *
from sprites.player import Player

# 20 x 15
WIDTH = 800
HEIGHT = 600
running = True

def readBoardFromFile(path):
    board = []
    f = open(path, 'r')

    text = f.readlines()
    for line in text:
        row = []
        for char in line:
            if char != '\n':
                row.append(char)
        board.append(row)
    
    return board

def generateWalls(board):
    y = 0
    x = 0
    walls = Group()

    for row in board:
        for item in row:
            if item == '-':
                walls.add(HorizontalWall(x, y))
            elif item == '\\':
                walls.add(VerticleWall(x, y))
            elif item == '/':
                walls.add(VerticleWall(x+32, y))
            elif item == '[':
                walls.add(LeftCornerWall(x, y))
            elif item == ']':
                walls.add(RightCornerWall(x, y))
            x += 40
        y += 40
        x = 0
    
    return walls


# pygame setup
pygame.init()
screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption("window title")
clock = pygame.time.Clock()

# get board from .txt and convert to sprites
board = readBoardFromFile('res/boards/board.txt')
walls = generateWalls(board)

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
    
    
    # Update
    walls.update()
    playerGroup.update(walls)
    

    # Draw / render
    screen.fill((100, 100, 100))
    walls.draw(screen)
    playerGroup.draw(screen)

    display.update()