import pygame


class Map:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.board = [[None] * width for _ in range(height)]
        self.cell_size = 128
        self.screen = screen

    # cell_x и cell_y это координаты на которых стоит черепашка, они будут центральными. (от 0 до размера карты - 1)
    # pix_x и pix_y это координаты смещения, необходимы для синхронизации движения карты с движением черепашки. (-128, 128)
    def render(self, cell_x, cell_y, pix_x=0, pix_y=0):
        self.left = cell_x - 5
        self.top = cell_y - 2

        drx, dry = -((cell_x - 5) * 128) + pix_x, -((cell_y - 2) * 128) + pix_y
        step = self.cell_size
        for y in range(len(self.board)):
            if y not in range(cell_y - 3, cell_y + 3 + 1):
                dry += step
                continue
            if y > (cell_y + 11 + 1):
                break
            for x in range(len(self.board[0])):
                if x in range(cell_x - 6, cell_x + 6 + 1):
                    if self.board[y][x] is None:
                        pygame.draw.rect(self.screen, (255, 255, 255), (drx,
                                                                        dry,
                                                                        step,
                                                                        step), 1)
                    elif self.board[y][x] == 1:
                        pygame.draw.rect(self.screen, (255, 255, 255), (drx,
                                                                        dry,
                                                                        step,
                                                                        step), 0)
                if x > cell_x + 15 + 1:
                    break
                drx += step
            dry += step
            drx = -((cell_x - 5) * 128) + pix_x

    def get_cell(self, mouse):
        cell_y = None
        cell_x = None
        y_range = self.cell_size
        for y in range(len(self.board)):
            if int(mouse[1]) in range(y_range):
                cell_y = y
                break
            y_range += self.cell_size

        x_range = self.cell_size
        for x in range(len(self.board[0])):
            if int(mouse[0]) in range(x_range):
                cell_x = x
                break
            x_range += self.cell_size
        if cell_y is None or cell_x is None:
            return None
        return cell_x + self.left, cell_y + self.top

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        return cell
