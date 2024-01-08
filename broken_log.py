import pygame
from entity import Entity


class Broken_log(Entity):
    def __init__(self):
        super().__init__("broken_log", sprite="slomannoe_brevno.png", hardness=0)