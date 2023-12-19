from random import randint

import pygame
from block import Block


class Water(Block):
    def __init__(self):
        super().__init__("more.png")

    def block_event(self):
        if randint(0, 10) == 0:
            return "damage", -1
        return 'endurance', -1
