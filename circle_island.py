from random import randint
from dirt_block import Grass
from magma_block import Magma
from ash_block import Ash


# круглый секретный остров-вулкан.
class CircleIsland:
    def __init__(self, x, y, radius, set_map, island_block=None):
        if island_block is None:
            island_block = [Grass(0)]
        self.radius = radius
        self.x = x - self.radius * 2
        self.y = y - self.radius * 2
        self.map = set_map
        self.island_block = island_block[:]
        self.generate_form()

    def generate_form(self):
        per, R = self.radius * 2, self.radius
        x = 0
        y = R
        t = 0
        delta = 1 - 2 * R
        error = 0

        num2 = randint(1, R // 5)  # если количество кругов от 5 до 9(R) то рандом не получается
        num3 = randint(1, R // 5)  # это происходит т.к. текстур 5 и чтобы не было багов
        num4 = randint(1, R // 5)  # чет с комментами плохо у меня и названия я с переводчиком делал(переменных)
        num5 = randint(1, R // 5)
        num1 = R - (num5 + num2 + num3 + num4)
        num5 = num5 + 1

        texture_percentages = {
            0: num1,
            2: num2,
            5: num3,
            7: num4,
            6: num5
        }

        for i in range(5):
            texture_options1 = [value for key, value in texture_percentages.items()]
            for j in range(texture_options1[i]):
                texture_options = [key for key, value in texture_percentages.items()]
                if texture_options[i] == int(7):
                    island_block = [Ash()]
                elif texture_options[i] == int(6):
                    island_block = [Magma()]
                else:
                    island_block = [Grass(int(texture_options[i]))]
                self.island_block = island_block[:]
                while y >= x:
                    t += 1
                    self.map.board[per + y + self.y][per + x + self.x] = self.island_block[0]
                    self.map.board[per + y + self.y][per + x + self.x - 1] = self.island_block[0]
                    self.map.board[per + y + self.y][per - x + self.x] = self.island_block[0]
                    self.map.board[per + y + self.y][per - x + self.x + 1] = self.island_block[0]
                    self.map.board[per - y + self.y][per + x + self.x] = self.island_block[0]
                    self.map.board[per - y + self.y][per + x + self.x - 1] = self.island_block[0]
                    self.map.board[per - y + self.y][per - x + self.x] = self.island_block[0]
                    self.map.board[per - y + self.y][per - x + self.x + 1] = self.island_block[0]
                    self.map.board[per + x + self.y][per + y + self.x] = self.island_block[0]
                    self.map.board[per + x + self.y - 1][per + y + self.x] = self.island_block[0]
                    self.map.board[per + x + self.y][per - y + self.x] = self.island_block[0]
                    self.map.board[per + x + self.y - 1][per - y + self.x] = self.island_block[0]
                    self.map.board[per - x + self.y][per + y + self.x] = self.island_block[0]
                    self.map.board[per - x + self.y + 1][per + y + self.x] = self.island_block[0]
                    self.map.board[per - x + self.y][per - y + self.x] = self.island_block[0]
                    self.map.board[per - x + self.y + 1][per - y + self.x] = self.island_block[0]

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
                self.radius -= 1
                self.x += 2
                self.y += 2
                per, R = self.radius * 2, self.radius
                x = 0
                y = R
                delta = 1 - 2 * R
                error = 0
