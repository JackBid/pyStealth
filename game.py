from pygame import *
from pygame.sprite import *

from sprites.wall import Wall
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
            if item == 'w':
                walls.add(Wall(x, y))
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
playerGroup = Group()
playerGroup.add(Player(100,100))


# the overall event loop
while running:
    
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    # Update
    playerGroup.update(keys)

    # Draw / render
    screen.fill((100, 100, 100))
    walls.draw(screen)
    playerGroup.draw(screen)

    display.update()