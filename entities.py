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
        self.jump_count = 15
        self.is_jump = False

    def update(self):
        self.animation_tick += 1
        if not self.collision['bottom'] and not self.is_jump:
            self.move[1] = 10
        if self.collision['right'] and self.move[0] > 0:
            self.move[0] = 0
        elif self.collision['left'] and self.move[0] < 0:
            self.move[0] = 0
        if self.collision['bottom'] and self.move[1] > 0:
            self.move[1] = 0
        elif self.collision['up'] and self.move[1] < 0:
            self.move[1] = 0
        self.x += self.move[0]
        self.y += self.move[1]

    def draw(self, surface):
        pass

    def check_collision_with_objects(self, objects):
        self.collision['right'] = False
        self.collision['left'] = False
        self.collision['up'] = False
        self.collision['bottom'] = False
        rect_x = pygame.Rect(self.x + self.move[0], self.y, self.width, self.height)
        for i in objects:
            rect_obj = pygame.Rect(i.x, i.y, i.width, i.height)
            x_col = rect_obj.colliderect(rect_x)
            if x_col and self.move[0] > 0:
                self.collision['right'] = True
                self.x = i.x - self.width
            elif x_col and self.move[0] < 0:
                self.collision['left'] = True
                self.x = i.x + i.width
        rect_y = pygame.Rect(self.x + self.move[0], self.y + self.move[1], self.width, self.height)
        for i in objects:
            rect_obj = pygame.Rect(i.x, i.y, i.width, i.height)
            y_col = rect_obj.colliderect(rect_y)
            if y_col and self.move[1] >= 0:
                self.collision['bottom'] = True
                self.y = i.y - self.height + 1
            if y_col and self.move[1] < 0:
                self.collision['up'] = True
                self.y = i.y + i.height

    def jump(self):
        if self.is_jump:
            if self.jump_count >= 0:
                self.move[1] = -(self.jump_count ** 2) / 2
                self.jump_count -= 1
            else:
                self.jump_count = 15
                self.is_jump = False


class Player(Entity):
    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 0),
                         (self.x, self.y, self.width, self.height))

    def shot(self):
        mx, my = pygame.mouse.get_pos()
        start_pos = (self.x + self.width // 2, self.y + self.height // 2)
        rot = math.atan2(my - start_pos[1], mx - start_pos[0])
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
            self.move = [5, 0]
        if self.x > player.x:
            self.move = [-5, 0]


class Enemy2(Enemy):
    pass


class Bullet(Entity):
    def draw(self, surface):
        pygame.draw.line(surface, (255, 255, 0), (self.x, self.y),
                         (self.x + self.width, self.y + self.height))

    def check_collisions_with_entity(self, entities):
        for i in entities:
            if (self.x + self.width > i.x > self.x) or (i.x < self.x < i.x + i.width):
                if self.y + self.height > i.y > self.y or i.y < self.y < i.y + i.height:
                    return i
        return None
