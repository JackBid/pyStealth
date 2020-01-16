import time as pyTime

from pygame import *
from pygame.sprite import *

from board import Board
from camera import Camera
from sprites.walls import *
from sprites.player import Player
from sprites.enemy import Enemy

from spritesheet import Spritesheet

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

        # Load spritesheet
        self.spritesheet = Spritesheet("res/sprites/spritesheet.png")

        # Create a player object and a group for rendering
        self.player = Player(380, 280, self.spritesheet)
        self.playerGroup = Group()
        self.playerGroup.add(self.player)

        # Create board and camera objects
        self.board = Board('res/boards/level_1.txt', self.spritesheet)
        self.currentLevel = 'level_1'
        self.camera = Camera(self.board.startPosition[0], self.board.startPosition[1])

        self.level0_collected_coins = []
        self.level1_collected_coins = []
        self.level2_collected_coins = []
        self.level3_collected_coins = []

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
    def loadLevel(self, levelName):

        self.board = Board('res/boards/' + levelName + '.txt', self.spritesheet)

        # Remove any coins already collected when returning
        if levelName == 'level_0':
            self.board.removeCoins(self.level0_collected_coins)
        elif levelName == 'level_1':
            self.board.removeCoins(self.level1_collected_coins)
        elif levelName == 'level_2':
            self.board.removeCoins(self.level2_collected_coins)
        elif levelName == 'level_3':
            self.board.removeCoins(self.level3_collected_coins)

        self.camera.x = self.board.startPosition[0]
        self.camera.y = self.board.startPosition[1]

        self.tiles = self.board.generateScreenView(self.camera.x, self.camera.y)
        self.enemies = self.findTiles('Enemy')
        self.walls = self.findTiles('Wall')
        self.coins = self.findTiles('Coin')

        self.currentLevel = levelName

    # Used to restart a level
    def restartLevel(self):

        pyTime.sleep(0.7)

        # Find how many coins were collected and subtract this from the players score
        coinsCollected = self.board.numberOfCoins - self.board.numberOfCoinsLeft()
        self.player.score -= coinsCollected

        self.board = Board('res/boards/' + self.currentLevel + '.txt', self.spritesheet)

        self.camera.x = self.board.startPosition[0]
        self.camera.y = self.board.startPosition[1]

        self.tiles = self.board.generateScreenView(self.camera.x, self.camera.y)
        self.enemies = self.findTiles('Enemy')
        self.walls = self.findTiles('Wall')
        self.coins = self.findTiles('Coin')

    # Called by the game loop, handle any events (eg. key presses)
    # Used to move the camera and update sprite orientation
    def handleEvents(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.camera.changespeed(-4, 0)
                    self.player.direction = 'left'
                elif event.key == pygame.K_d:
                    self.camera.changespeed(4, 0)
                    self.player.direction = 'right'
                    #self.player.image = self.player.rightImage
                elif event.key == pygame.K_w:
                    self.camera.changespeed(0, -4)
                    #self.player.image = self.player.backImage
                elif event.key == pygame.K_s:
                    self.camera.changespeed(0, 4)
                    #self.player.image = self.player.frontImage

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.camera.changespeed(4, 0)
                elif event.key == pygame.K_d:
                    self.camera.changespeed(-4, 0)
                elif event.key == pygame.K_w:
                    self.camera.changespeed(0, 4)
                elif event.key == pygame.K_s:
                    self.camera.changespeed(0, -4)

    def addPositions(self, master, positions):
        for position in positions:
            master.append(position)

    # Called every game loop
    # Call the update on sprite groups
    def update(self):

        # Update
        self.tiles = self.board.generateScreenView(self.camera.x, self.camera.y)
        self.enemies.update(self.walls, self.player, self.camera)
        self.coins.update()
        self.playerGroup.update(self.camera)

        newLevel, collected_coin_locations = self.camera.update(self.player, self.tiles)

        if self.currentLevel == 'level_0':
            self.addPositions(self.level0_collected_coins, collected_coin_locations)
        elif self.currentLevel == 'level_1':
            self.addPositions(self.level1_collected_coins, collected_coin_locations)
        elif self.currentLevel == 'level_2':
            self.addPositions(self.level2_collected_coins, collected_coin_locations)
        elif self.currentLevel == 'level_3':
            self.addPositions(self.level3_collected_coins, collected_coin_locations)

        

        if newLevel != '':
            self.loadLevel(newLevel)

        if self.player.enemyCollision:
            self.restartLevel()
            self.player.enemyCollision = False

        self.text = self.font.render('Score: ' + str(self.player.score), True, (255,255,255))
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
