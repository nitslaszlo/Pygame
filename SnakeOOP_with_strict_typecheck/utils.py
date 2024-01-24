from random import randrange
from settings import RANGE


class Utils:
    @staticmethod
    def get_random_position() -> tuple[int, int]:
        return (randrange(*RANGE), randrange(*RANGE))
