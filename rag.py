import pygame
from entity import Entity


class Rag(Entity):
    def __init__(self):
        super().__init__("rag", sprite="tkan.png", hardness=0)