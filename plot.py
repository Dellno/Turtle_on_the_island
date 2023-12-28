import pygame
from entity import Entity
from load_sprite import load_sprite


class Plot(Entity):
    def __init__(self):
        super().__init__("plot", sprite="plot.png", hardness=0, weight=0)
        self.anim = [load_sprite("assets/texture/entity/plot_1.png"), load_sprite("assets/texture/entity/plot_2.png")]

    def render(self, x, y, screen, rotate=0, anim_step=None):
        if anim_step is None:
            screen.blit(pygame.transform.rotate(self.img, rotate), (x, y))
        else:
            screen.blit(pygame.transform.rotate(self.anim[anim_step % 2], rotate), (x, y))
