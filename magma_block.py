from random import randint

import pygame
from block import Block


class Magma(Block):
    def __init__(self):
        super().__init__("magma.png")

    def block_event(self):
        return "damage", -200
