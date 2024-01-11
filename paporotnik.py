from entity import Entity


# сущность для крафта ниток
class Paporotnik(Entity):
    def __init__(self):
        super().__init__("paporotnic", sprite="paporotnik.png", hardness=-1)
