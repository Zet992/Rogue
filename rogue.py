import pygame

from entities import Player, Enemy1


pygame.init()
size = width, height = 1024, 576
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rogue")

running = True
clock = pygame.time.Clock()
player = Player(200, 200, 50, 50)
bullets = []
enemies = []
enemies.append(Enemy1(800, 200, 50, 50))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullets.append(player.shot())
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
