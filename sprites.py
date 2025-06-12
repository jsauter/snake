from enum import Enum
import random
import pygame


class TileStatus(Enum):
    EMPTY = 0
    OCCUPIED = 1


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Tile:
    def __init__(self, x, y, width, height, tileStatus: TileStatus):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.tileStatus = tileStatus

    def draw(self, screen):
        if self.tileStatus == TileStatus.EMPTY:
            pygame.draw.rect(screen, "black", (self.x, self.y, self.width, self.height))
            pygame.draw.rect(
                screen,
                "grey",
                (self.x + 1, self.y + 1, self.width - 2, self.height - 2),
            )
        # elif self.tileStatus == TileStatus.OCCUPIED:
        #     pygame.draw.rect(screen, "black", (self.x, self.y, self.width, self.height))

    def setStatus(self, status: TileStatus):
        self.status = status


class Food:
    def __init__(self, screenWidth, screenHeight, width, height):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.width = width
        self.height = height

        self.foodLocation = (
            random.randint(1, self.screenWidth // self.width),
            random.randint(1, self.screenHeight // self.height),
        )
        self.x = self.width * self.foodLocation[0]
        self.y = self.height * self.foodLocation[1]

    def draw(self, screen):
        pygame.draw.rect(screen, "green", (self.x, self.y, self.width, self.height))


class Snake:
    def __init__(self, screenWidth, screenHeight, width, height, direction: Direction):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.width = width
        self.height = height
        self.dt = 0
        self.speed = 1  # this is how many seconds to wait before moving 1 tile
        self.path = []

        self.direction = direction

        self.startLocation = (
            random.randint(1, self.screenWidth // self.width),
            random.randint(1, self.screenHeight // self.height),
        )
        self.x = self.width * self.startLocation[0]
        self.y = self.height * self.startLocation[1]

    def draw(self, screen):
        pygame.draw.rect(screen, "red", (self.x, self.y, self.width, self.height))
        for i in range(len(self.path)):
            pygame.draw.rect(
                screen,
                "red",
                (self.path[i][0], self.path[i][1], self.width, self.height),
            )

    def move(self, direction: Direction, dt: float):
        self.dt += dt
        self.direction = direction

        if self.dt >= self.speed:

            print(self.direction)
            print(self.dt)
            self.dt = 0
