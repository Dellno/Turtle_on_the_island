from entity import Entity


class DryBush(Entity):
    def __init__(self):
        super().__init__("dry_bush", sprite="suhoy_kust.png", hardness=-1)
