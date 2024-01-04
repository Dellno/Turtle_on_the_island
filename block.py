import pygame


class Block:
    def __init__(self, texture: str, name="block"):
        self.name = name
        self.texture = pygame.image.load(f"assets/texture/ground/{texture}")

    def render(self, x, y, screen):
        screen.blit(self.texture, (x, y))

    def block_event(self):
        return None
