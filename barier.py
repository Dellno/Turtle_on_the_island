from entity import Entity
from load_sprite import load_sprite


# технический блок ограничевающий возможность передвежения по карте игроку
class Barier(Entity):
    def __init__(self):
        super().__init__("barier", sprite='barier.png', hardness=-1)
        self.img = load_sprite('assets/texture/entity/barier.png', -1)
