import pygame
import random
from sprites import Food, Tile, TileStatus

pygame.init()

defaultTileSize = 20
defaultHeight = 1000
defaultWidth = 1000
screen = pygame.display.set_mode((defaultHeight, defaultWidth))
clock = pygame.time.Clock()

foodLocation = random.randint(0, 99), random.randint(0, 99)

tiles = []

for i in range(100):
    for j in range(100):
        tiles.append(Tile(i*defaultTileSize, j*defaultTileSize, defaultTileSize, defaultTileSize, TileStatus.EMPTY))

running = True
dt = 0
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill("gray")

    for tile in tiles:
        tile.draw(screen)

    food = Food(foodLocation[0], foodLocation[1], defaultTileSize, defaultTileSize)
    food.draw(screen)
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()