from random import randint

import pygame
from block import Block


class Magma(Block):
    def __init__(self):
        super().__init__("lava.png", "lava")

    def block_event(self):
        return "damage", -200
