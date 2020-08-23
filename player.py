import pygame

class Player():
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.vel = 5
        self.jumpCount = 10
        self.isJump = False
        self.image = pygame.image.load(image)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.vel
        if keys[pygame.K_d]:
            self.x += self.vel
        if keys[pygame.K_SPACE]:
            self.isJump = True
            self.jump()

    def jump(self):
        if self.jumpCount >= -10:
            y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
            self.jumpCount -= 1
        else: # This will execute if our jump is finished
            jumpCount = 10
            self.isJump = False
        