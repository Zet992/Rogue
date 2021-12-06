import pygame

from entities import Player

pygame.init()
size = width, height = 1024, 576
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rogue")
x, y = 150, 150

running = True
clock = pygame.time.Clock()
player = Player(200, 200, 50, 50)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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
    player.update()
    player.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
