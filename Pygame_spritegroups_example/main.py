import random
from typing import Any
import pygame

# define screen size
SCREEN_WIDTH: int = 1000
SCREEN_HEIGHT: int = 600


# create class for squares
class Square(pygame.sprite.Sprite):
    def __init__(self, col: str, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.image: pygame.Surface = pygame.Surface((50, 50))
        self.image.fill(col)
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)
        self.rect.move_ip(0, 5)
        # check if sprite has gone off screen
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


def main() -> None:
    pygame.init()

    # create game window
    screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sprite Groups Example")

    # frame rate
    clock: pygame.time.Clock = pygame.time.Clock()
    FPS: int = 60

    # colours
    colours: list[str] = [
        "crimson",
        "chartreuse",
        "coral",
        "darkorange",
        "forestgreen",
        "lime",
        "navy",
    ]

    # create sprite group for squares
    squares: pygame.sprite.Group[Any] = pygame.sprite.Group()

    # create square and add to squares group
    square: Square = Square("red", 500, 300)

    squares.add(square)

    # game loop
    run: bool = True
    while run:
        clock.tick(FPS)

        # update background
        screen.fill("cyan")

        # update sprite group
        squares.update()

        # draw sprite group
        squares.draw(screen)

        print(squares) # to terminal (console) window

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # get mouse coordinates
                x, y = pygame.mouse.get_pos()
                # create square
                square: Square = Square(random.choice(colours), x, y)
                squares.add(square)
            # quit program
            if event.type == pygame.QUIT:
                run = False

        # update display
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
