import pygame

from block import Block


class Grass(Block):
    def __init__(self, texture_type: int):
        self.texture_type = texture_type
        if texture_type == 0:
            super().__init__("ground_0.png", "ground_0")
        if texture_type == 1:
            super().__init__("ground_1.png", "ground_1")
        if texture_type == 2:
            super().__init__("ground_2.png", "ground_2")
        if texture_type == 3:
            super().__init__("ground_3.png", "ground_3")
        if texture_type == 4:
            super().__init__("ground_4.png", "ground_4")
        if texture_type == 5:
            super().__init__("graviy.png", "ground_5")

