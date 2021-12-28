import pygame


class Decoration:
    def __init__(self, surface, x, y):
        self.surface = surface
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 50, 50)


class Box(Decoration):
    def check_collision_with_player(self, player):
        player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
        player_rect.center = player.x, player.y
        if self.rect.colliderect(player_rect):
            return True
        else:
            return False

    def draw(self):
        pass







