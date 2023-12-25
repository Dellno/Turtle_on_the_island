import pygame
from entity import Entity


class Stick(Entity):
    def __init__(self):
        super().__init__("stick", sprite="stick", hardness=0)