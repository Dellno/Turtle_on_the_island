from entity import Entity


# дерево. используется для создания брёвен
class Tree(Entity):
    def __init__(self):
        super().__init__("tree", sprite="tree.png", hardness=-1)
