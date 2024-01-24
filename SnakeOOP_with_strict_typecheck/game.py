import sys
import pygame
from food import Food
from settings import WINDOW_SIZE, TILE_SIZE
from snake import Snake
from utils import Utils


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode([WINDOW_SIZE] * 2)
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.new_game()

    def draw_grid(self) -> None:
        for x in range(0, WINDOW_SIZE, TILE_SIZE):
            pygame.draw.line(self.screen, [50] * 3, (x, 0), (x, WINDOW_SIZE))
        for y in range(0, WINDOW_SIZE, TILE_SIZE):
            pygame.draw.line(self.screen, [50] * 3, (0, y), (WINDOW_SIZE, y))

    def new_game(self) -> None:
        self.snake = Snake()
        self.food = Food()

    def update(self) -> None:
        if self.snake.update():
            self.new_game()
        self.check_food()
        pygame.display.flip()
        self.clock.tick(60)

    def check_food(self) -> None:
        if self.snake.rect.center == self.food.rect.center:
            self.food.rect.center = Utils.get_random_position()
            self.snake.length += 1

    def draw(self) -> None:
        self.screen.fill("black")
        self.draw_grid()
        self.food.draw(self.screen)
        self.snake.draw(self.screen)

    def check_event(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # snake control
            self.snake.control(event)

    def run(self) -> None:
        while True:
            self.check_event()
            self.update()
            self.draw()
