from map import Map


# карта для расположения мачты
class MachtaMap(Map):
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.board = [[None] * width for _ in range(height)]
        self.cell_size = 128
        self.screen = screen
