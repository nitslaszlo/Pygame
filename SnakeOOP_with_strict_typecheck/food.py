import pygame
from settings import TILE_SIZE
from utils import Utils


class Food:
    def __init__(self) -> None:
        self.rect: pygame.rect.Rect = pygame.rect.Rect(
            [0, 0, TILE_SIZE - 2, TILE_SIZE - 2]
        )
        self.rect.center = Utils.get_random_position()

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, "red", self.rect)
