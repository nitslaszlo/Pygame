import sys

import pygame

from tetris import Tetris
from colors import Colors


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.title_font: pygame.font.Font = pygame.font.Font(None, 40)
        self.score_surface: pygame.surface.Surface = self.title_font.render(
            "Score", True, Colors.white
        )
        self.next_surface: pygame.surface.Surface = self.title_font.render(
            "Next", True, Colors.white
        )
        self.game_over_surface: pygame.surface.Surface = self.title_font.render(
            "GAME OVER", True, Colors.white
        )

        self.score_rect: pygame.Rect = pygame.Rect(320, 55, 170, 60)
        self.next_rect: pygame.Rect = pygame.Rect(320, 215, 170, 180)

        self.screen: pygame.Surface = pygame.display.set_mode((500, 620))

        self.clock: pygame.time.Clock = pygame.time.Clock()

        self.game: Tetris = Tetris()

        self.GAME_UPDATE: int = pygame.USEREVENT

        pygame.display.set_caption("Python TetrisOOP")
        pygame.time.set_timer(self.GAME_UPDATE, 200)

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if self.game.game_over:
                        self.game.game_over = False
                        self.game.reset()
                    if event.key == pygame.K_LEFT and not self.game.game_over:
                        self.game.move_left()
                    if event.key == pygame.K_RIGHT and not self.game.game_over:
                        self.game.move_right()
                    if event.key == pygame.K_DOWN and not self.game.game_over:
                        self.game.move_down()
                        self.game.update_score(0, 1)
                    if event.key == pygame.K_UP and not self.game.game_over:
                        self.game.rotate()
                if event.type == self.GAME_UPDATE and not self.game.game_over:
                    self.game.move_down()
            self.draw()

    def draw(self) -> None:
        # Drawing
        score_value_surface: pygame.surface.Surface = self.title_font.render(
            str(self.game.score), True, Colors.white
        )

        self.screen.fill(Colors.dark_blue)
        self.screen.blit(self.score_surface, (365, 20, 50, 50))
        self.screen.blit(self.next_surface, (375, 180, 50, 50))

        if self.game.game_over:
            self.screen.blit(self.game_over_surface, (320, 450, 50, 50))

        pygame.draw.rect(self.screen, Colors.light_blue, self.score_rect, 0, 10)
        self.screen.blit(
            score_value_surface,
            score_value_surface.get_rect(
                centerx=self.score_rect.centerx, centery=self.score_rect.centery
            ),
        )
        pygame.draw.rect(self.screen, Colors.light_blue, self.next_rect, 0, 10)
        self.game.draw(self.screen)

        pygame.display.update()
        self.clock.tick(60)
