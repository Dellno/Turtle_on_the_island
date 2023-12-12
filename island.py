import pygame
from random import randint
from dirt_block import Grass
from water_block import Water


class Island:
    def __init__(self, x, y, width, height, set_map, island_block=None):
        if island_block is None:
            island_block = [Grass(0)]
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.map = set_map
        self.island_block = island_block[:]
        self.generate_form()

    def generate_form(self):
        b1 = 0
        b2 = 0
        for j in range(self.height // 2):
            if b1 == 0 and b2 == 0:
                b1 = randint(self.x, self.x + self.width // 2)
                b2 = randint(b1, self.x + self.width)
            else:
                b1 = b1 - randint(0, b1 - self.x)
                b2 = b2 + randint(0, self.x + self.width - b2)
            for i in range(b1, b2):
                self.map[j + self.y][i] = self.island_block[0]
        for j in range(self.height // 2, self.height):
            b1 = b1 + randint(0, b1 - self.x)
            b2 = b2 - randint(0, self.x + self.width - b2)
            for i in range(b1, b2):
                self.map[j + self.y][i] = self.island_block[0]
