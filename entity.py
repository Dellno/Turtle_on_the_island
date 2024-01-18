import pygame
from load_sprite import load_sprite

data_pach = '/data/data/com.dellno.TOTI/files/app/'


# родительский класс. Все наследники этого класса являются элементами entity_map и подобным.
class Entity:
    def __init__(self, name: str, sprite='nnn_crystal.png', hardness=-1, weight=1):
        self.hardness = hardness  # прочность предмета. отвечает за разрушаемость
        self.name = name  # используется для идентификации предмета в сохранениях и крафтах
        self.weight = weight  # отвечает за то, тонет ли предмет в воде
        self.img = load_sprite("assets/texture/entity/" + sprite)

    # проверяет может ли черепашка взять предмет
    def destroy(self, instrument_level):
        if self.hardness != -1 and instrument_level >= self.hardness:
            return True
        return False

    # использутся классами наследниками класса map для отрисовки предмета
    def render(self, x, y, screen, rotate=0):
        screen.blit(pygame.transform.rotate(self.img, rotate), (x, y))
