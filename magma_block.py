from block import Block


# блок магмы. моментально убивает черепашку, если та на него наступит
class Magma(Block):
    def __init__(self):
        super().__init__("lava.png", "lava")

    def block_event(self):
        return "damage", -200
