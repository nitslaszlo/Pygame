from typing import Any

import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, color: str, x: int, y: int):
        super().__init__()
        file_path: str = "graphics/" + color + ".png"
        self.image: pygame.Surface = pygame.image.load(file_path).convert_alpha()
        self.rect: pygame.rect.Rect = self.image.get_rect(topleft=(x, y))
        self.value: int = 0

        if color == "red":
            self.value = 100
        elif color == "green":
            self.value = 200
        else:
            self.value = 300

    def update(self, *args: Any, **kwargs: dict[str, Any]) -> None:
        super().update(*args, **kwargs)
        self.rect.x += int(args[0])


class Extra(pygame.sprite.Sprite):
    def __init__(self, side: str, screen_width: int):
        super().__init__()
        self.image = pygame.image.load("graphics/extra.png").convert_alpha()

        if side == "right":
            x = screen_width + 50
            self.speed = -3
        else:
            x = -50
            self.speed = 3

        self.rect = self.image.get_rect(topleft=(x, 80))

    #def update(self):
    def update(self, *args: Any, **kwargs: dict[str, Any]) -> None:
        super().update(*args, **kwargs)
        self.rect.x += self.speed
