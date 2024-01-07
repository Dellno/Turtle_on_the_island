import time
import pygame
from map import Map
from entity_map import EntityMap
import sys
from turtle import Turtle
from stone import Stone
from dirt_block import Grass
from paporotnik import Paporotnik
from endurance_crystal import EnduranceCrystal
from health_crystal import HealthCrystal
from ash_block import Ash
from magma_block import Magma
from water_block import Water
from brevno import Brevno
from brevno2 import Brevno_2
from brevno3 import Brevno_3
from brevno4 import Brevno_4
from plot import Plot
from sharp_stone import SharpStone
from stick import Stick
from thread import Thread
from topor import Topor
from tree import Tree


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


def load_game(block_board, entity_board, turtl):
    block_keys = {'#': Ash(), '0': Grass(0), '1': Grass(1),
                  '2': Grass(2), '3': Grass(3), '4': Grass(4),
                  '5': Grass(5), '%': Magma(),
                  '.': Water()}
    entity_keys = {'.': None, '0': Brevno(), '2': Brevno_2(), '3': Brevno_3(),
                   '4': Brevno_4(), '#': EnduranceCrystal(), '$': HealthCrystal(),
                   '%': Paporotnik(), '&': Plot(), '*': SharpStone(), '-': Stick(),
                   's': Stone(), 'd': Thread(), 'f': Topor(), 'g': Tree(), 'h': turtl}
    with open("save/save") as save:
        for y in range(len(block_board.board)):
            keys = save.readline().rstrip('\n')
            line = []
            for x in keys:
                line.append(block_keys[x])
            block_board.board[y] = line
        save.readline()
        for y in range(len(entity_board.board)):
            keys = save.readline().rstrip('\n')
            line = []
            for j, x in enumerate(keys):
                if isinstance(entity_keys[x], Turtle):
                    line.append(None)
                    turt_cords = (j, y)
                else:
                    line.append(entity_keys[x])
            entity_board.board[y] = line
        save.readline()
        turtl.stat["damage"] = int(save.readline().rstrip('\n'))
        turtl.stat["endurance"] = int(save.readline().rstrip('\n'))
        turtl.inventory = entity_keys[save.readline().rstrip('\n')]
        turtl.cords = turt_cords
        turtl.in_plot = bool(int(save.readline().rstrip('\n')))
        entity_board.board[turt_cords[1]][turt_cords[0]] = turtl


def save_game(block_board, entity_board, turtl):
    block_keys = {"ash": "#", "ground_0": "0", "ground_1": "1",
                  "ground_2": "2", "ground_3": "3", "ground_4": "4",
                  "ground_5": "5", "lava": "%", "lava1": "$",
                  "water": "."}
    entity_keys = {None: '.', "brevno": '0', "brevno_2": '2', "brevno_3": '3',
                   "brevno_4": '4', "endurance_crystal": "#", "health_cristal": '$',
                   "paporotnic": "%", "plot": "&", "sharp_stone": "*", "stick": '-',
                   "stone": "s", "thread": "d", "topor": 'f', "tree": 'g',
                   "master_turtle": 'h'}
    with open(f"save/save", "w") as save:
        for y in block_board.board:
            line = ""
            for x in y:
                line += block_keys[x.name]
            line += '\n'
            save.write(line)
        save.write('\n')
        for y in entity_board.board:
            line = ""
            for x in y:
                if x is None:
                    line += entity_keys[x]
                else:
                    line += entity_keys[x.name]

            line += '\n'
            save.write(line)
        save.write('\n')
        save.write(str(turtl.stat["damage"]))
        save.write('\n')
        save.write(str(turtl.stat["endurance"]))
        save.write('\n')
        if turtl.inventory is None:
            save.write(entity_keys[None])
            save.write('\n')
        else:
            save.write(entity_keys[turtl.inventory.name])
            save.write('\n')
        if turtl.in_plot:
            save.write('1')
            save.write('\n')
        else:
            save.write('0')
            save.write('\n')


def main():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    print(screen.get_width(), screen.get_height())
    board = Map(256, 256, screen)
    entity_board = EntityMap(256, 256, screen)
    entity_board.generate_entity(128, 128, 10, 10, 5, Stone(), board, Grass, min_entity=4, max_entity=8)
    entity_board.generate_entity(80, 80, 100, 100, 5, EnduranceCrystal(), board, Grass)
    entity_board.generate_entity(80, 80, 100, 100, 1, HealthCrystal(), board, Grass, min_entity=3, max_entity=6)
    entity_board.generate_entity(140, 128, 20, 20, 10, Tree(), board, Grass, min_entity=10, max_entity=30)

    fps = 30
    clock = pygame.time.Clock()
    start_type = start_screen(screen, clock)
    turt = Turtle(128, 128, board, entity_board)
    running = True
    mouse_pos = (0, 0)
    buttons_pos = [(screen.get_width() // 1.15, 32), (screen.get_width() // 1.15, 128)]
    buttons_k = [0, 0]
    if start_type == 'load':
        load_game(board, entity_board, turt)
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
                    if x1 > buttons_pos[0][0] and x1 < buttons_pos[0][0] + 160 and y1 > buttons_pos[0][1] and y1 < \
                            buttons_pos[0][1] + 64:
                        buttons_k[0] = 1
                    if x1 > buttons_pos[1][0] and x1 < buttons_pos[1][0] + 160 and y1 > buttons_pos[1][1] and y1 < \
                            buttons_pos[1][1] + 64:
                        buttons_k[1] = 1
            else:
                buttons_k[0], buttons_k[1], = 0, 0
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    x1, y1 = event.pos
                    if x1 > buttons_pos[0][0] and x1 < buttons_pos[0][0] + 160 and y1 > buttons_pos[0][1] and y1 < \
                            buttons_pos[0][1] + 64:
                        save_game(board, entity_board, turt)
                        return  # <--> сюда писать то что должна делать кнопка

        if turt.stat["damage"] > 0:
            render_game(screen, board, entity_board, turt, clock, fps, 0, 0, mouse_pos, buttons_pos, buttons_k)
        else:
            died_screen(screen)
            main()


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
    buttons_pos = [(screen.get_width() // 2 - 80, screen.get_height() // 2 - 128),
                   (screen.get_width() // 2 - 80, screen.get_height() // 2),
                   (screen.get_width() // 2 - 80, screen.get_height() // 2 + 128)]
    kk = False
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
                    if x1 > buttons_pos[0][0] and x1 < buttons_pos[0][0] + 160 and y1 > buttons_pos[0][1] and y1 < \
                            buttons_pos[0][1] + 64:
                        buttons_k1 = 1
                    if x1 > buttons_pos[1][0] and x1 < buttons_pos[1][0] + 160 and y1 > buttons_pos[1][1] and y1 < \
                            buttons_pos[1][1] + 64:
                        buttons_k2 = 1
                    if x1 > buttons_pos[2][0] and x1 < buttons_pos[2][0] + 160 and y1 > buttons_pos[2][1] and y1 < \
                            buttons_pos[2][1] + 64:
                        buttons_k3 = 1
            else:
                buttons_k1, buttons_k2, buttons_k3 = 0, 0, 0
            if event.type == pygame.MOUSEBUTTONUP:
                print(screen.get_width(), screen.get_height())
                if event.button == 1:
                    x1, y1 = event.pos
                    if x1 > buttons_pos[0][0] and x1 < buttons_pos[0][0] + 160 and y1 > buttons_pos[0][1] and y1 < \
                            buttons_pos[0][1] + 64:
                        return 'new'
                    if x1 > buttons_pos[1][0] and x1 < buttons_pos[1][0] + 160 and y1 > buttons_pos[1][1] and y1 < \
                            buttons_pos[1][1] + 64:
                        return 'load'
                    if x1 > buttons_pos[2][0] and x1 < buttons_pos[2][0] + 160 and y1 > buttons_pos[2][1] and y1 < \
                            buttons_pos[2][1] + 64:
                        kk = not kk
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
            screen.blit(pygame.image.load('assets/texture/load_game_1.png'), buttons_pos[1])
        else:
            screen.blit(pygame.image.load('assets/texture/load_game.png'), buttons_pos[1])

        if buttons_k3 == 0:
            screen.blit(pygame.image.load('assets/texture/how_to_play.png'), buttons_pos[2])
        else:
            screen.blit(pygame.image.load('assets/texture/how_to_play_1.png'), buttons_pos[2])

        if kk:
            screen.blit(pygame.image.load('assets/texture/explanatory_card.png'), (1000, 100))

        if pygame.mouse.get_focused():
            screen.blit(pygame.image.load('assets/texture/arrow.png'), pos)
        pygame.display.flip()


def died_screen(screen):
    fon = pygame.image.load('assets/texture/died.png')
    buttons_k1, buttons_k2 = 0, 0
    buttons_pos = [(screen.get_width() // 4, screen.get_height() // 1.5),
                   (screen.get_width() // 1.7, screen.get_height() // 1.5), ]
    pygame.mouse.set_visible(False)
    mouse_pos = (0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(screen.get_width(), screen.get_height())
                if event.button == 1:
                    x1, y1 = event.pos
                    if x1 > buttons_pos[0][0] and x1 < buttons_pos[0][0] + 160 and y1 > buttons_pos[0][1] and y1 < \
                            buttons_pos[0][1] + 64:
                        buttons_k1 = 1
                    if x1 > buttons_pos[1][0] and x1 < buttons_pos[1][0] + 160 and y1 > buttons_pos[1][1] and y1 < \
                            buttons_pos[1][1] + 64:
                        buttons_k2 = 1
            else:
                buttons_k1, buttons_k2 = 0, 0
            if event.type == pygame.MOUSEBUTTONUP:
                print(screen.get_width(), screen.get_height())
                if event.button == 1:
                    x1, y1 = event.pos
                    if x1 > buttons_pos[0][0] and x1 < buttons_pos[0][0] + 160 and y1 > buttons_pos[0][1] and y1 < \
                            buttons_pos[0][1] + 64:
                        return 'new'
                    if x1 > buttons_pos[1][0] and x1 < buttons_pos[1][0] + 160 and y1 > buttons_pos[1][1] and y1 < \
                            buttons_pos[1][1] + 64:
                        return 'load'
        screen.fill((0, 0, 0))
        screen.blit(fon, (screen.get_width() // 7, screen.get_height() // 3))
        if buttons_k1 == 0:
            screen.blit(pygame.image.load('assets/texture/new_game.png'), buttons_pos[0])
        else:
            screen.blit(pygame.image.load('assets/texture/new_game_1.png'), buttons_pos[0])

        if buttons_k2 == 0:
            screen.blit(pygame.image.load('assets/texture/load_game_1.png'), buttons_pos[1])
        else:
            screen.blit(pygame.image.load('assets/texture/load_game.png'), buttons_pos[1])
        screen.blit(pygame.image.load('assets/texture/arrow.png'), mouse_pos)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Turtle_on_the_island')
    main()
