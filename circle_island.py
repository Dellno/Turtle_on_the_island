import pygame
from random import randint
from dirt_block import Grass
from magma_block import Magma
from water_block import Water


class CircleIsland:
    def __init__(self, x, y, width, height, set_map, island_block=None):
        if island_block is None:
            island_block = [Grass(4)]
        self.x = x - 10
        self.y = y - 10
        self.width = width
        self.height = height
        self.map = set_map
        self.island_block = island_block[:]
        self.generate_form()

    def generate_form(self):
        X1, Y1, R = self.width, self.height, self.width // 2
        x = 0
        y = R
        t = 0
        delta = 1 - 2 * R
        error = 0

        for i in range(self.width):
            while y >= x:
                t += 1
                # print(X1 + x + self.x, Y1 + y + self.y)
                self.map.board[X1 + x + self.x][Y1 + y + self.y] = self.island_block[0]
                self.map.board[X1 + x + self.x][Y1 - y + self.y] = self.island_block[0]
                self.map.board[X1 - x + self.x][Y1 + y + self.y] = self.island_block[0]
                self.map.board[X1 - x + self.x][Y1 - y + self.y] = self.island_block[0]
                self.map.board[X1 + y + self.x][Y1 + x + self.y] = self.island_block[0]
                self.map.board[X1 + y + self.x][Y1 - x + self.y] = self.island_block[0]
                self.map.board[X1 - y + self.x][Y1 + x + self.y] = self.island_block[0]
                self.map.board[X1 - y + self.x][Y1 - x + self.y] = self.island_block[0]

                error = 2 * (delta + y) - 1

                if delta < 0 and error <= 0:
                    delta += 2 * (x + 1)
                    x += 1
                    continue

                if delta > 0 and error > 0:
                    delta -= 2 * (y - 1)
                    y -= 1
                    continue

                delta += 2 * (x - y)
                x += 1
                y -= 1
            print(t)
            self.width -= 2
            self.height -= 2
            self.x += 2
            self.y += 2
            X1, Y1, R = self.width, self.height, self.width // 2
            x = 0
            y = R
            delta = 1 - 2 * R
            error = 0

        # for i in range(X1 - R + 1, X1 + R):
        #     for j in range(Y1 - R + 1, Y1 + R):
        #         if (i - X1) ** 2 + (j - Y1) ** 2 <= R ** 2:
        #             print(i + self.x, j + self.y)
        #             self.map[i + self.x][j + self.y] = self.island_block[0]
