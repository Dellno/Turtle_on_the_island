import time

import pygame
from map import Map
from entity_map import EntityMap
import sys
from turtle import Turtle
from stone import Stone
from dirt_block import Grass
from tree import Tree
from paporotnik import Paporotnik


def render_game(screen, board, entity_board, turtl, clock, fps, pix_x, pix_y, pos, buttons_pos, buttons_k):
    screen.fill((0, 0, 0))
    board.render(turtl.cords[0], turtl.cords[1], pix_x, pix_y)
    entity_board.render(turtl.cords[0], turtl.cords[1], pix_x, pix_y)
    if buttons_k[0] == 0:
        screen.blit(pygame.image.load('assets/texture/save.png'), buttons_pos[0])
    else:
        screen.blit(pygame.image.load('assets/texture/save_1.png'), buttons_pos[0])
    if pygame.mouse.get_focused() and pix_x == 0 and pix_y == 0:
        x, y = pos[0] // 128, pos[1] // 128
        pygame.draw.rect(screen, (255, 255, 255), (x * 128, y * 128, 128, 128), 3)
        screen.blit(pygame.image.load('assets/texture/arrow.png'), pos)
    pygame.display.flip()
    clock.tick(fps)


def load_game():
    pass


def main():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    print(screen.get_width(), screen.get_height())
    board = Map(256, 256, screen)
    entity_board = EntityMap(256, 256, screen)
    entity_board.generate_entity(128, 128, 10, 10, 10, Stone(), board, Grass)
    entity_board.generate_entity(140, 140, 20, 20, 20, Tree(), board, Grass)
    entity_board.generate_entity(135, 135, 20, 20, 20, Paporotnik(), board, Grass)

    fps = 30
    clock = pygame.time.Clock()
    start_screen(screen, clock)
    turt = Turtle(128, 128, board, entity_board)
    running = True
    mouse_pos = (0, 0)
    buttons_pos = [(screen.get_width() // 1.15, 32), (screen.get_width() // 1.15, 128)]
    buttons_k = [0, 0]
    pygame.mouse.set_visible(False)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = board.get_click(event.pos)
                if event.button == 1:
                    if turt.is_correct_move(x, y):
                        dx = 0
                        dy = 0
                        if x > turt.cords[0]:
                            turt.rotate = 1
                            dx = 1
                            dy = 0
                        if x < turt.cords[0]:
                            turt.rotate = 3
                            dx = -1
                            dy = 0
                        if y > turt.cords[1]:
                            turt.rotate = 2
                            dy = 1
                            dx = 0
                        if y < turt.cords[1]:
                            turt.rotate = 0
                            dy = -1
                            dx = 0
                        for i in range(8):
                            turt.anim_step = i
                            render_game(screen, board, entity_board, turt, clock, fps,
                                        -128 // 8 * i * dx,
                                        -128 // 8 * i * dy, mouse_pos, buttons_pos, buttons_k)
                        turt.anim_step = 0
                        turt.move(x, y)
                        turt.cords = (x, y)
                    else:
                        turt.crafter(x, y)
                if event.button == 3:
                    turt.inventory_move(x, y)
                if event.button == 1:
                    x1, y1 = event.pos
                    if x1 > buttons_pos[0][0] and x1 < buttons_pos[0][0] + 160 and y1 > buttons_pos[0][1] and y1 < buttons_pos[0][1] + 64:
                        buttons_k[0] = 1
                    if x1 > buttons_pos[1][0] and x1 < buttons_pos[1][0] + 160 and y1 > buttons_pos[1][1] and y1 < buttons_pos[1][1] + 64:
                        buttons_k[1] = 1
            else:
                buttons_k[0], buttons_k[1], = 0, 0
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    x1, y1 = event.pos
                    if x1 > buttons_pos[0][0] and x1 < buttons_pos[0][0] + 160 and y1 > buttons_pos[0][1] and y1 < buttons_pos[0][1] + 64:
                        return  # <--> сюда писать то что должна делать кнопка
                    if x1 > buttons_pos[1][0] and x1 < buttons_pos[1][0] + 160 and y1 > buttons_pos[1][1] and y1 < buttons_pos[1][1] + 64:
                        pass  # <-->
        render_game(screen, board, entity_board, turt, clock, fps, 0, 0, mouse_pos, buttons_pos, buttons_k)


def start_screen(screen, clock):
    fon = pygame.transform.scale(pygame.image.load('assets/texture/fon.png'), (5000, screen.get_height()))
    plot_img = pygame.transform.rotate(pygame.image.load('assets/texture/entity/plot.png'), 270)
    turtle_anim = [pygame.transform.rotate(pygame.image.load('assets/texture/turtle/turtle_' + str(i) + '.png'),
                                           270) for i in range(1, 9)]
    plot_anim = [pygame.transform.rotate(pygame.image.load('assets/texture/entity/plot_' + str(i) + '.png'),
                                         270) for i in range(1, 3)]
    turt = pygame.transform.rotate(pygame.image.load('assets/texture/turtle/turtle_1.png'), 270)

    v = -2
    x, y = 0, 0
    c = 0
    pos = (0, 0)
    buttons_k1, buttons_k2, buttons_k3 = 0, 0, 0
    buttons_pos = [(128, screen.get_height() // 2 - 128), (128, screen.get_height() // 2), (128, screen.get_height() // 2 + 128)]
    pygame.mouse.set_visible(False)
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(screen.get_width(), screen.get_height())
                if event.button == 1:
                    x1, y1 = event.pos
                    if x1 > buttons_pos[0][0] and x1 < buttons_pos[0][0] + 160 and y1 > buttons_pos[0][1] and y1 < buttons_pos[0][1] + 64:
                        buttons_k1 = 1
                    if x1 > buttons_pos[1][0] and x1 < buttons_pos[1][0] + 160 and y1 > buttons_pos[1][1] and y1 < buttons_pos[1][1] + 64:
                        buttons_k2 = 1
                    if x1 > buttons_pos[2][0] and x1 < buttons_pos[2][0] + 160 and y1 > buttons_pos[2][1] and y1 < buttons_pos[2][1] + 64:
                        buttons_k3 = 1
            else:
                buttons_k1, buttons_k2, buttons_k3 = 0, 0, 0
            if event.type == pygame.MOUSEBUTTONUP:
                print(screen.get_width(), screen.get_height())
                if event.button == 1:
                    x1, y1 = event.pos
                    if x1 > buttons_pos[0][0] and x1 < buttons_pos[0][0] + 160 and y1 > buttons_pos[0][1] and y1 < buttons_pos[0][1] + 64:
                        return
                    if x1 > buttons_pos[1][0] and x1 < buttons_pos[1][0] + 160 and y1 > buttons_pos[1][1] and y1 < buttons_pos[1][1] + 64:
                        load_game()
                    if x1 > buttons_pos[2][0] and x1 < buttons_pos[2][0] + 160 and y1 > buttons_pos[2][1] and y1 < buttons_pos[2][1] + 64:
                        pass
            if event.type == pygame.MOUSEMOTION:
                pos = event.pos
        if x <= -5000:
            x = 0
        x += v
        if c == 30:
            c = 0
        c += 1
        screen.blit(fon, (x, y))
        screen.blit(fon, (x + 5000, y))

        if x in range(-2670, -800):
            screen.blit(plot_anim[int((c % 7) // 4)], (280, screen.get_height() // 2))
            screen.blit(turt, (300, screen.get_height() // 2))
        else:
            screen.blit(plot_img, (x + 1100, screen.get_height() // 2))
            screen.blit(turtle_anim[int(c // 3.8)], (300, screen.get_height() // 2))
        if buttons_k1 == 0:
            screen.blit(pygame.image.load('assets/texture/new_game.png'), buttons_pos[0])
        else:
            screen.blit(pygame.image.load('assets/texture/new_game_1.png'), buttons_pos[0])

        if buttons_k2 == 0:
            screen.blit(pygame.image.load('assets/texture/download_game.png'), buttons_pos[1])
        else:
            screen.blit(pygame.image.load('assets/texture/download_game_1.png'), buttons_pos[1])

        if buttons_k3 == 0:
            screen.blit(pygame.image.load('assets/texture/how_to_play.png'), buttons_pos[2])
        else:
            screen.blit(pygame.image.load('assets/texture/how_to_play_1.png'), buttons_pos[2])

        if pygame.mouse.get_focused():
            screen.blit(pygame.image.load('assets/texture/arrow.png'), pos)

        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Turtle_on_the_island')
    main()
