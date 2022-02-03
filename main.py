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

# game loop
running = True
while running:
    # set upload the game FPS times per second
    clock.tick(FPS)
    # get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # game display
    screen.fill(WHITE)
    pygame.display.update()

pygame.quit()
