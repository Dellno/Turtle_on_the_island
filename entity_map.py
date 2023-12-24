from random import randint

import pygame
from entity import Entity
from stone import Stone
from sharp_stone import SharpStone
from map import Map
from dirt_block import Grass


class EntityMap(Map):
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.board = [[None] * width for _ in range(height)]
        self.cell_size = 128
        self.screen = screen

    def generate_entity(self, start_x, start_y, width, height, luck, entity, block_map, block_type):
        for y in range(start_y, start_y + height):
            for x in range(start_x, start_x + width):
                ran = randint(1, 100 // luck)
                if ran == 1 and self.board[y][x] is None and isinstance(block_map.board[y][x], block_type):
                    self.board[y][x] = entity
