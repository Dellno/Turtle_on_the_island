from entity import Entity


class Thread(Entity):
    def __init__(self):
        super().__init__("thread", sprite="thread.png", hardness=0)
