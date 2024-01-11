from entity import Entity


# острый камень. используется для начальных крафтов
class SharpStone(Entity):
    def __init__(self):
        super().__init__("sharp_stone", sprite="sharp_stone.png", hardness=0)
