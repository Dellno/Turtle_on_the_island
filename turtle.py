import pygame

import dirt_block
from entity import Entity
from block import Block
from dirt_block import Grass
from water_block import Water


class Turtle:
    def __init__(self, spawn_x, spawn_y, block_map, entity_map):
        self.stat = {"damage": 3, "endurance": 9, "max_damage": 3, "max_endurance": 9}
        self.name = "master_turtle"
        self.entity_map = entity_map
        self.block_map = block_map
        self.cords = (spawn_x, spawn_y)
        self.anim = [[pygame.transform.rotate(pygame.image.load('assets/texture/turtle/turtle_' + str(i) + '.png'),
                                              j) for i in range(1, 17)] for j in [0, 270, 180, 90]]
        self.rotate = 0
        self.anim_step = 0
        self.turtle_damage = pygame.image.load('assets/texture/turtle/turtle_0.png')
        i_spawn = False
        for y in range(spawn_y, spawn_y + 30):
            for x in range(spawn_x, spawn_x + 30):
                if isinstance(block_map.board[y][x], Grass):
                    entity_map.board[y][x] = self
                    self.cords = (x, y)
                    i_spawn = True
                    break
            if i_spawn:
                break
        if not i_spawn:
            block_map.board[spawn_y][spawn_x] = Grass(0)
            entity_map.board[spawn_y][spawn_x] = self

    def render(self, x, y, screen):
        if isinstance(self.block_map.board[self.cords[1]][self.cords[0]], Water):
            screen.blit(self.anim[self.rotate][self.anim_step + 8], (x, y))
        else:
            screen.blit(self.anim[self.rotate][self.anim_step], (x, y))

    def is_correct_move(self, x, y):
        if (((self.cords[0] != x) ^ (self.cords[1] != y)) and self.entity_map.board[y][x] is None
                and abs(x - self.cords[0]) <= 1
                and abs(y - self.cords[1]) <= 1):
            return True
        return False

    def move(self, x, y):
        print(x, y)
        block_event = self.block_map.board[y][x].block_event()
        if not (block_event is None):
            self.stat[block_event[0]] += block_event[1]
            print(self.stat)
        self.entity_map.board[self.cords[1]][self.cords[0]] = None
        self.entity_map.board[y][x] = self

    def inventory_add(self, x, y):
        pass
