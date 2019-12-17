from pygame import *
from pygame.sprite import *
from sprites.wall import Wall

WIDTH = 800
HEIGHT = 600

pygame.init()

screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption("window title")

w = Wall(0, 0)

environment = Group(w)

# the overall event loop
while True:
    e = event.wait()
    if e.type == QUIT:
        pygame.quit()
        break

    
    screen.fill((100, 100, 100))
    environment.draw(screen)
    display.update()