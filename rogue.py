import pygame

from decorations import TreeSpruce, BackGroundSky, BackGroundGrass
from interface import Button
from entities import Player, Enemy1, Enemy2
from location import Location, WINDOW_SIZE

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
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
location = Location("arena.txt")
bullets = []
enemies = []
enemies.append(Enemy2(800, 200, 50, 50))

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

# Decorations
background_elements = list()
sky = BackGroundSky(screen, WINDOW_SIZE[0], WINDOW_SIZE[1])
background_elements.append(sky)
grass = BackGroundGrass(screen, WINDOW_SIZE[0], WINDOW_SIZE[1])
background_elements.append(grass)

decorations = list()
tree = TreeSpruce(screen, 50, WINDOW_SIZE[1] - 70)
decorations.append(tree)
tree = TreeSpruce(screen, WINDOW_SIZE[0] - 200, WINDOW_SIZE[1] - 130)
decorations.append(tree)
tree = TreeSpruce(screen, 230, WINDOW_SIZE[1] - 170)
decorations.append(tree)

pygame.mixer.music.load("data/sounds/M.O.O.N. - Hydrogen.mp3")
pygame.mixer.music.play()
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

    screen.fill((0, 0, 0))

    for background_element in background_elements:
        background_element.draw()

    for decoration in decorations:
        decoration.draw()

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

    screen.fill((0, 0, 0))

    for background_element in background_elements:
        background_element.draw()

    for decoration in decorations:
        decoration.draw()

    for button in choose_save_menu_buttons:
        button.draw()
    pygame.display.flip()
    clock.tick(60)

FONT = pygame.font.SysFont("arial", 20)
pygame.mixer.music.load("data/sounds/DOOM.mp3")
pygame.mixer.music.play()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bullets.append(player.shot(location.scroll))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player.move[0] = 7
    if keys[pygame.K_a]:
        player.move[0] = -7
    if not keys[pygame.K_a] and not keys[pygame.K_d]:
        player.move[0] = 0
    if keys[pygame.K_SPACE] and player.collision['bottom']:
        print(1)
        player.is_jump = True
        player.jumps = 1
    if keys[pygame.K_SPACE] and player.jumps < 2 and player.jump_count < 15:
        print(2)
        player.jump_count = 20
        player.jumps = 2
    if keys[pygame.K_a] and keys[pygame.K_d]:
        player.move[0] = 0
    if player.is_jump:
        player.jump()

    screen.fill((0, 0, 0))
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

pygame.quit()
