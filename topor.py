from entity import Entity


# топор. используется для добычи брёвен
class Topor(Entity):
    def __init__(self):
        super().__init__("topor", sprite="topor.png", hardness=0)
