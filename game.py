from pygame import *
from pygame.sprite import *
from sprites.wall import Wall

# 20 x 15
WIDTH = 800
HEIGHT = 600

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

# get board from .txt and convert to sprites
board = readBoardFromFile('res/boards/board.txt')
walls = generateWalls(board)

# the overall event loop
while True:
    e = event.wait()
    if e.type == QUIT:
        pygame.quit()
        break
    
    screen.fill((100, 100, 100))
    walls.draw(screen)
    display.update()