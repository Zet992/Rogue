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


class BackGround:
    def __init__(self, surface, width, height):
        self.surface = surface
        self.width = width
        self.height = height


class BackGroundSky(BackGround):
    def draw(self):
        pygame.draw.rect(self.surface, (0, 191, 255),
                         (0, 0, self.width, self.height))


class BackGroundGrass(BackGround):
    def draw(self):
        pygame.draw.rect(self.surface, (63, 155, 11),
                         (0, self.height // 2, self.width, self.height))
