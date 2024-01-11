from water_block import Water
from dirt_block import Grass
from circle_island import CircleIsland
from island import Island
from turtle import Turtle


# клас для отрисовки блоков. родительский класс для остальных карт
class Map:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.board = [[Water()] * width for _ in range(height)]
        # генерация основных островов
        Island(128, 128, 10, 10, self)

        Island(142, 128, 6, 6, self, (Grass(2), Grass(4)))
        Island(147, 128, 6, 6, self, (Grass(2), Grass(4)))
        Island(140, 133, 6, 6, self, (Grass(2), Grass(4)))
        Island(145, 133, 6, 6, self, (Grass(2), Grass(4)))
        Island(142, 138, 6, 6, self, (Grass(2), Grass(4)))
        Island(147, 138, 6, 6, self, (Grass(2), Grass(4)))
        Island(149, 128, 6, 6, self, (Grass(2), Grass(4)))
        Island(149, 140, 6, 6, self, (Grass(2), Grass(4)))

        Island(108, 115, 6, 6, self)
        Island(113, 115, 6, 6, self)
        Island(110, 118, 6, 6, self)
        Island(113, 118, 6, 6, self)
        Island(112, 116, 6, 7, self, (Grass(4),))

        Island(117, 129, 8, 8, self, (Grass(0),))
        Island(118, 130, 6, 6, self, (Grass(2),))
        Island(118, 130, 6, 6, self, (Grass(4), Grass(2)))

        Island(115, 140, 20, 7, self, (Grass(4),))
        Island(112, 145, 20, 7, self, (Grass(4),))
        Island(109, 150, 20, 7, self, (Grass(4),))

        CircleIsland(100, 100, 10, self)

        # 10 - это кол-во кругов то есть ширина и длина 20
        self.cell_size = 128
        self.screen = screen
        self.left = 0
        self.top = 0

    # отрисовка всех элементов
    # cell_x и cell_y это координаты на которых стоит черепашка, они будут центральными. (от 0 до размера карты - 1)
    # pix_x и pix_y это координаты смещения, необходимы для синхронизации движения карты с движением черепашки. (-128, 128)
    def render(self, cell_x: int, cell_y: int, pix_x=0, pix_y=0):
        self.left = cell_x - self.screen.get_width() // 128 // 2
        self.top = cell_y - self.screen.get_height() // 128 // 2

        drx, dry = pix_x, pix_y
        step = self.cell_size
        for y in range(self.top - 1, len(self.board)):
            if y > (cell_y + self.screen.get_height() // 128 + 1):
                break
            for x in range(self.left - 1, len(self.board[0])):
                if x in range(self.left - 1, cell_x + self.screen.get_width() // 128 // 2 + 2):
                    if not (self.board[y][x] is None) and not isinstance(self.board[y][x], Turtle):
                        self.board[y][x].render(drx - 128, dry - 128, self.screen)
                    elif isinstance(self.board[y][x], Turtle):
                        self.board[y][x].render(drx - pix_x - 128, dry - pix_y - 128, self.screen)
                if x > cell_x + self.screen.get_width() // 128 + 1:
                    break
                drx += step
            dry += step
            drx = pix_x

    # метод для определения нажатой клетки
    def get_cell(self, mouse):
        cell_y = mouse[1] // 128
        cell_x = mouse[0] // 128
        return cell_x + self.left, cell_y + self.top

    # возвращает нажатую клетку

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        return cell
