import pygame


class Decoration:
    def __init__(self, surface, x, y):
        self.surface = surface
        self.x = x
        self.y = y


class TreeSpruce(Decoration):
    def draw(self):
        tree_sprite = pygame.image.load('data\\images\\decorations\\spruce\\spruce.png')
        self.surface.blit(tree_sprite, (self.x, self.y - 217))


