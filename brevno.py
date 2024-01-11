from entity import Entity


# 1 бревно
class Brevno(Entity):
    def __init__(self):
        super().__init__("brevno", sprite="brevno.png", hardness=0, weight=0)
