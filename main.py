import os
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
from barier import Barier
from ship_map import ShipMap
import ship
import machta_
from dry_bush import Dry_bush


def render_game(screen, board, entity_board, ship_board, turtl, clock, fps, pix_x, pix_y, pos, buttons_pos, buttons_k,
                machta):
    screen.fill((0, 0, 0))
    board.render(turtl.cords[0], turtl.cords[1], pix_x, pix_y)
    ship_board.render(turtl.cords[0], turtl.cords[1], pix_x, pix_y)
    entity_board.render(turtl.cords[0], turtl.cords[1], pix_x, pix_y)
    machta.render(turtl.cords[0], turtl.cords[1], pix_x, pix_y)
    if pygame.mouse.get_focused() and pix_x == 0 and pix_y == 0:
        x, y = pos[0] // 128, pos[1] // 128
        pygame.draw.rect(screen, (255, 255, 255), (x * 128, y * 128, 128, 128), 3)
    if buttons_k[0] == 0:
        screen.blit(pygame.image.load('assets/texture/save.png'), buttons_pos[0])
    else:
        screen.blit(pygame.image.load('assets/texture/save_1.png'), buttons_pos[0])
    if pygame.mouse.get_focused() and pix_x == 0 and pix_y == 0:
        screen.blit(pygame.image.load('assets/texture/arrow.png'), pos)
    pygame.display.flip()
    clock.tick(fps)


def load_game(block_board, entity_board, turtl):
    block_keys = {'#': Ash(), '0': Grass(0), '1': Grass(1),
                  '2': Grass(2), '3': Grass(3), '4': Grass(4),
                  '5': Grass(5), '%': Magma(),
                  '.': Water()}
    entity_keys = {'.': None, '0': Brevno(), '2': Brevno_2(), '3': Brevno_3(), '4': Brevno_4(), '#': EnduranceCrystal(),
                   '$': HealthCrystal(), '%': Paporotnik(), '&': Plot(), '*': SharpStone(), '-': Stick(), 's': Stone(),
                   'd': Thread(), 'f': Topor(), 'g': Tree(), 'h': turtl, '~': Barier(),
                   'Q': ship.Ship_1(), 'W': ship.Ship_2(), 'E': ship.Ship_3(), 'R': ship.Ship_4(), 'T': ship.Ship_5(),
                   'Y': ship.Ship_6(), 'U': ship.Ship_7(), 'I': ship.Ship_8(), 'O': ship.Ship_9(), 'P': ship.Ship_10(),
                   'A': ship.Ship_11(), 'S': ship.Ship_12(), 'D': ship.Ship_13(), 'F': ship.Ship_14(),
                   'G': ship.Ship_15(),
                   'H': ship.Ship_16(), 'J': ship.Ship_17(), 'K': ship.Ship_18(), 'L': ship.Ship_19(),
                   'Z': ship.Ship_20(),
                   'X': ship.Ship_21(), 'C': ship.Ship_22(), 'V': ship.Ship_23(), 'B': ship.Ship_24(), 'u': Dry_bush()}
    if os.path.isfile("save/save"):
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
            turtl.stat['fixed_ship'] = int(save.readline().rstrip('\n'))
            entity_board.board[turt_cords[1]][turt_cords[0]] = turtl

    elif os.path.exists('save'):
        save_game(block_board, entity_board, turtl)
    else:
        os.mkdir('save')
        save_game(block_board, entity_board, turtl)


def save_game(block_board, entity_board, turtl):
    block_keys = {"ash": "#", "ground_0": "0", "ground_1": "1",
                  "ground_2": "2", "ground_3": "3", "ground_4": "4",
                  "ground_5": "5", "lava": "%", "lava1": "$",
                  "water": "."}
    entity_keys = {None: '.', "brevno": '0', "brevno_2": '2', "brevno_3": '3', "brevno_4": '4',
                   "endurance_crystal": "#",
                   "health_cristal": '$', "paporotnic": "%", "plot": "&", "sharp_stone": "*", "stick": '-',
                   "stone": "s",
                   "thread": "d", "topor": 'f', "tree": 'g', "master_turtle": 'h', "barier": '~',
                   'ship_1': 'Q', 'ship_2': 'W', 'ship_3': 'E', 'ship_4': 'R', 'ship_5': 'T', 'ship_6': 'Y',
                   'ship_7': 'U', 'ship_8': 'I', 'ship_9': 'O', 'ship_10': 'P', 'ship_11': 'A', 'ship_12': 'S',
                   'ship_13': 'D', 'ship_14': 'F', 'ship_15': 'G', 'ship_16': 'H', 'ship_17': 'J', 'ship_18': 'K',
                   'ship_19': 'L', 'ship_20': 'Z', 'ship_21': 'X', 'ship_22': 'C', 'ship_23': 'V', 'ship_24': 'B', "dry_bush": 'u'}
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
        save.write(str(turtl.stat['fixed_ship']))
        save.write('\n')


def final_screen(screen, clock):
    fon = pygame.transform.scale(pygame.image.load('assets/texture/final_fon.png'), (screen.get_width() + 300, screen.get_height()))
    ship_im = [pygame.image.load('assets/texture/ship_1.png'), pygame.image.load('assets/texture/ship_2.png')]
    buttons_pos = [(screen.get_width() // 1.15, 32), (screen.get_width() // 1.15, 128)]
    buttons_k = 0
    pygame.mouse.set_visible(False)
    v = 2
    x, y = 0, 0
    pos = (0, 0)
    c = 0
    while True:
        if c == 30:
            c = 0
        c += 1
        pygame.display.flip()
        x += v
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x1, y1 = event.pos
                    if x1 > buttons_pos[0][0] and x1 < buttons_pos[0][0] + 160 and y1 > buttons_pos[0][1] and y1 < \
                            buttons_pos[0][1] + 64:
                        buttons_k = 1
            else:
                buttons_k = 0
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    x1, y1 = event.pos
                    if x1 > buttons_pos[0][0] and x1 < buttons_pos[0][0] + 160 and y1 > buttons_pos[0][1] and y1 < \
                            buttons_pos[0][1] + 64:
                        pygame.quit()
                        sys.exit()
            if event.type == pygame.MOUSEMOTION:
                pos = event.pos
        if x >= screen.get_width() + 300:
            x = 0
        screen.blit(fon, (x - screen.get_width() - 300, y))
        screen.blit(fon, (x, y))

        screen.blit(ship_im[int((c % 7) // 4)], (400, screen.get_height() // 2 - 210))

        if buttons_k == 0:
            screen.blit(pygame.image.load('assets/texture/exit_f.png'), buttons_pos[0])
        else:
            screen.blit(pygame.image.load('assets/texture/exit_f2.png'), buttons_pos[0])

        if pygame.mouse.get_focused():
            screen.blit(pygame.image.load('assets/texture/arrow.png'), pos)




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
            screen.blit(plot_anim[int((c % 7) // 4)], (300, screen.get_height() // 2))
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
            screen.blit(pygame.image.load('assets/texture/explanatory_card.png'), (screen.get_width() - 510,
                                                                                   (screen.get_height() - 700) // 2))

        if pygame.mouse.get_focused():
            screen.blit(pygame.image.load('assets/texture/arrow.png'), pos)
        pygame.display.flip()


def died_screen(screen):
    fon = pygame.image.load('assets/texture/died.png')
    buttons_k1 = 0
    buttons_pos = [(screen.get_width() // 2 - 80, screen.get_height() // 2 + 280)]
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
                if event.button == 1:
                    x1, y1 = event.pos
                    if x1 > buttons_pos[0][0] and x1 < buttons_pos[0][0] + 160 and y1 > buttons_pos[0][1] and y1 < \
                            buttons_pos[0][1] + 64:
                        buttons_k1 = 1
            else:
                buttons_k1 = 0
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    x1, y1 = event.pos
                    if x1 > buttons_pos[0][0] and x1 < buttons_pos[0][0] + 160 and y1 > buttons_pos[0][1] and y1 < \
                            buttons_pos[0][1] + 64:
                        return
        screen.fill((0, 0, 0))
        screen.blit(fon,
                    (screen.get_width() // 2 - fon.get_width() // 2, screen.get_height() // 2 - fon.get_height() // 2))
        if buttons_k1 == 0:
            screen.blit(pygame.image.load('assets/texture/restart.png'), buttons_pos[0])
        else:
            screen.blit(pygame.image.load('assets/texture/restart_1.png'), buttons_pos[0])

        screen.blit(pygame.image.load('assets/texture/arrow.png'), mouse_pos)
        pygame.display.flip()


def main():
    game_time = 0
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    board = Map(256, 256, screen)
    machta_ren = machta_.MachtaMap(256, 256, screen)
    ship_board = ShipMap(256, 256, screen)
    entity_board = EntityMap(256, 256, screen)
    entity_board.generate_entity(128, 128, 10, 10, 5, Stone(), board, Grass, min_entity=4, max_entity=8)
    end_crystal = entity_board.generate_entity(1, 1, 254, 254, 1, EnduranceCrystal(), board, Grass, 40, max_entity=80)
    hp_crystal = entity_board.generate_entity(80, 80, 100, 100, 1, HealthCrystal(), board, Grass, min_entity=3,
                                              max_entity=10)
    entity_board.generate_entity(140, 128, 20, 20, 10, Paporotnik(), board, Grass, min_entity=10, max_entity=30)
    entity_board.generate_entity(120, 140, 20, 20, 5, Tree(), board, Grass, min_entity=30, max_entity=50)
    entity_board.generate_entity(118, 128, 8, 8, 5, Dry_bush(), board, Grass, min_entity=5, max_entity=10)
    c = 1
    for i in range(1, 5):
        for j in range(1, 4):
            ship_board.board[117 + i][112 + j] = eval('ship.Ship_' + str(12 + c) + '()')
            entity_board.board[117 + i][112 + j] = eval('ship.Ship_' + str(c) + '()')
            c += 1
    machta_ren.board[119][113] = ship.Machta()

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
        if game_time >= 36000:
            if end_crystal < 80:
                entity_board.generate_entity(1, 1, 254, 254, 1, EnduranceCrystal(), board, Grass, 70 - end_crystal,
                                             max_entity=70)
            if hp_crystal < 10:
                entity_board.generate_entity(80, 80, 100, 100, 1, HealthCrystal(), board, Grass, 10 - hp_crystal,
                                             max_entity=10)
            game_time = 0
        if turt.stat['fixed_ship'] >= turt.stat['max_fixed_ship']:
            final_screen(screen, clock)
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
                            render_game(screen, board, entity_board, ship_board, turt, clock, fps,
                                        -128 // 8 * i * dx,
                                        -128 // 8 * i * dy, mouse_pos, buttons_pos, buttons_k, machta_ren)
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
                        sys.exit(0)
        if turt.stat["damage"] > 0:
            render_game(screen, board, entity_board, ship_board, turt, clock, fps, 0, 0, mouse_pos, buttons_pos,
                        buttons_k, machta_ren)
            game_time += 1
        else:
            died_screen(screen)
            main()


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Turtle_on_the_island')
    main()
