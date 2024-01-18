import pygame
from pahc_const import path_file


# используется для загрузки изображений со специфичным фоном
def load_sprite(name, color=None):
    img = pygame.image.load(path_file + name)
    if color is not None:
        img = img.convert()
        if color == -1:
            color = img.get_at((0, 0))
        img.set_colorkey(color)
    else:
        img = img.convert_alpha()
    return img
