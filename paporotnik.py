from entity import Entity


class Paporotnik(Entity):
    def __init__(self):
        super().__init__("paporotnic", sprite="paporotnik.png", hardness=-1)
