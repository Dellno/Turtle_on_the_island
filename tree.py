import pygame
from entity import Entity


class Tree(Entity):
    def __init__(self):
        super().__init__("tree", sprite="tree.png", hardness=0)