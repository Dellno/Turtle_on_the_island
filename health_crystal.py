import pygame
from entity import Entity


class HealthCrystal(Entity):
    def __init__(self):
        super().__init__("health_cristal", sprite="health_crystal.png")