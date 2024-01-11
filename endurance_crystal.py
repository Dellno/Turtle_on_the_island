from entity import Entity


# кристал для востонавления выносливости.
class EnduranceCrystal(Entity):
    def __init__(self):
        super().__init__("endurance_crystal", sprite="endurance_crystal.png")
