import pygame
from settings import COLOR, MAX_VEL


class Ball:
    def __init__(self, x: int, y: int, radius: int):
        self.x: float = x
        self.original_x: int = x
        self.y: float = y
        self.original_y: int = y
        self.radius = radius
        self.x_vel: float = MAX_VEL
        self.y_vel: float = 0

    def draw(self, win: pygame.Surface):
        pygame.draw.circle(win, COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1
