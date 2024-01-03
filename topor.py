import pygame
from entity import Entity


class Topor(Entity):
    def __init__(self):
        super().__init__("topor", sprite="topor.png", hardness=0)