import pygame

from block import Block


class Grass(Block):
    def __init__(self, texture_type: int):
        self.texture_type = texture_type
        match texture_type:
            case 0:
                super().__init__("ground_0.png")
            case 1:
                super().__init__("ground_1.png")
            case 2:
                super().__init__("ground_2.png")
            case 3:
                super().__init__("ground_3.png")
            case 4:
                super().__init__("ground_4.png")
