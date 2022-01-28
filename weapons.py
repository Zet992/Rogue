import math

import pygame
import entities

assault_rifle_shot_sound = pygame.mixer.Sound('data\\sounds\\player\\shot.wav')
shotgun_shot_sound = assault_rifle_shot_sound


class Weapon:
    pass


class WeaponAssaultRifle(Weapon):
    def __init__(self, weapon_level):
        self.weapon_level = weapon_level
        self.damage = 25 * self.weapon_level
        self.tick_need_for_shot = 15
        self.current_shooting_tick = self.tick_need_for_shot - 1

    def shot(self, location, scroll, coordinates, bullet_start_pos):
        mx, my = pygame.mouse.get_pos()
        start_pos = (coordinates[0] + bullet_start_pos[0], coordinates[1] + bullet_start_pos[1])
        rot = math.atan2(my + scroll[1] - start_pos[1], mx + scroll[0] - start_pos[0])
        move = math.cos(rot) * 10, math.sin(rot) * 10
        bullet = entities.AssaultRifleBullet(start_pos[0], start_pos[1], 1, 1, location, move=move)
        self.current_shooting_tick = 0
        self.play_shot_sound()
        return bullet

    def play_shot_sound(self):
        assault_rifle_shot_sound.play()


class WeaponShotgun(Weapon):
    def __init__(self, weapon_level):
        self.weapon_level = weapon_level
        self.damage = 25 * self.weapon_level
        self.tick_need_for_shot = 35
        self.current_shooting_tick = self.tick_need_for_shot - 1


    def shot(self, location, scroll, coordinates, bullet_start_pos):
        mx, my = pygame.mouse.get_pos()
        start_pos = (coordinates[0] + bullet_start_pos[0], coordinates[1] + bullet_start_pos[1])
        rot = math.atan2(my + scroll[1] - start_pos[1], mx + scroll[0] - start_pos[0])
        move = math.cos(rot) * 10, math.sin(rot) * 10
        self.current_shooting_tick = 0
        bullets = [
            entities.ShotgunBullet(start_pos[0], start_pos[1], 1, 1, location, move=(move[0], move[1] - 1), damage=self.damage),
            entities.ShotgunBullet(start_pos[0], start_pos[1], 1, 1, location, move=(move[0], move[1] - 3), damage=self.damage),
            entities.ShotgunBullet(start_pos[0], start_pos[1], 1, 1, location, move=(move[0], move[1] - 5), damage=self.damage),
            entities.ShotgunBullet(start_pos[0], start_pos[1], 1, 1, location, move=(move[0], move[1] + 1), damage=self.damage),
            entities.ShotgunBullet(start_pos[0], start_pos[1], 1, 1, location, move=(move[0], move[1] + 3), damage=self.damage),
            entities.ShotgunBullet(start_pos[0], start_pos[1], 1, 1, location, move=(move[0], move[1] + 5), damage=self.damage)]
        self.play_shot_sound()
        return bullets

    def play_shot_sound(self):
        shotgun_shot_sound.play()
