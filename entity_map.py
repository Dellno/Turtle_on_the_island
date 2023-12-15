import pygame
from entity import Entity
from stone import Stone
from sharp_stone import SharpStone
from map import Map


class EntityMap(Map):
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.board = [[None] * width for _ in range(height)]
        self.board[127][127] = Stone()
        self.cell_size = 128
        self.screen = screen
