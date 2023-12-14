import pygame
from map import Map


def main():
    size = width, height = 1408, 640
    screen = pygame.display.set_mode(size)
    board = Map(256, 256, screen)

    fps = 60
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(128, 128, 0, 0)
        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Turtle_on_the_island')
    main()
