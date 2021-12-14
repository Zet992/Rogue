import pygame

from decorations import TreeSpruce
from entities import Player, Enemy2
from interface import Button
from location import Location, WINDOW_SIZE

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Rogue")

transparent_game_menu_background = pygame.Surface((WINDOW_SIZE[0], WINDOW_SIZE[1]), pygame.SRCALPHA)
transparent_game_menu_background.fill((0, 0, 0, 128))

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

# Меню при нажатии на esc
esc_menu = False

clock = pygame.time.Clock()
player = Player(200, 200, 54, 72)
location = Location("arena.txt")
bullets = []
enemies = []
enemies.append(Enemy2(800, 200, 50, 50))

# Button functions
main_menu_buttons = []
choose_save_menu_buttons = []
game_menu_buttons = []


def start_game():
    global main_menu, running
    main_menu = False


def open_help_menu():
    print('Help menu have not created yet')


def open_choose_save_menu():
    global choose_save_menu, main_menu
    choose_save_menu = True
    main_menu = False


def read_first_save():
    global running, choose_save_menu
    running = True
    choose_save_menu = False


def back_to_menu():
    global choose_save_menu, main_menu
    choose_save_menu = False
    main_menu = True


def continue_game():
    global game_menu, running
    game_menu = False
    running = True


def quit_game():
    global game_menu, main_menu, running
    main_menu = True
    game_menu = False
    running = False


# Buttons
play_button = Button(screen, WINDOW_SIZE[0] // 2 - 100, WINDOW_SIZE[1] // 2 - 92,
                     200, 46, 'Играть', open_choose_save_menu)
main_menu_buttons.append(play_button)

help_button = Button(screen, WINDOW_SIZE[0] // 2 - 100, WINDOW_SIZE[1] // 2 - 20,
                     200, 46, 'Помощь', open_help_menu)
main_menu_buttons.append(help_button)

first_save_button = Button(screen, WINDOW_SIZE[0] // 2 - 100, WINDOW_SIZE[1] // 3,
                           200, 46, 'Игра #1', read_first_save)
choose_save_menu_buttons.append(first_save_button)

second_save_button = Button(screen, WINDOW_SIZE[0] // 2 - 100, WINDOW_SIZE[1] // 3 + 92,
                            200, 46, 'Игра #2', read_first_save)
choose_save_menu_buttons.append(second_save_button)

third_save_button = Button(screen, WINDOW_SIZE[0] // 2 - 100, WINDOW_SIZE[1] // 3 + 184,
                           200, 46, 'Игра #3', read_first_save)
choose_save_menu_buttons.append(third_save_button)

back_save_menu_button = Button(screen, WINDOW_SIZE[0] // 2 - 100, WINDOW_SIZE[1] // 3 + 272, 200, 46, 'Назад',
                               back_to_menu)

choose_save_menu_buttons.append(back_save_menu_button)

continue_button = Button(screen, WINDOW_SIZE[0] // 2 - 200, WINDOW_SIZE[1] // 2 - 46, 400, 46, 'Продолжить',
                         continue_game)
game_menu_buttons.append(continue_button)

quit_button = Button(screen, WINDOW_SIZE[0] // 2 - 200, WINDOW_SIZE[1] // 2 + 46, 400, 46, 'Выйти в меню', quit_game)
game_menu_buttons.append(quit_button)
# Decorations

background = pygame.image.load('data\\images\\environment\\environment.jpg')


def draw(screen, background):
    screen.blit(background, (0, 0))


FONT = pygame.font.SysFont("arial", 20)

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
            pygame.quit()
    if main_menu:
        pass
        #pygame.mixer.music.load("data/sounds/M.O.O.N. - Hydrogen.mp3")
        #pygame.mixer.music.play()
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
        #pygame.mixer.music.load("data/sounds/DOOM.mp3")
        #pygame.mixer.music.play()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                main = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bullets.append(player.shot(location.scroll))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_menu = True
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
            player.draw(screen, location.scroll)

            for enemy in enemies:
                enemy.draw(screen, location.scroll)
            for wall in location.walls:
                wall.draw(screen, location.scroll)
            for bullet in bullets[:]:
                bullet.draw(screen, location.scroll)
            screen.blit(transparent_game_menu_background, (0, 0))
            for button in game_menu_buttons:
                button.draw()

            pygame.display.flip()
            clock.tick(60)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            player.move[0] = 7
            player.run = True
            player.idle = False
            player.right = True
            player.left = False
        if keys[pygame.K_a]:
            player.move[0] = -7
            player.idle = False
            player.run = True
            player.left = True
            player.right = False
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            player.move[0] = 0
            if not player.is_jump:
                player.idle = True
            if player.is_jump:
                player.idle = False
            player.run = False
        if keys[pygame.K_SPACE] and player.collision['bottom']:
            player.run = False
            player.idle = False
            player.is_jump = True
        if keys[pygame.K_a] and keys[pygame.K_d]:
            player.move[0] = 0
            player.idle = True
            player.run = False
        if player.is_jump:
            player.jump()

        screen.fill((0, 0, 0))
        draw(screen, background)
        player.check_collision_with_objects(location.walls)
        player.update()
        player.draw(screen, location.scroll)

        for bullet in bullets[:]:
            bullet.update()
            bullet.draw(screen, location.scroll)
            if bullet.x > location.size[0]:
                bullets.remove(bullet)
            elif bullet.y > location.size[1]:
                bullets.remove(bullet)
            elif bullet.x + bullet.width < 0:
                bullets.remove(bullet)
            elif bullet.y + bullet.height < 0:
                bullets.remove(bullet)
            enemy = bullet.check_collisions_with_entity(enemies)
            if enemy:
                enemies.remove(enemy)
                bullets.remove(bullet)

        for enemy in enemies:
            enemy.find_player(player)
            enemy.update()
            enemy.draw(screen, location.scroll)

        for wall in location.walls:
            wall.draw(screen, location.scroll)

        follow = FONT.render(str(round(clock.get_fps())), True, (255, 255, 0))
        screen.blit(follow, (WINDOW_SIZE[0] - 30, 10))

        location.update_scroll(player)
        pygame.display.flip()
        clock.tick(60)
