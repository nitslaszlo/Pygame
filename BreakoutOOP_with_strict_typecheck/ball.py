import pygame

from brick import Brick
from paddle import Paddle


class Ball:
    def __init__(self, x: int, y: int):
        self.start_x: int = x
        self.start_y: int = y
        self.reset()

    def reset(self):
        # Reset the ball to its initial position and direction."""
        self.rect = pygame.Rect(self.start_x, self.start_y, 10, 10)
        self.dx = 1
        self.dy = -1

    def draw(self, screen: pygame.Surface):
        # Draw the ball on the screen.
        # screen (pygame.Surface): The surface to draw the ball on.
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

    def move(self, speed: int):
        # Move the ball based on its current direction and speed.
        # speed (int): The speed at which the ball moves.
        self.rect.move_ip(self.dx * speed, self.dy * speed)

    def bounce(self, paddle: Paddle, bricks: list[Brick]) -> int | None:
        # Handle ball bouncing off walls, paddle, and bricks.
        # paddle (Paddle): The paddle object.
        # bricks (list): List of Brick objects.
        # return int or None: The index of the brick that the ball hit, or None if no brick was hit.
        if self.rect.left < 0 or self.rect.right > 800:
            self.dx *= -1
        elif self.rect.top < 0 or self.rect.colliderect(paddle.rect):
            self.dy *= -1
        else:
            # hit_brick: int = self.rect.collidelist(bricks)
            hit_brick: int = self.rect.collidelist([b.rect for b in bricks])
            if hit_brick != -1:
                self.dy *= -1
                return hit_brick
