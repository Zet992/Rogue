import pygame

from entities import Player


pygame.init()
size = width, height = 1024, 576
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rogue")
x, y = 150, 150

running = True
clock = pygame.time.Clock()
player = Player(100, 100, 50, 50)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    player.update()
    player.draw(screen)
    pygame.display.flip()

pygame.quit()
