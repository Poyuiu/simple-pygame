from random import random
from tkinter import E
from turtle import width
import pygame
import random

# initialize the game and create the window
pygame.init()
WIDTH = 500
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('shooting game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BlUE = (0, 0, 255)

# init fps clock
clock = pygame.time.Clock()
FPS = 60

# sprite


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 8

    def update(self):
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_RIGHT] or keyPressed[pygame.K_d]:
            self.rect.x += self.speedx
        if keyPressed[pygame.K_LEFT] or keyPressed[pygame.K_a]:
            self.rect.x -= self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(4, 10)
        self.sppedx = random.randrange(-3, 3)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.sppedx
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(4, 10)
            self.sppedx = random.randrange(-3, 3)
        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(4, 10)
            self.sppedx = random.randrange(-3, 3)


allSprites = pygame.sprite.Group()
# player
player = Player()
allSprites.add(player)
# rock's'
for i in range(8):
    r = Rock()
    allSprites.add(r)

# game loop
running = True
while running:
    # set upload the game FPS times per second
    clock.tick(FPS)

    # get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # game update
    allSprites.update()

    # game display
    screen.fill(WHITE)
    allSprites.draw(screen)
    pygame.display.update()

pygame.quit()
