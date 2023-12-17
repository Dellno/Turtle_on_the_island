import pygame
from map import Map
from entity_map import EntityMap


def main():
    size = width, height = 1408, 640
    screen = pygame.display.set_mode(size)
    board = Map(256, 256, screen)
    entity_board = EntityMap(256, 256, screen)
    fps = 60
    clock = pygame.time.Clock()
    start_screen(screen, clock)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(128, 128, 0, 0)
        entity_board.render(128, 128, 0, 0)
        pygame.display.flip()
        clock.tick(fps)


def start_screen(screen, clock):
    fon = pygame.image.load('assets/texture/fon.png')
    plot_img = pygame.transform.rotate(pygame.image.load('assets/texture/entity/plot.png'), 270)
    turtle_anim = [pygame.transform.rotate(pygame.image.load('assets/texture/turtle/turtle_' + str(i) + '.png'),
                                           270) for i in range(1, 9)]
    plot_anim = [pygame.transform.rotate(pygame.image.load('assets/texture/entity/plot_' + str(i) + '.png'),
                                         270) for i in range(1, 3)]
    turt = pygame.transform.rotate(pygame.image.load('assets/texture/turtle/turtle_1.png'), 270)

    v = -2
    x, y = 0, -300
    c = 0
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        if x <= -5000:
            x = 0
        x += v
        if c == 30:
            c = 0
        c += 1
        screen.blit(fon, (x, y))
        screen.blit(fon, (x + 5000, y))

        if x < -800 and x > -2670:
            screen.blit(plot_anim[int((c % 7) // 4)], (280, 300))
            screen.blit(turt, (300, 300))
        else:
            screen.blit(plot_img, (x + 1100, 300))
            screen.blit(turtle_anim[int(c // 3.8)], (300, 300))
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Turtle_on_the_island')
    main()
