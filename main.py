import pygame
from sprites import Direction, Food, Snake, Tile, TileStatus


class KeyManager:
    def __init__(self):
        self.keyBuffer = Direction.UP

    def handleKey(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN or pygame.K_s]:
            self.keyBuffer = Direction.DOWN
        if keys[pygame.K_UP or pygame]:
            self.keyBuffer = Direction.UP
        if keys[pygame.K_LEFT]:
            self.keyBuffer = Direction.LEFT
        if keys[pygame.K_RIGHT]:
            self.keyBuffer = Direction.RIGHT


pygame.init()

defaultTileSize = 25
defaultHeight = 1000
defaultWidth = 1000
screen = pygame.display.set_mode((defaultHeight, defaultWidth))
clock = pygame.time.Clock()
keyManager = KeyManager()

tiles = []
keyBuffer = Direction.UP

food = Food(defaultWidth, defaultHeight, defaultTileSize, defaultTileSize)
snake = Snake(defaultWidth, defaultHeight, defaultTileSize, defaultTileSize, keyBuffer)

for i in range(defaultWidth // defaultTileSize):
    for j in range(defaultHeight // defaultTileSize):
        tiles.append(
            Tile(
                i * defaultTileSize,
                j * defaultTileSize,
                defaultTileSize,
                defaultTileSize,
                TileStatus.EMPTY,
            )
        )

running = True
dt = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keyManager.handleKey()
    snake.move(keyManager.keyBuffer, dt)

    screen.fill("gray")

    for tile in tiles:
        tile.draw(screen)

    food.draw(screen)
    snake.draw(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
