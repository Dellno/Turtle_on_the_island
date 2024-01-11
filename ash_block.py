from block import Block


# блок пепла. используется в секретном острове. наносит урон при наступлении на него.
class Ash(Block):
    def __init__(self):
        super().__init__("pepel2.png", "ash")

    def block_event(self):
        return "damage", -1
