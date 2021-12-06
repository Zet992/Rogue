import math

import pygame


class Entity:
    def __init__(self, x, y, width, height, move=(0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.move = list(move)
        self.animation_tick = 0
        self.animation_images = []

    def update(self):
        self.animation_tick += 1
        self.x += self.move[0]
        self.y += self.move[1]

    def draw(self, surface):
        pass


class Player(Entity):
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y,
                                                self.width,
                                                self.height))

    def shot(self):
        mx, my = pygame.mouse.get_pos()
        start_pos = (self.x + self.width // 2, self.y + self.height // 2)
        rot = math.degrees(math.atan2(my - start_pos[0], mx - start_pos[1]))
        rot = math.radians(rot)
        move = math.cos(rot) * 10, math.sin(rot) * 10
        bullet = Bullet(start_pos[0], start_pos[1], 1, 1, move=move)
        return bullet

class Enemy(Entity):
    pass


class Enemy1(Enemy):
    pass


class Enemy2(Enemy):
    pass



class Bullet(Entity):
    def draw(self, surface):
        pygame.draw.line(surface, (255, 255, 0), (self.x, self.y),
                         (self.x + self.width, self.y + self.height))
