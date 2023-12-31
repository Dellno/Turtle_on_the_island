import pygame
from load_sprite import load_sprite


class Entity:
    def __init__(self, name: str, sprite='nnn_crystal.png', hardness=-1, weight=1):
        self.hardness = hardness
        self.name = name
        self.weight = weight
        self.img = load_sprite("assets/texture/entity/" + sprite)

    def destroy(self, instrument_level):
        if self.hardness != -1 and instrument_level >= self.hardness:
            return True
        return False

    def render(self, x, y, screen, rotate=0):
        screen.blit(pygame.transform.rotate(self.img, rotate), (x, y))
