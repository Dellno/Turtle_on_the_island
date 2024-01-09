import pygame


def load_sprite(name, color=None):
    img = pygame.image.load(name)
    if color is not None:
        img = img.convert()
        if color == -1:
            color = img.get_at((0, 0))
        img.set_colorkey(color)
    else:
        img = img.convert_alpha()
    return img
