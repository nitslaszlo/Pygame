import sys

import pygame

from ball import Ball
from brick import Brick
from paddle import Paddle


class BreakoutGame:
    def __init__(self, width: int = 800, height: int = 600) -> None:
        # Initialize the BreakoutGame class.
        # width (int, optional): Width of the game window. Defaults to 800.
        # height (int, optional): Height of the game window. Defaults to 600.
        pygame.init()
        self.font: pygame.font.Font = pygame.font.Font(None, 36)
        self.score: int = 0

        self.width: int = width
        self.height: int = height
        self.screen: pygame.Surface = pygame.display.set_mode((width, height))
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.paddle: Paddle = Paddle(width // 2, height - 20)
        self.ball: Ball = Ball(width // 2, height // 2)

        self.lives: int = 5
        self.bricks: list[Brick] = []
        self.reset_bricks()

    def reset_bricks(self):
        # Reset the bricks for a new game.
        self.bricks = []
        for i in range(5):
            for j in range(12):
                self.bricks.append(Brick(j * 60 + 50, i * 20 + 50))

    def draw_text(self, text: str, pos: tuple[int, int]) -> None:
        # Draw text on the screen.
        # text (str): The text to display.
        # pos (tuple): The position (x, y) to display the text.
        surface: pygame.Surface = self.font.render(text, True, (255, 255, 255))
        rect: pygame.rect.Rect = surface.get_rect(center=pos)
        self.screen.blit(surface, rect)

    def run(self) -> None:
        # Main game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.paddle.move(2)

            if not self.bricks:
                self.ball.dx = 0
                self.ball.dy = 0
                self.draw_text(
                    "Congratulations! You Win!",
                    (self.screen.get_width() // 2, self.height // 2),
                )
                self.draw_text(
                    "Press any key to start a new game",
                    (self.screen.get_width() // 2, self.height // 2 + 50),
                )

                pygame.display.flip()
                # Wait for player to press any key
                waiting_for_input = True
                while waiting_for_input:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            waiting_for_input = False

                self.reset_bricks()
                self.ball.reset()
                self.paddle = Paddle(self.width // 2, self.height - 20)
                self.score = 0
                continue

            self.ball.move(2)
            hit_brick = self.ball.bounce(self.paddle, self.bricks)

            if hit_brick is not None:
                del self.bricks[hit_brick]
                self.score += 5

            # Check if ball hit the bottom of the screen
            if self.ball.rect.bottom > self.height:
                self.lives -= 1
                if self.lives == 0:
                    self.lives = 3
                    self.reset_bricks()
                    self.score = 0
                self.ball.reset()
                self.paddle = Paddle(self.width // 2, self.height - 20)

            self.screen.fill((0, 0, 0))
            self.paddle.draw(self.screen)
            self.ball.draw(self.screen)
            for brick in self.bricks:
                brick.draw(self.screen)
            self.draw_text(f"Score: {self.score}", (self.screen.get_width() // 2, 20))
            pygame.display.flip()
            self.clock.tick(120)
