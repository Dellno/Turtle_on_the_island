from entity import Entity


class SharpStone(Entity):
    def __init__(self):
        super().__init__("sharp_stone", sprite="sharp_stone.png", hardness=0)
