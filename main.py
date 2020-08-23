import pygame
#from enemy import Enemy
from player import Player
#from window import Window
pygame.init()

import pygame

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.isRunning = True
        self.caption = "Gun Game"
    def draw(self, image, x, y):
        image.blit(self.window, (x, y))
    def mainloop(self):
        main_player = Player(100, 100, "images/standing.png")
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)
        while self.isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False

            self.draw(main_player.image, main_player.x, main_player.y)    
            self.window.fill((255,255,255))
               
            pygame.display.update()

game = Window(1200, 800)
game.mainloop()


#game.draw(main_player.image, main_player.x, main_player.y)