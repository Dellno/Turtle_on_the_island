from entity import Entity


# сухой куст. используется для получения палок
class DryBush(Entity):
    def __init__(self):
        super().__init__("dry_bush", sprite="suhoy_kust.png", hardness=-1)
