from random import randint

import pygame


class Brick:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y
        self.rect: pygame.Rect = pygame.Rect(x, y, 60, 20)
        self.color: tuple[int, int, int] = (
            randint(0, 255),
            randint(0, 255),
            randint(0, 255),
        )

    def draw(self, screen: pygame.Surface) -> None:
        # Draw the brick on the screen.
        # screen (pygame.Surface): The surface to draw the brick on.
        pygame.draw.rect(screen, self.color, self.rect)
