import math

import pygame

from entities import ShotgunBullet, AssaultRifleBullet

assault_rifle_shot_sound = pygame.mixer.Sound('data\\sounds\\player\\shot.wav')
shotgun_shot_sound = assault_rifle_shot_sound


class Weapon:
    pass


class WeaponAssaultRifle(Weapon):
    def __init__(self, weapon_level):
        self.weapon_level = weapon_level
        self.damage = 25 * self.weapon_level

    def shot(self, location, scroll, coordinates, bullet_start_pos):
        mx, my = pygame.mouse.get_pos()
        start_pos = (coordinates[0] + bullet_start_pos[0], coordinates[1] + bullet_start_pos[1])
        rot = math.atan2(my + scroll[1] - start_pos[1], mx + scroll[0] - start_pos[0])
        move = math.cos(rot) * 10, math.sin(rot) * 10
        bullet = AssaultRifleBullet(start_pos[0], start_pos[1], 1, 1, location, move=move)
        self.play_shot_sound()
        return bullet

    def play_shot_sound(self):
        assault_rifle_shot_sound.play()


class WeaponShotgun(Weapon):
    def __init__(self, weapon_level):
        self.weapon_level = weapon_level
        self.damage = 9 * self.weapon_level

    def shot(self, location, scroll, coordinates, bullet_start_pos):
        mx, my = pygame.mouse.get_pos()
        start_pos = (coordinates[0] + bullet_start_pos[0], coordinates[1] + bullet_start_pos[1])
        rot = math.atan2(my + scroll[1] - start_pos[1], mx + scroll[0] - start_pos[0])
        move = math.cos(rot) * 10, math.sin(rot) * 10
        bullets = [
            ShotgunBullet(start_pos[0], start_pos[1], 1, 1, location, move=(move[0], move[1] - 1), damage=self.damage),
            ShotgunBullet(start_pos[0], start_pos[1], 1, 1, location, move=(move[0], move[1] - 3), damage=self.damage),
            ShotgunBullet(start_pos[0], start_pos[1], 1, 1, location, move=(move[0], move[1] - 5), damage=self.damage),
            ShotgunBullet(start_pos[0], start_pos[1], 1, 1, location, move=(move[0], move[1] + 1), damage=self.damage),
            ShotgunBullet(start_pos[0], start_pos[1], 1, 1, location, move=(move[0], move[1] + 3), damage=self.damage),
            ShotgunBullet(start_pos[0], start_pos[1], 1, 1, location, move=(move[0], move[1] + 5), damage=self.damage)]
        self.play_shot_sound()
        return bullets

    def play_shot_sound(self):
        shotgun_shot_sound.play()
