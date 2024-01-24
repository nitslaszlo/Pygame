import pygame
from ball import Ball
from paddle import Paddle
from settings import (
    WHITE,
    BLACK,
    WIDTH,
    HEIGHT,
    PADDLE_HEIGHT,
    PADDLE_WIDTH,
    WINNING_SCORE,
    BALL_RADIUS,
    FPS,
    VEL,
    MAX_VEL
)


class Game:
    def draw(
        self,
        win: pygame.Surface,
        paddles: list[Paddle],
        ball: Ball,
        left_score: int,
        right_score: int,
    ) -> None:
        win.fill(BLACK)
        self.left_score_text = self.SCORE_FONT.render(f"{left_score}", 1, WHITE)
        self.right_score_text = self.SCORE_FONT.render(f"{right_score}", 1, WHITE)
        win.blit(
            self.left_score_text,
            (WIDTH // 4 - self.left_score_text.get_width() // 2, 20),
        )
        win.blit(
            self.right_score_text,
            (WIDTH * (3 / 4) - self.right_score_text.get_width() // 2, 20),
        )

        for paddle in paddles:
            paddle.draw(win)

        for i in range(10, HEIGHT, HEIGHT // 20):
            if i % 2 == 1:
                continue
            pygame.draw.rect(win, WHITE, (WIDTH // 2 - 5, i, 10, HEIGHT // 20))

        ball.draw(win)
        pygame.display.update()

    def handle_collision(self, ball: Ball, left_paddle: Paddle, right_paddle: Paddle):
        if ball.y + ball.radius >= HEIGHT:
            ball.y_vel *= -1
        elif ball.y - ball.radius <= 0:
            ball.y_vel *= -1

        if ball.x_vel < 0:
            if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
                if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                    ball.x_vel *= -1

                    middle_y: float = left_paddle.y + left_paddle.height / 2
                    difference_in_y: float = middle_y - ball.y
                    reduction_factor: float = (left_paddle.height / 2) / MAX_VEL
                    y_vel: float = difference_in_y / reduction_factor
                    ball.y_vel = -1 * y_vel

        else:
            if (
                ball.y >= right_paddle.y
                and ball.y <= right_paddle.y + right_paddle.height
            ):
                if ball.x + ball.radius >= right_paddle.x:
                    ball.x_vel *= -1

                    middle_y: float = right_paddle.y + right_paddle.height / 2
                    difference_in_y: float = middle_y - ball.y
                    reduction_factor: float = (right_paddle.height / 2) / MAX_VEL
                    y_vel: float = difference_in_y / reduction_factor
                    ball.y_vel = -1 * y_vel

    def handle_paddle_movement(
        self,
        keys: pygame.key.ScancodeWrapper,
        left_paddle: Paddle,
        right_paddle: Paddle,
    ):
        if keys[pygame.K_w] and left_paddle.y - VEL >= 0:
            left_paddle.move(up=True)
        if (
            keys[pygame.K_s]
            and left_paddle.y + VEL + left_paddle.height <= HEIGHT
        ):
            left_paddle.move(up=False)

        if keys[pygame.K_UP] and right_paddle.y - VEL >= 0:
            right_paddle.move(up=True)
        if (
            keys[pygame.K_DOWN]
            and right_paddle.y + VEL + right_paddle.height <= HEIGHT
        ):
            right_paddle.move(up=False)

    def run(self) -> None:
        run: bool = True
        clock: pygame.time.Clock = pygame.time.Clock()

        left_paddle = Paddle(
            10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT
        )
        right_paddle = Paddle(
            WIDTH - 10 - PADDLE_WIDTH,
            HEIGHT // 2 - PADDLE_HEIGHT // 2,
            PADDLE_WIDTH,
            PADDLE_HEIGHT,
        )
        ball: Ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

        left_score: int = 0
        right_score: int = 0

        while run:
            clock.tick(FPS)
            self.draw(
                self.WIN, [left_paddle, right_paddle], ball, left_score, right_score
            )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
            self.handle_paddle_movement(keys, left_paddle, right_paddle)

            ball.move()
            self.handle_collision(ball, left_paddle, right_paddle)

            if ball.x < 0:
                right_score += 1
                ball.reset()
            elif ball.x > WIDTH:
                left_score += 1
                ball.reset()

            won: bool = False
            win_text: str = ""
            if left_score >= WINNING_SCORE:
                won = True
                win_text = "Left Player Won!"
            elif right_score >= WINNING_SCORE:
                won = True
                win_text = "Right Player Won!"

            if won:
                text = self.SCORE_FONT.render(win_text, 1, WHITE)
                self.WIN.blit(
                    text,
                    (
                        WIDTH // 2 - text.get_width() // 2,
                        HEIGHT // 2 - text.get_height() // 2,
                    ),
                )
                pygame.display.update()
                pygame.time.delay(5000)
                ball.reset()
                left_paddle.reset()
                right_paddle.reset()
                left_score = 0
                right_score = 0

        pygame.quit()

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("OOP Pong example")
        self.SCORE_FONT = pygame.font.SysFont("comicsans", 50)
        self.WIN: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
