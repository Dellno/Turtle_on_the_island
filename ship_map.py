from map import Map


# карта для карабля
class ShipMap(Map):
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.board = [[None] * width for _ in range(height)]
        self.cell_size = 128
        self.screen = screen
