import pygame
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

running = True
dt = 0
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill("blue")

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()






