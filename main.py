import pygame

# initialize the game and create the window
pygame.init()
WIDTH = 500
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('shooting game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# init fps clock
clock = pygame.time.Clock()
FPS = 60

# sprite


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    def update(self):
        self.rect.x += 10
        if self.rect.left > WIDTH:
            self.rect.right = 0

allSprites = pygame.sprite.Group()
player = Player()
allSprites.add(player)

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
