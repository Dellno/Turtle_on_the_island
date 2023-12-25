import pygame
from entity import Entity


class End_crystal(Entity):
    def __init__(self):
        super().__init__("end_cristal", sprite="endurance_crystal.png", hardness=0)