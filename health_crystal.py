import pygame
from entity import Entity


class Health_crystal(Entity):
    def __init__(self):
        super().__init__("health_cristal", sprite="health_crystal.png", hardness=0)