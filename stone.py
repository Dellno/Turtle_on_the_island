import pygame
from entity import Entity


class Stone(Entity):
    def __init__(self):
        super().__init__("stone", sprite="stone.png", hardness=0)
