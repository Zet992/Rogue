import pygame

from entities import Player, Enemy1
from interface import Button

pygame.init()
size = width, height = 1024, 576
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rogue")

# Главное меню
main_menu = True

# Меню выбора сохранений
choose_save_menu = False

# Игровой процесс
running = False

# Меню при нажатии на esc
esc_menu = False

clock = pygame.time.Clock()
player = Player(200, 200, 50, 50)
bullets = []
enemies = []
enemies.append(Enemy1(800, 200, 50, 50))

# Button functions

main_menu_buttons = []
choose_save_menu_buttons = []


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


##############################################################################################

# Buttons
play_button = Button(screen, width // 2 - 100, height // 2 - 92, 200, 46, 'Играть', open_choose_save_menu)
main_menu_buttons.append(play_button)

help_button = Button(screen, width // 2 - 100, height // 2 - 20, 200, 46, 'Помощь', open_help_menu)
main_menu_buttons.append(help_button)

# Все три кнопки сейчас указывают только на один сейв
first_save_button = Button(screen, width // 2 - 100, height // 3, 200, 46, 'Игра #1', read_first_save)
choose_save_menu_buttons.append(first_save_button)

second_save_button = Button(screen, width // 2 - 100, height // 3 + 92, 200, 46, 'Игра #2', read_first_save)
choose_save_menu_buttons.append(second_save_button)

third_save_button = Button(screen, width // 2 - 100, height // 3 + 184, 200, 46, 'Игра #3', read_first_save)
choose_save_menu_buttons.append(third_save_button)

#############################################################################################################

while main_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_menu = False
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

    screen.fill((80, 80, 80))

    for button in main_menu_buttons:
        button.draw()
    pygame.display.flip()
    clock.tick(60)

while choose_save_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            choose_save_menu = False
            main_menu = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_cursor, y_cursor = event.pos
            for button in choose_save_menu_buttons:
                if button.check_click(x_cursor, y_cursor):
                    button.clicked()
        if event.type == pygame.MOUSEMOTION:
            for button in choose_save_menu_buttons:
                x_cursor, y_cursor = event.pos
                button.check_hover(x_cursor, y_cursor)

    screen.fill((80, 80, 80))
    for button in choose_save_menu_buttons:
        button.draw()
    pygame.display.flip()
    clock.tick(60)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bullets.append(player.shot())

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player.move[0] = 7
    if keys[pygame.K_a]:
        player.move[0] = -7
    if not keys[pygame.K_a] and not keys[pygame.K_d]:
        player.move[0] = 0
    if keys[pygame.K_SPACE]:
        player.is_jump = True
    if keys[pygame.K_a] and keys[pygame.K_d]:
        player.move[0] = 0
    if player.is_jump:
        player.jump()

    screen.fill((0, 0, 0))
    player.update()
    player.draw(screen)

    for bullet in bullets[:]:
        bullet.update()
        bullet.draw(screen)
        if bullet.x > width:
            bullets.remove(bullet)
        if bullet.y > height:
            bullets.remove(bullet)
        if bullet.x + bullet.width < 0:
            bullets.remove(bullet)
        if bullet.y + bullet.height < 0:
            bullets.remove(bullet)
        enemy = bullet.check_collisions_with_entity(enemies)
        if enemy:
            enemies.remove(enemy)
            bullets.remove(bullet)

    for enemy in enemies:
        enemy.find_player(player)
        enemy.update()
        enemy.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
