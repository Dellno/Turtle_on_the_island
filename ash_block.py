import pygame
from block import Block


class Ash(Block):
    def __init__(self):
        super().__init__("pepel2.png")

    def block_event(self):
        return "damage", -1