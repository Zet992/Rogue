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
        self.collision = {"up": False, "bottom": False, "right": False, "left": False}
        self.jump_count = 10
        self.is_jump = False
        self.right = False
        self.left = False

    def update(self):
        self.animation_tick += 1
        self.x += self.move[0]
        self.y += self.move[1]

    def draw(self, surface):
        pass

    def jump(self):
        if self.is_jump:
            if self.jump_count >= - 10:
                if self.jump_count < 0:
                    self.y += (self.jump_count ** 2) / 2
                else:
                    self.y -= (self.jump_count ** 2) / 2
                self.jump_count -= 1
            else:
                self.jump_count = 10
                self.is_jump = False


class Player(Entity):
    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), (self.x, self.y, self.width, self.height))


    def shot(self):
        mx, my = pygame.mouse.get_pos()
        start_pos = (self.x + self.width // 2, self.y + self.height // 2)
        print(start_pos, mx, my)
        rot = math.degrees(math.atan2(my - start_pos[1], mx - start_pos[0]))
        rot = math.radians(rot)
        move = math.cos(rot) * 10, math.sin(rot) * 10
        bullet = Bullet(start_pos[0], start_pos[1], 1, 1, move=move)
        return bullet


class Enemy(Entity):
    pass


class Enemy1(Enemy):
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0),
                         (self.x, self.y, self.width, self.height))

    def find_player(self, player):
        if self.x < player.x:
            self.move = (5, 0)
        if self.x > player.x:
            self.move = (-5, 0)


class Enemy2(Enemy):
    pass


class Bullet(Entity):
    def draw(self, surface):
        pygame.draw.line(surface, (255, 255, 0), (self.x, self.y),
                         (self.x + self.width, self.y + self.height))

    def check_collisions_with_entity(self, entities):
        for i in entities:
            if ((self.x + self.width > i.x > self.x) or (i.x < self.x < i.x + i.width)):
                if (self.y + self.height > i.y > self.y or i.y < self.y < i.y + i.height):
                    return i
        return None

