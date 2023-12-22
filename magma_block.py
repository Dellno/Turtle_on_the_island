from random import randint

import pygame
from block import Block


class Magma(Block):
    def __init__(self):
        super().__init__("magma.png")

    def block_event(self):
        if randint(0, 10) == 0:
            return "damage", -200
