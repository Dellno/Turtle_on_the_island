from entity import Entity


# 3 бревна
class Brevno_3(Entity):
    def __init__(self):
        super().__init__("brevno_3", sprite="brevno3.png", hardness=-1, weight=0)
