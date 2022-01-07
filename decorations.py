import random

import pygame

health = pygame.image.load('data\\images\\bonuses\\health\\health.png').convert_alpha()
health = pygame.transform.scale2x(health)

money = [pygame.image.load('data\\images\\bonuses\\money\\money_1.png').convert_alpha(),
         pygame.image.load('data\\images\\bonuses\\money\\money_2.png').convert_alpha(),
         pygame.image.load('data\\images\\bonuses\\money\\money_3.png').convert_alpha(),
         pygame.image.load('data\\images\\bonuses\\money\\money_4.png').convert_alpha(),
         pygame.image.load('data\\images\\bonuses\\money\\money_5.png').convert_alpha(),
         pygame.image.load('data\\images\\bonuses\\money\\money_1.png').convert_alpha()]

for i in range(len(money)):
    money[i] = pygame.transform.scale2x(money[i])


class Decoration:
    def __init__(self, surface, x, y):
        self.surface = surface
        self.x = x
        self.y = y


class TreeSpruce(Decoration):
    def draw(self):
        tree_sprite = pygame.image.load('data\\images\\decorations\\spruce\\spruce.png')
        self.surface.blit(tree_sprite, (self.x, self.y - 217))


class Bonus:
    def __init__(self, x, y, location):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 64, 32)
        self.animation_tick = 0
        self.location = location

    def update(self):
        self.animation_tick += 1
        if self.animation_tick == 60:
            self.animation_tick = 0


class HealthBonus(Bonus):
    def draw(self, surface, scroll):
        surface.blit(health, (self.x - scroll[0], self.y - scroll[1]))

    def __str__(self):
        return 'HealthBonus'

    def check_collision_with_player(self, player):
        if self.rect.colliderect(player.rect):
            if player.hp < 100:
                player.hp = min(player.hp + random.randrange(25, 50), 100)
                return True
        return False


class MoneyBonus(Bonus):
    def draw(self, surface, scroll):
        image = money[self.animation_tick // 10]
        surface.blit(image, (self.x - scroll[0], self.y - scroll[1]))

    def __str__(self):
        return 'MoneyBonus'

    def check_collision_with_player(self, player):
        if self.rect.colliderect(player.rect):
            player.money += random.randrange(40, 70, 1)
            return True
        return False
