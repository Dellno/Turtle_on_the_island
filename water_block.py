from random import randint
from block import Block


# вода. отнимает выносливость черепашки при перемещенииcle
class Water(Block):
    def __init__(self):
        super().__init__("more.png", "water")

    def block_event(self):
        if randint(0, 10) == 0:
            return "damage", -1
        return 'endurance', -1
