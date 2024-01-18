import pygame
from load_sprite import load_sprite


# родительски класс, все наследники этого класса формируют карту блоков.
class Block:
    def __init__(self, texture: str, name="block"):
        self.name = name  # используется для идентификации блока в сохранениях и крафтах
        self.texture = load_sprite(f"assets/texture/ground/{texture}")

    #  использутся классом map для отрисовки блока
    def render(self, x, y, screen):
        screen.blit(self.texture, (x, y))

    # при наступлении на блок черепашка вызывает этот метод. Может быть использован для обновления параметров черепашки
    def block_event(self):
        return None
