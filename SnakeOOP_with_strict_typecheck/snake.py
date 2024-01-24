import pygame
from settings import WINDOW_SIZE, TILE_SIZE
from utils import Utils


class Snake:
    def __init__(self) -> None:
        self.rect: pygame.rect.Rect = pygame.rect.Rect(
            [0, 0, TILE_SIZE - 2, TILE_SIZE - 2]
        )
        self.rect.center = Utils.get_random_position()
        self.direction: pygame.math.Vector2 = pygame.math.Vector2(0, 0)
        self.step_delay: int = 100  # milliseconds
        self.time: int = 0
        self.length: int = 1
        self.segments: list[pygame.Rect] = []
        self.directions: dict[int, int] = {
            pygame.K_UP: 1,
            pygame.K_DOWN: 1,
            pygame.K_LEFT: 1,
            pygame.K_RIGHT: 1,
        }

    def control(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.directions[pygame.K_UP]:
                self.direction = pygame.math.Vector2(0, -TILE_SIZE)
                self.directions = {
                    pygame.K_UP: 1,
                    pygame.K_DOWN: 0,
                    pygame.K_LEFT: 1,
                    pygame.K_RIGHT: 1,
                }

            if event.key == pygame.K_DOWN and self.directions[pygame.K_DOWN]:
                self.direction = pygame.math.Vector2(0, TILE_SIZE)
                self.directions = {
                    pygame.K_UP: 0,
                    pygame.K_DOWN: 1,
                    pygame.K_LEFT: 1,
                    pygame.K_RIGHT: 1,
                }

            if event.key == pygame.K_LEFT and self.directions[pygame.K_LEFT]:
                self.direction = pygame.math.Vector2(-TILE_SIZE, 0)
                self.directions = {
                    pygame.K_UP: 1,
                    pygame.K_DOWN: 1,
                    pygame.K_LEFT: 1,
                    pygame.K_RIGHT: 0,
                }

            if event.key == pygame.K_RIGHT and self.directions[pygame.K_RIGHT]:
                self.direction = pygame.math.Vector2(TILE_SIZE, 0)
                self.directions = {
                    pygame.K_UP: 1,
                    pygame.K_DOWN: 1,
                    pygame.K_LEFT: 0,
                    pygame.K_RIGHT: 1,
                }

    def delta_time(self) -> bool:
        time_now: int = pygame.time.get_ticks()
        if time_now - self.time > self.step_delay:
            self.time = time_now
            return True
        return False

    def check_borders(self) -> bool:
        if self.rect.left < 0 or self.rect.right > WINDOW_SIZE:
            return True
        if self.rect.top < 0 or self.rect.bottom > WINDOW_SIZE:
            return True
        return False

    def check_selfeating(self) -> bool:
        if len(self.segments) != len(set(segment.center for segment in self.segments)):
            return True
        return False

    def move(self) -> None:
        if self.delta_time():
            self.rect.move_ip(self.direction)
            self.segments.append(self.rect.copy())
            self.segments = self.segments[-self.length :]

    def update(self) -> bool:
        if self.check_selfeating():
            return True
        if self.check_borders():
            return True
        # self.check_food()
        self.move()
        return False

    def draw(self, screen: pygame.Surface) -> None:
        for segment in self.segments:
            pygame.draw.rect(screen, "green", segment)
