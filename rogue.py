import random

import pygame

from settings import WINDOW_SIZE
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Rogue")

from decorations import MoneyBonus, HealthBonus
from entities import Player, EnemySoldier, Particle, Boss
from entities import run_player_45, run_player_70, run_player_90, run_player_120, run_player_150
from entities import jump_player_45, jump_player_70, jump_player_90, jump_player_120, jump_player_150
from entities import idle_player_45, idle_player_70, idle_player_90, idle_player_120, idle_player_150
from entities import idle_player_180, idle_enemy_soldier, run_enemy_soldier, boss
from interface import Button, HealthBar, MoneyCounter
from location import Location, tiles


transparent_game_menu_background = pygame.Surface((WINDOW_SIZE[0], WINDOW_SIZE[1]), pygame.SRCALPHA)
transparent_game_menu_background.fill((0, 0, 0, 128))

font = pygame.font.Font(None, 70)
game_over_title = font.render('ВЫ УМЕРЛИ', 1, 'red')
game_over_title_rect = game_over_title.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))

win_title = font.render('ВЫ ПОБЕДИЛИ', 1, 'green')
win_title_rect = win_title.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))

font = pygame.font.Font(None, 31)
advice_title = font.render('Нажмите ПРОБЕЛ, чтобы продолжить', 1, 'yellow')
advice_title_rect = advice_title.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 80))

win_sound = pygame.mixer.Sound('data\\sounds\\win\\win.wav')
defeat_sound = pygame.mixer.Sound('data\\sounds\\defeat\\defeat.wav')

health_bar = HealthBar()
money_counter = MoneyCounter()

# Главный цикл, включающий все остальные циклы
main = True

# Главное меню
main_menu = True

# Внутриигровое меню
game_menu = False

# Меню выбора сохранений
choose_save_menu = False

# Игровой процесс
running = False

# Меню, при победе Босса
win_menu = False

# Меню после смерти игрока
game_over_menu = False

clock = pygame.time.Clock()
location = Location("1.txt")
bullets = []
enemy_bullets = []
enemies = []
particles = []
bonuses = []
player_location = []

with open(file='data\\saves\\starter_enemies.txt') as starter_enemies_file:
    starter_enemies = starter_enemies_file.read().replace('\n', '')


def draw_enemies(enemies, surface):
    global location
    for enemy in enemies:
        if enemy.location == player.location:
            enemy.draw(surface, location.scroll)


def update_enemies(enemies):
    global location
    for enemy in enemies:
        if enemy.location == player.location:
            enemy.check_collision_with_objects(location.walls)
            enemy.update()
            enemy.ai(player)


def draw_bonuses(bonuses, surface):
    global location, player
    for bonus in bonuses:
        if bonus.location == player.location:
            bonus.draw(surface, location.scroll)


def update_bonuses(bonuses):
    global location
    for bonus in bonuses:
        if bonus.location == player.location:
            bonus.draw(screen, location.scroll)
            if bonus.check_collision_with_player(player):
                bonuses.remove(bonus)


# Button functions
main_menu_buttons = []
choose_save_menu_buttons = []
game_menu_buttons = []
save = list()


def start_game():
    global main_menu, running
    main_menu = False


def open_help_menu():
    print('Help menu has not created yet')


def open_choose_save_menu():
    global choose_save_menu, main_menu
    choose_save_menu = True
    main_menu = False


def read_save(n):
    global running, choose_save_menu, player_location, save, enemies, bonuses
    running = True
    choose_save_menu = False
    with open(file=f'data\\saves\\save_{n}.txt', mode='r', encoding='utf-8') as save_file:
        data = save_file.read().split('\n')
        location = data[0].split()[-1]
        hp = int(data[1].split()[-1])
        x = float(data[2].split()[-1])
        y = float(data[3].split()[-1])
        money = int(data[4].split()[-1])
        player = Player(x, y, 40, 86, int(location), (0, 0), hp)
        player.money = money

        enemies_temp = data[5].split('; ')

        if enemies_temp != ['None']:
            for enemy in enemies_temp:
                enemies.append(eval(enemy))
        else:
            enemies = []

        bonuses_temp = data[6].split('; ')

        if bonuses_temp != ['None']:
            for bonus in bonuses_temp:
                bonuses.append(eval(bonus))
        else:
            bonuses = []

        location = Location(f'{location}.txt')
        player_location = [player, location]
        save = [n]


def back_to_menu():
    global choose_save_menu, main_menu
    choose_save_menu = False
    main_menu = True


def continue_game():
    global game_menu, running
    game_menu = False
    running = True


def quit_game():
    global game_menu, main_menu, running, save, player, location
    main_menu = True
    game_menu = False
    running = False
    with open(file=f'data\\saves\\save_{save[0]}.txt', encoding='utf-8', mode='w') as save_file:
        loc = location.name.split('.')[0]
        enemies_line = 'None'
        if enemies:
            enemies_line = ''
            for enemy in enemies:
                if type(enemy) == EnemySoldier:
                    enemies_line += f'{enemy}({enemy.x}, {enemy.y}, {enemy.width}, {enemy.height}, {enemy.location}, {enemy.hp}, {enemy.move})'
                if type(enemy) == Boss:
                    enemies_line += f'{enemy}({enemy.x}, {enemy.y}, {enemy.width}, {enemy.height}, {enemy.location}, {enemy.hp}, [0, 0])'

                if enemy is not enemies[-1]:
                    enemies_line += '; '
            enemies.clear()
            bullets.clear()
            enemy_bullets.clear()

        bonuses_line = 'None'
        if bonuses:
            bonuses_line = ''
            for bonus in bonuses:
                if bonuses[-1] is not bonus:
                    bonuses_line += f'{bonus}({bonus.x}, {bonus.y}, {bonus.location}); '
                else:
                    bonuses_line += f'{bonus}({bonus.x}, {bonus.y}, {bonus.location})'
        save_file.write(
            f'location: {loc}\nhp: {player.hp}\nx: {player.x}\ny: {player.y}\nmoney: {player.money}\n{enemies_line}\n{bonuses_line}')
        bonuses.clear()


# Buttons
play_button = Button(screen, WINDOW_SIZE[0] // 2 - 100, WINDOW_SIZE[1] // 2 - 92,
                     200, 46, 'Играть', open_choose_save_menu)
main_menu_buttons.append(play_button)

help_button = Button(screen, WINDOW_SIZE[0] // 2 - 100, WINDOW_SIZE[1] // 2 - 20,
                     200, 46, 'Помощь', open_help_menu)
main_menu_buttons.append(help_button)

first_save_button = Button(screen, WINDOW_SIZE[0] // 2 - 100, WINDOW_SIZE[1] // 3,
                           200, 46, 'Игра #1', lambda: read_save(1))
choose_save_menu_buttons.append(first_save_button)

second_save_button = Button(screen, WINDOW_SIZE[0] // 2 - 100, WINDOW_SIZE[1] // 3 + 92,
                            200, 46, 'Игра #2', lambda: read_save(2))
choose_save_menu_buttons.append(second_save_button)

third_save_button = Button(screen, WINDOW_SIZE[0] // 2 - 100, WINDOW_SIZE[1] // 3 + 184,
                           200, 46, 'Игра #3', lambda: read_save(3))
choose_save_menu_buttons.append(third_save_button)

back_save_menu_button = Button(screen, WINDOW_SIZE[0] // 2 - 100, WINDOW_SIZE[1] // 3 + 272, 200, 46, 'Назад',
                               back_to_menu)

choose_save_menu_buttons.append(back_save_menu_button)

continue_button = Button(screen, WINDOW_SIZE[0] // 2 - 200, WINDOW_SIZE[1] // 2 - 46, 400, 46, 'Продолжить',
                         continue_game)
game_menu_buttons.append(continue_button)

quit_button = Button(screen, WINDOW_SIZE[0] // 2 - 200, WINDOW_SIZE[1] // 2 + 46, 400, 46, 'Сохранить и выйти',
                     quit_game)
game_menu_buttons.append(quit_button)
# Decorations

background = pygame.image.load('data\\images\\environment\\environment.jpg')


def draw(screen, background):
    screen.blit(background, (0, 0))


def create_jump_particles(player):
    count = 20
    for _ in range(count):
        particles.append(Particle(player.x + player.width // 2, player.y + player.height, 5, 5,
                                  move=[random.randint(-7, 7), random.randint(0, 1)],
                                  ticks=10))
    return particles


def create_blood_particles(x, y, collision):
    count = 50
    for _ in range(count):
        if collision == 'r':
            move_x = random.randint(2, 5)
        else:
            move_x = random.uniform(-5, 2)
        particles.append(Particle(x, y, 5, 5,
                                  move=[move_x, random.uniform(-3, 3)],
                                  ticks=10, physics=False, color=(255, 0, 0)))
    return particles


def create_shot_particles(player):
    pass


def create_dash_particles(player):
    pass


FONT = pygame.font.SysFont("arial", 20)

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
            pygame.quit()
    if main_menu:
        pass
        # pygame.mixer.music.load("data/sounds/M.O.O.N. - Hydrogen.mp3")
        # pygame.mixer.music.play()
    while main_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu = False
                main = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x_cursor, y_cursor = event.pos
                    for button in main_menu_buttons:
                        if button.check_click(x_cursor, y_cursor):
                            button.clicked()
            if event.type == pygame.MOUSEMOTION:
                for button in main_menu_buttons:
                    x_cursor, y_cursor = event.pos
                    button.check_hover(x_cursor, y_cursor)

        screen.fill((0, 0, 0))
        draw(screen, background)

        for button in main_menu_buttons:
            button.draw()

        pygame.display.flip()
        clock.tick(60)

    while choose_save_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                choose_save_menu = False
                main_menu = True
                main = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_cursor, y_cursor = event.pos
                for button in choose_save_menu_buttons:
                    if button.check_click(x_cursor, y_cursor):
                        button.clicked()
                        player, location = player_location
            if event.type == pygame.MOUSEMOTION:
                for button in choose_save_menu_buttons:
                    x_cursor, y_cursor = event.pos
                    button.check_hover(x_cursor, y_cursor)

        screen.fill((0, 0, 0))

        draw(screen, background)

        for button in choose_save_menu_buttons:
            button.draw()
        pygame.display.flip()
        clock.tick(60)

    if running:
        pass
        # pygame.mixer.music.load("data/sounds/DOOM.mp3")
        # pygame.mixer.music.play()

    while game_over_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_menu = False
                main = False
                running = False
                game_over_menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                    with open(file=f'data\\saves\\save_{save[0]}.txt', encoding='utf-8', mode='w') as save_file:
                        save_file.write(
                            f'location: 1\nhp: 100\nx: 300\ny: 300\nmoney: 0\n{starter_enemies}\nNone')
                    game_menu = False
                    running = False
                    game_over_menu = False
                    main_menu = True
                    enemies.clear()
                    enemy_bullets.clear()
                    bonuses.clear()
                    bullets.clear()
        screen.fill('black')
        screen.blit(game_over_title, game_over_title_rect)
        screen.blit(advice_title, advice_title_rect)
        pygame.display.flip()
        clock.tick(60)

    while win_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_menu = False
                win_menu = False
                main = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                    with open(file=f'data\\saves\\save_{save[0]}.txt', encoding='utf-8', mode='w') as save_file:
                        save_file.write(
                            f'location: 1\nhp: 100\nx: 300\ny: 300\nmoney: 0\n{starter_enemies}\nNone')
                    game_menu = False
                    running = False
                    game_over_menu = False
                    main_menu = True
                    enemies.clear()
                    enemy_bullets.clear()
                    bonuses.clear()
                    bullets.clear()
                    win_menu = False
        screen.fill('black')
        screen.blit(win_title, win_title_rect)
        screen.blit(advice_title, advice_title_rect)
        pygame.display.flip()
        clock.tick(60)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                main = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player.shooting = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    player.shooting = False
                    player.shooting = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_menu = True
                elif event.key == pygame.K_SPACE:
                    if player.collision['bottom']:
                        player.jump_tick = 20
                        player.jumps = 1
                        player.run = False
                        player.idle = False
                        particles.extend(create_jump_particles(player))
                    elif player.jumps != 2 and player.jump_tick < 15:
                        player.jump_tick = 18
                        player.fall_count = 1
                        player.jumps = 2
                        player.run = False
                        player.idle = False
                        particles.extend(create_jump_particles(player))
                elif event.key == pygame.K_LCTRL:
                    player.dash()

        if player.shooting:
            player.shooting_tick += 1
            if player.shooting_tick % 15 == 0:
                bullets.append(player.shot(location.scroll))

        x, y = pygame.mouse.get_pos()
        if x >= player.x + player.width // 2 - location.scroll[0]:
            player.right = True
            player.left = False
        elif x < player.x + player.width // 2 - location.scroll[0]:
            player.left = True
            player.right = False

        while game_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_menu = False
                    main = False
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x_cursor, y_cursor = event.pos
                    for button in game_menu_buttons:
                        if button.check_click(x_cursor, y_cursor):
                            button.clicked()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        continue_game()
                if event.type == pygame.MOUSEMOTION:
                    for button in game_menu_buttons:
                        x_cursor, y_cursor = event.pos
                        button.check_hover(x_cursor, y_cursor)
            screen.fill('black')
            draw(screen, background)
            location.update_scroll(player)
            player.check_collision_with_objects(location.walls)

            draw_bonuses(bonuses, screen)

            draw_enemies(enemies, screen)

            for bullet in enemy_bullets:
                if bullet.location == player.location:
                    bullet.draw(screen, location.scroll)
                else:
                    enemy_bullets.remove(bullet)

            for wall in location.walls:
                wall.draw(screen, location.scroll)
            for bullet in bullets[:]:
                bullet.draw(screen, location.scroll)
            player.draw(screen, location.scroll)
            screen.blit(transparent_game_menu_background, (0, 0))
            for button in game_menu_buttons:
                button.draw()
            pygame.display.flip()
            clock.tick(60)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and player.dash_count == 0:
            player.move[0] = 7
            player.run = True
            player.idle = False
        if keys[pygame.K_a]:
            player.move[0] = -7
            player.idle = False
            player.run = True
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            player.move[0] = 0
            if not player.jumps:
                player.idle = True
            if player.jumps:
                player.idle = False
            player.run = False
        if keys[pygame.K_a] and keys[pygame.K_d]:
            player.move[0] = 0
            player.idle = True
            player.run = False
        if player.jumps:
            player.jump()
        if player.dash_count != 0:
            if player.left:
                player.move[0] = -35
            else:
                player.move[0] = 35
            player.dash_count -= 1
        if not player.collision['bottom'] and player.jump_tick == -1 and player.dash_count == 0:
            player.move[1] = player.fall_count ** 2 / 10
            if player.fall_count < 15:
                player.fall_count += 1

        screen.fill((0, 0, 0))
        draw(screen, background)
        player.check_collision_with_objects(location.walls)
        player.update()
        player.location = int(location.name.split('.')[0])

        if player.hp <= 0:
            defeat_sound.play()
            main_menu = False
            running = False
            game_over_menu = True

        for bullet in enemy_bullets:
            bullet_removed = False
            if bullet.location == player.location:
                bullet.draw(screen, location.scroll)
                bullet.update()
                if bullet.living_tick == 400:
                    enemy_bullets.remove(bullet)
                    bullet_removed = True
                if bullet.x > location.size[0]:
                    enemy_bullets.remove(bullet)
                    bullet_removed = True
                elif bullet.y > location.size[1]:
                    enemy_bullets.remove(bullet)
                    bullet_removed = True
                elif bullet.x + bullet.width < 0:
                    enemy_bullets.remove(bullet)
                    bullet_removed = True
                elif bullet.y + bullet.height < 0:
                    enemy_bullets.remove(bullet)
                    bullet_removed = True
                if not bullet_removed:
                    if bullet.check_collisions_with_player(player):
                        if player.move[0] - bullet.move[0] > 0:
                            collision = 'r'
                            pos_x = bullet.x
                        else:
                            collision = 'l'
                            pos_x = bullet.x + bullet.width
                        particles.extend(create_blood_particles(pos_x, bullet.y + bullet.height // 2,
                                                                collision))
                        enemy_bullets.remove(bullet)
                    wall = bullet.check_collision_with_walls(location.walls)
                    if wall:
                        enemy_bullets.remove(bullet)
            else:
                enemy_bullets.remove(bullet)

        for bullet in bullets[:]:
            if bullet.location == player.location:
                bullet.draw(screen, location.scroll)
                bullet.update()
                bullet_removed = False
                if bullet.living_tick >= 85:
                    bullets.remove(bullet)
                    bullet_removed = True
                if bullet.x > location.size[0] and not bullet_removed:
                    bullets.remove(bullet)
                    bullet_removed = True
                elif bullet.y > location.size[1] and not bullet_removed:
                    bullets.remove(bullet)
                    bullet_removed = True
                elif bullet.x + bullet.width < 0 and not bullet_removed:
                    bullets.remove(bullet)
                    bullet_removed = True
                elif bullet.y + bullet.height < 0 and not bullet_removed:
                    bullets.remove(bullet)
                    bullet_removed = True
                if not bullet_removed:
                    enemy = bullet.check_collisions_with_entity(enemies)
                    if enemy:
                        enemy.hp -= random.randrange(35, 60)
                        if type(enemy) == Boss:
                            if enemy.hp <= 0:
                                enemies.remove(enemy)
                                win_menu = True
                                running = False
                                main_menu = False
                                choose_save_menu = False
                                win_sound.play()
                        if enemy.hp <= 0 and type(enemy) != Boss:
                            enemies.remove(enemy)
                            chance = random.randrange(1, 6, 1)
                            if chance == 1:
                                bonuses.append(HealthBonus(enemy.x, enemy.y, enemy.location))
                            elif chance in (2, 3, 4):
                                bonuses.append(MoneyBonus(enemy.x, enemy.y, enemy.location))
                        bullets.remove(bullet)
                    wall = bullet.check_collision_with_walls(location.walls)
                    if wall:
                        bullets.remove(bullet)

        draw_bonuses(bonuses, screen)
        update_bonuses(bonuses)

        for wall in location.walls:
            wall.draw(screen, location.scroll)

        for tp_zone in location.tp_zones:
            if player.rect.colliderect(location.tp_zones[tp_zone]):
                old_name = location.name[:-4]  # remove .txt
                d_x = player.x - location.tp_zones[tp_zone].x
                d_y = player.y - location.tp_zones[tp_zone].y
                location = Location(f'{tp_zone[:-1]}.txt')
                print(tp_zone)
                for new_tp_zone in location.tp_zones:
                    if new_tp_zone[:-1] == old_name:
                        position = new_tp_zone[-1]
                        tp_rect = location.tp_zones[new_tp_zone]
                        if position == 'l':
                            player.x = tp_rect.x - player.width - 10
                            if d_y < 0 or d_y > tp_rect.height:
                                player.y = tp_rect.bottom - player.height - 3
                            else:
                                player.y = tp_rect.y + d_y
                        elif position == 'r':
                            player.x = tp_rect.right + 10
                            if d_y < 0 or d_y > tp_rect.height:
                                player.y = tp_rect.bottom - player.height - 3
                            else:
                                player.y = tp_rect.y + d_y
                        elif position == 'd':
                            player.x = tp_rect.x + d_x
                            player.y = tp_rect.bottom + 1
                        elif position == 'u':
                            player.y = tp_rect.y - player.height - 10
                            player.jump_tick = 10
                            player.jumps = 2
                            if player.move[0] < 0:
                                player.x = tp_rect.x - player.width - 10
                                break
                            else:
                                player.x = tp_rect.right + 10
                        break
                break

        if enemies:
            for enemy in enemies:
                if type(enemy) == EnemySoldier:
                    if enemy.engaging_tick % 25 == 0:
                        enemy_bullets.extend(enemy.shot())
                if type(enemy) == Boss:
                    if enemy.location == player.location:
                        if enemy.engaging_tick % 20 == 0:
                            enemy_bullets.extend(enemy.shot())

            update_enemies(enemies)
            draw_enemies(enemies, screen)

        for particle in particles:
            particle.update()
            particle.draw(screen, location.scroll)
            if particle.ticks < 0:
                particles.remove(particle)

        follow = FONT.render(str(round(clock.get_fps())), True, (255, 255, 0))
        screen.blit(follow, (WINDOW_SIZE[0] - 30, 10))
        player.draw(screen, location.scroll)
        health_bar.draw(screen, player.hp)
        money_counter.draw(screen, player.money)
        location.update_scroll(player)
        pygame.display.flip()
        clock.tick(60)
