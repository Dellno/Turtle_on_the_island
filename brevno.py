import pygame
from entity import Entity


class Brevno(Entity):
    def __init__(self):
        super().__init__("brevno", sprite="brevno.png", hardness=0)