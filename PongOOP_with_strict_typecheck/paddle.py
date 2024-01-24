import pygame
from settings import COLOR, VEL

class Paddle:

    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x: int = x
        self.original_x: int = x
        self.y: int = y
        self.original_y: int = y
        self.width = width
        self.height = height

    def draw(self, win: pygame.Surface):
        pygame.draw.rect(win, COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up: bool = True):
        if up:
            self.y -= VEL
        else:
            self.y += VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
