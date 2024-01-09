import pygame
from random import randint
from dirt_block import Grass
from ash_block import Ash
from water_block import Water
from stone import Stone


class rIsland:
    def __init__(self, x, y, width, height, set_map, island_block=None):
        if island_block is None:
            island_block = [Grass(0)]
        self.x = x
        self.y = y
        self.width = width  # ширина
        self.height = height
        self.map = set_map
        self.island_block = island_block[:]
        self.generate_form()

    def generate_form(self):
        left_x = randint(5, self.height)
        right_x = randint(5, self.height)
        up_y = left_x
        low_y = right_x
        print(left_x, right_x, low_y, up_y)
        left_x = 10
        right_x = 10
        up_y = 10
        low_y = 10

        num2 = randint(1, min(left_x, right_x, up_y, low_y) // 4)
        num3 = randint(1, min(left_x, right_x, up_y, low_y) // 4)
        num1 = max(min(left_x, right_x), min(up_y, low_y)) / 2 - (num2 + num3)
        print(num1)
        if num1 % 1 != 0:
            num1 += 0.5
            num1 = int(num1)
        num1 = int(num1)
        if num1 == 0:
            num2 -= 1
            num1 = 1

        print(left_x, right_x, up_y, low_y)

        texture_percentages = {
            0: num1,
            2: num2,
            4: num3
        }

        print(num1, num2, num3)

        if left_x == right_x or up_y == low_y:
            x, y = max(up_y, low_y), max(left_x, right_x)
            # if x == y:
            #     num2 = randint(1, x // 4)
            #     num3 = randint(1, x // 4)
            #     num1 = x / 2 - (num2 + num3)
            #     if num1 % 1 != 0:
            #         num1 += 0.5
            #         num1 = int(num1)
            #     num1 = int(num1)
            #     if num1 == 0:
            #         num2 -= 1
            #         num1 = 1
            #
            #     texture_percentages = {
            #         0: num1,
            #         2: num2,
            #         4: num3
            #     }

            print(num1, num2, num3)
            for i in range(3):
                print(i)
                texture_options1 = [value for key, value in texture_percentages.items()]
                for j in range(texture_options1[i]):
                    texture_options = [key for key, value in texture_percentages.items()]
                    island_block = [Grass(int(texture_options[i]))]
                    self.island_block = island_block[:]
                    for i in range(0, x):
                        self.map.board[self.y][self.x + i] = self.island_block[0]
                        self.map.board[self.y + y - 1][self.x + i] = self.island_block[0]
                    for j in range(0, y):
                        self.map.board[self.y + j][self.x] = self.island_block[0]
                        self.map.board[self.y + j][self.x + x - 1] = self.island_block[0]
                    self.x += 1
                    self.y += 1
                    x -= 2
                    y -= 2
        else:
            average_y, average_x = max(up_y, low_y) - min(up_y, low_y), max(left_x, right_x) - min(left_x, right_x)
            for i in range(3):
                print(i)
                texture_options1 = [value for key, value in texture_percentages.items()]
                for j in range(texture_options1[i]):
                    texture_options = [key for key, value in texture_percentages.items()]
                    island_block = [Grass(int(texture_options[i]))]
                    self.island_block = island_block[:]
                    for _ in range(0, left_x):
                        if up_y < low_y:
                            if left_x < right_x:
                                self.map.board[self.y + average_x + _][self.x] = self.island_block[0]
                        else:
                            self.map.board[self.y + _][self.x] = self.island_block[0]
                    for _ in range(0, right_x):
                        if up_y < low_y:
                            if left_x < right_x:
                                self.map.board[self.y + _][self.x + low_y - 1] = self.island_block[0]
                        else:
                            self.map.board[self.y + _][self.x + up_y - 1] = self.island_block[0]
                    for _ in range(0, up_y):
                        if up_y < low_y:
                            if left_x < right_x:
                                self.map.board[self.y][self.x + average_y + _] = self.island_block[0]
                        else:
                            self.map.board[self.y][self.x + _] = self.island_block[0]
                    for _ in range(0, low_y):
                        if up_y < low_y:
                            self.map.board[self.y + max(left_x, right_x) - 1][self.x + _] = self.island_block[0]
                        else:
                            if left_x > right_x:
                                self.map.board[self.y + left_x - 1][self.x + _] = self.island_block[0]
                    for _ in range(0, average_y):
                        if up_y > low_y:
                            if left_x > right_x:
                                self.map.board[self.y + right_x - 1][self.x + low_y - 1 + _] = self.island_block[0]
                        else:
                            if left_x < right_x:
                                self.map.board[self.y + average_x][self.x + _] = self.island_block[0]
                    for _ in range(0, average_x):
                        if up_y > low_y:
                            if left_x > right_x:
                                self.map.board[self.y + right_x - 1 + _][self.x + low_y - 1] = self.island_block[0]
                        else:
                            if left_x < right_x:
                                self.map.board[self.y + _][self.x + average_y - 1] = self.island_block[0]
                    self.x += 1
                    self.y += 1
                    left_x -= 2
                    right_x -= 2
                    up_y -= 2
                    low_y -= 2
