from entity import Entity


# палка. используется для крафтов.
class Stick(Entity):
    def __init__(self):
        super().__init__("stick", sprite="stick.png", hardness=0)
