class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.width = 800
        self.height = 600
    
    def changespeed(self, x, y):
        self.dx += x
        self.dy += y
    
    def update(self):
        self.x += self.dx
        self.y += self.dy
    
