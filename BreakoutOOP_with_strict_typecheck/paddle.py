import pygame


class Paddle:
    def __init__(self, x: int, y: int) -> None:
        self.rect: pygame.Rect = pygame.Rect(x, y, 80, 10)

    def draw(self, screen: pygame.Surface) -> None:
        # Draw the paddle on the screen.
        # screen (pygame.Surface): The surface to draw the paddle on.
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

    def move(self, speed: int) -> None:
        # Move the paddle based on user input.
        # speed (int): The speed at which the paddle moves.
        keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-speed, 0)
        elif keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.move_ip(speed, 0)
