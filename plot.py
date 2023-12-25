import pygame
from entity import Entity


class Plot(Entity):
    def __init__(self):
        super().__init__("plot", sprite="plot.png", hardness=0)