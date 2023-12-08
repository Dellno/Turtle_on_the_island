class Entity:
    def __init__(self, x, y, hardness=False):
        self.pos = (x, y)
        self.hardness = hardness
        print(self)

    def destroy(self, instrument_level):
        if not self.hardness:
            return False
        elif instrument_level >= self.hardness:
            return True
