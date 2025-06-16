from enum import Enum, auto
import random
import pygame


class TileStatus(Enum):
    EMPTY = 0
    OCCUPIED = 1


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

    def __int__(self):
        if self == Direction.UP or self == Direction.LEFT:
            return -1
        return 1

    @property
    def value(self):
        return int(self)


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
            random.randint(1, self.screenWidth // self.width) - 1,
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
        self.speed = 0.25  # this is how many seconds to wait before moving 1 tile
        self.body = []
        self.bodyLength = 5
        self.is_alive = True

        randomY = random.randint(1, self.screenHeight // self.height)

        while randomY > (self.screenHeight // self.height) - self.bodyLength:
            randomY = random.randint(1, self.screenHeight // self.height)

        self.direction = direction
        startLocation = (
            random.randint(1, self.screenWidth // self.width) - 1,
            randomY,
        )

        x = self.width * startLocation[0]
        y = self.height * startLocation[1]

        # build body of snake to start with
        for i in range(self.bodyLength):
            self.body.append(
                (
                    x // self.width,
                    y // self.height + i,
                )
            )

    def draw(self, screen):
        for i in range(len(self.body)):
            pygame.draw.rect(
                screen,
                "red",
                (
                    self.width * self.body[i][0],
                    self.height * self.body[i][1],
                    self.width,
                    self.height,
                ),
            )

    def update(self, direction: Direction, dt: float):
        self.dt += dt
        self.direction = direction

        if self.dt >= self.speed:
            self.dt = 0
            if self.try_to_eat():
                self.add_to_tail()
            self.move()

    def move(self):
        x = self.body[0][0]
        y = self.body[0][1]

        if self.direction == Direction.UP or self.direction == Direction.DOWN:
            y = self.body[0][1] + self.direction.value
        elif self.direction == Direction.LEFT or self.direction == Direction.RIGHT:
            x = self.body[0][0] + self.direction.value

        body_copy = self.body.copy()

        self.body = []
        self.body.append((x, y))

        for i in range(len(body_copy)):
            self.body.append(body_copy[i])

        self.body.pop()

    def try_to_eat(self):
        return False

    def add_to_tail(self):
        pass
