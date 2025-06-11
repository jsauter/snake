from enum import Enum
import pygame

class TileStatus(Enum):
    EMPTY = 0
    OCCUPIED = 1

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
            pygame.draw.rect(screen, "grey", (self.x+1, self.y+1, self.width-2, self.height-2))
        # elif self.tileStatus == TileStatus.OCCUPIED:
        #     pygame.draw.rect(screen, "black", (self.x, self.y, self.width, self.height))

    def setStatus(self, status: TileStatus):
        self.status = status

class Food:
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, "green", (self.x, self.y, self.width, self.height))
        
        
