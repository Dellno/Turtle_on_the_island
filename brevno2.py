from entity import Entity


# 2 бревна
class Brevno_2(Entity):
    def __init__(self):
        super().__init__("brevno_2", sprite="brevno2.png", hardness=0, weight=0)
