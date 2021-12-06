import pygame

from entities import Player, Enemy1
from location import Location

pygame.init()
size = width, height = 1024, 576
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rogue")
x, y = 150, 150

running = True
clock = pygame.time.Clock()
player = Player(200, 200, 50, 50)
location = Location("arena.txt")
bullets = []
enemies = []
enemies.append(Enemy1(800, 200, 50, 50))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
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

    if player.is_jump:
        player.jump()

    screen.fill((0, 0, 0))
    player.check_collision_with_objects(location.walls)
    player.update()
    player.draw(screen)

    for bullet in bullets[:]:
        bullet.update()
        bullet.draw(screen)
        if bullet.x > width:
            bullets.remove(bullet)
        elif bullet.y > height:
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
        enemy.draw(screen)

    for wall in location.walls:
        wall.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
