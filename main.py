import pygame
import sys


pygame.init()
size = width, height = 1408, 640
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True

fon = pygame.image.load('assets\\texture\\fon.png')
turtleimg = [pygame.transform.rotate(pygame.image.load('assets\\texture\\Turtle\\Turtle_' + str(i) + '.png'), 270) for i in
          range(1, 9)]
plotimg = [pygame.transform.rotate(pygame.image.load('assets\\texture\\entity\\plot_' + str(i) + '.png'), 270) for i in
           range(1, 3)]
turt = pygame.transform.rotate(pygame.image.load('assets\\texture\\Turtle\\Turtle_1.png'), 270)


def start_screen():
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
        if x < -750 and x > -2670:
            screen.blit(plotimg[int((c % 7) // 4)], (280, 300))
            screen.blit(turt, (300, 300))
        else:
            screen.blit(turtleimg[int(c // 3.8)], (300, 300))
        pygame.display.flip()


start_screen()
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
