import pygame
from entity import Entity


class Brevno_4(Entity):
    def __init__(self):
        super().__init__("brevno_4", sprite="brevno4.png", hardness=-1, weight=0)