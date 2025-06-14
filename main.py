import pygame
from sprites import Direction, Food, Snake, Tile, TileStatus


class KeyManager:
    def __init__(self):
        self.keyBuffer = Direction.UP

    def handle_key(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            self.keyBuffer = Direction.DOWN
        elif keys[pygame.K_UP]:
            self.keyBuffer = Direction.UP
        elif keys[pygame.K_LEFT]:
            self.keyBuffer = Direction.LEFT
        elif keys[pygame.K_RIGHT]:
            self.keyBuffer = Direction.RIGHT


pygame.init()

defaultTileSize = 25
defaultHeight = 1000
defaultWidth = 1000
screen = pygame.display.set_mode((defaultHeight, defaultWidth))
clock = pygame.time.Clock()
keyManager = KeyManager()

tiles = []

food = Food(defaultWidth, defaultHeight, defaultTileSize, defaultTileSize)
snake = Snake(defaultWidth, defaultHeight,
              defaultTileSize, defaultTileSize, Direction.UP)

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

    keyManager.handle_key()
    snake.update(keyManager.keyBuffer, dt)

    screen.fill("gray")

    for tile in tiles:
        tile.draw(screen)

    food.draw(screen)
    snake.draw(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
