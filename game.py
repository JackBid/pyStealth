from pygame import *
from pygame.sprite import *

from board import Board
from camera import Camera
from sprites.walls import *
from sprites.player import Player
from sprites.enemy import Enemy

class Game():

    def __init__(self): # constructor

        # 20 x 15 tile game
        self.windowWidth = 800
        self.windowHeight = 600

        # pygame setup
        pygame.init()
        self.screen = display.set_mode((self.windowWidth, self.windowHeight))
        display.set_caption("pyStealth")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('freesansbold.ttf', 28)

        # Create a player object and a group for rendering
        self.player = Player(380, 280)
        self.playerGroup = Group()
        self.playerGroup.add(self.player)

        # Create board and camera objects
        self.board = Board('res/boards/cathedral_floor.txt')
        self.currentLevel = 'cathedral_floor'
        self.camera = Camera(50, 200)

        # Create sprite groups for all tiles, enemies and walls
        self.tiles = self.board.generateScreenView(self.camera.x, self.camera.y)
        self.enemies = self.findTiles('Enemy')
        self.walls = self.findTiles('Wall')
        self.coins = self.findTiles('Coin')

        # Set running to True and start the game
        self.running = True
        self.run()

    # Return a group of tiles that match a given type
    def findTiles(self, tileType):
        group = Group()

        for tile in self.tiles:
            if type(tile).__name__ == tileType:
                group.add(tile)

        return group

    # Used to load a new level
    def loadLevel(self, levelName, startX, startY):

        self.board = Board('res/boards/' + levelName + '.txt')

        self.camera.x = startX
        self.camera.y = startY

        self.tiles = self.board.generateScreenView(self.camera.x, self.camera.y)
        self.enemies = self.findTiles('Enemy')
        self.walls = self.findTiles('Wall')

        self.currentLevel = levelName

    # Used to restart a level
    def restartLevel(self):

        # Find how many coins were collected and subtract this from the players score
        coinsCollected = self.board.numberOfCoins - self.board.numberOfCoinsLeft()
        self.player.score -= coinsCollected

        self.board = Board('res/boards/' + self.currentLevel + '.txt')

        self.camera.x = 50
        self.camera.y = 200

        self.tiles = self.board.generateScreenView(self.camera.x, self.camera.y)
        self.enemies = self.findTiles('Enemy')
        self.walls = self.findTiles('Wall')

    # Called by the game loop, handle any events (eg. key presses)
    # Used to move the camera and update sprite orientation
    def handleEvents(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.camera.changespeed(-4, 0)
                    self.player.image = self.player.leftImage
                elif event.key == pygame.K_d:
                    self.camera.changespeed(4, 0)
                    self.player.image = self.player.rightImage
                elif event.key == pygame.K_w:
                    self.camera.changespeed(0, -4)
                    self.player.image = self.player.backImage
                elif event.key == pygame.K_s:
                    self.camera.changespeed(0, 4)
                    self.player.image = self.player.frontImage

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.camera.changespeed(4, 0)
                elif event.key == pygame.K_d:
                    self.camera.changespeed(-4, 0)
                elif event.key == pygame.K_w:
                    self.camera.changespeed(0, 4)
                elif event.key == pygame.K_s:
                    self.camera.changespeed(0, -4)

    # Called every game loop
    # Call the update on sprite groups
    def update(self):

        # Update
        self.tiles = self.board.generateScreenView(self.camera.x, self.camera.y)
        self.enemies.update(self.walls, self.player, self.camera)
        self.camera.update(self.player, self.tiles)
        self.coins.update()

        if self.player.enemyCollision:
            self.restartLevel()
            self.player.enemyCollision = False

        self.text = self.font.render('Score: ' + str(self.player.score), True, (255,0,0))
        self.textRect = self.text.get_rect()
        self.textRect.x = 0
        self.textRect.y = 0

    # Called at end of game loop
    # Render information to screen based on current states
    def render(self):

        # Draw / render
        self.screen.fill((100, 100, 100))
        self.tiles.draw(self.screen)
        self.playerGroup.draw(self.screen)
        self.screen.blit(self.text, self.textRect)

        display.update()

    # The game loop
    def run(self):

        while self.running:

            self.clock.tick(30)

            self.handleEvents()

            self.update()
            self.render()

game = Game()
