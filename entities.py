import math
import random

import pygame

from settings import WINDOW_HEIGHT

run_player_45 = [pygame.image.load('data\\images\\player\\run\\45\\run_1.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\45\\run_2.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\45\\run_3.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\45\\run_4.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\45\\run_5.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\45\\run_6.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\45\\run_7.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\45\\run_8.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\idle\\45\\idle.png').convert_alpha()]

run_player_70 = [pygame.image.load('data\\images\\player\\run\\70\\run_1.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\70\\run_2.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\70\\run_3.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\70\\run_4.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\70\\run_5.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\70\\run_6.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\70\\run_7.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\70\\run_8.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\idle\\70\\idle.png').convert_alpha()]

run_player_90 = [pygame.image.load('data\\images\\player\\run\\90\\run_1.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\90\\run_2.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\90\\run_3.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\90\\run_4.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\90\\run_5.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\90\\run_6.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\90\\run_7.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\run\\90\\run_8.png').convert_alpha(),
                 pygame.image.load('data\\images\\player\\idle\\90\\idle.png').convert_alpha()]

run_player_120 = [pygame.image.load('data\\images\\player\\run\\120\\run_1.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\run\\120\\run_2.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\run\\120\\run_3.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\run\\120\\run_4.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\run\\120\\run_5.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\run\\120\\run_6.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\run\\120\\run_7.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\run\\120\\run_8.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\idle\\120\\idle.png').convert_alpha()]

run_player_150 = [pygame.image.load('data\\images\\player\\run\\150\\run_1.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\run\\150\\run_2.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\run\\150\\run_3.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\run\\150\\run_4.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\run\\150\\run_5.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\run\\150\\run_6.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\run\\150\\run_7.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\run\\150\\run_8.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\idle\\150\\idle.png').convert_alpha()]

jump_player_45 = [pygame.image.load('data\\images\\player\\jump\\45\\jump.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\jump\\45\\jump.png').convert_alpha()]

jump_player_70 = [pygame.image.load('data\\images\\player\\jump\\70\\jump.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\jump\\70\\jump.png').convert_alpha()]

jump_player_90 = [pygame.image.load('data\\images\\player\\jump\\90\\jump.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\jump\\90\\jump.png').convert_alpha()]

jump_player_120 = [pygame.image.load('data\\images\\player\\jump\\120\\jump.png').convert_alpha(),
                   pygame.image.load('data\\images\\player\\jump\\120\\jump.png').convert_alpha()]

jump_player_150 = [pygame.image.load('data\\images\\player\\jump\\150\\jump.png').convert_alpha(),
                   pygame.image.load('data\\images\\player\\jump\\150\\jump.png').convert_alpha()]

idle_player_45 = [pygame.image.load('data\\images\\player\\idle\\45\\idle.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\idle\\45\\idle.png').convert_alpha()]

idle_player_70 = [pygame.image.load('data\\images\\player\\idle\\70\\idle.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\idle\\70\\idle.png').convert_alpha()]

idle_player_90 = [pygame.image.load('data\\images\\player\\idle\\90\\idle.png').convert_alpha(),
                  pygame.image.load('data\\images\\player\\idle\\90\\idle.png').convert_alpha()]

idle_player_120 = [pygame.image.load('data\\images\\player\\idle\\120\\idle.png').convert_alpha(),
                   pygame.image.load('data\\images\\player\\idle\\120\\idle.png').convert_alpha()]

idle_player_150 = [pygame.image.load('data\\images\\player\\idle\\150\\idle.png').convert_alpha(),
                   pygame.image.load('data\\images\\player\\idle\\150\\idle.png').convert_alpha()]

idle_player_180 = [pygame.image.load('data\\images\\player\\idle\\180\\idle.png').convert_alpha(),
                   pygame.image.load('data\\images\\player\\idle\\180\\idle.png').convert_alpha()]

idle_enemy_soldier = [pygame.image.load('data\\images\\enemies\\soldier\\idle\\idle.png').convert_alpha(),
                      pygame.image.load('data\\images\\enemies\\soldier\\idle\\idle.png').convert_alpha()]

run_enemy_soldier = [pygame.image.load('data\\images\\enemies\\soldier\\run\\run_1.png').convert_alpha(),
                     pygame.image.load('data\\images\\enemies\\soldier\\run\\run_2.png').convert_alpha(),
                     pygame.image.load('data\\images\\enemies\\soldier\\run\\run_3.png').convert_alpha(),
                     pygame.image.load('data\\images\\enemies\\soldier\\run\\run_4.png').convert_alpha(),
                     pygame.image.load('data\\images\\enemies\\soldier\\run\\run_5.png').convert_alpha(),
                     pygame.image.load('data\\images\\enemies\\soldier\\run\\run_6.png').convert_alpha(),
                     pygame.image.load('data\\images\\enemies\\soldier\\run\\run_7.png').convert_alpha(),
                     pygame.image.load('data\\images\\enemies\\soldier\\run\\run_8.png').convert_alpha(),
                     pygame.image.load('data\\images\\enemies\\soldier\\idle\\idle.png').convert_alpha()]

boss = pygame.image.load('data\\images\\enemies\\boss\\boss.png').convert_alpha()

for i in range(len(idle_player_45)):
    idle_player_45[i] = pygame.transform.scale2x(idle_player_45[i])

for i in range(len(idle_player_70)):
    idle_player_70[i] = pygame.transform.scale2x(idle_player_70[i])

for i in range(len(idle_player_90)):
    idle_player_90[i] = pygame.transform.scale2x(idle_player_90[i])

for i in range(len(idle_player_120)):
    idle_player_120[i] = pygame.transform.scale2x(idle_player_120[i])

for i in range(len(idle_player_150)):
    idle_player_150[i] = pygame.transform.scale2x(idle_player_150[i])

for i in range(len(idle_player_180)):
    idle_player_180[i] = pygame.transform.scale2x(idle_player_180[i])

for i in range(len(run_player_45)):
    run_player_45[i] = pygame.transform.scale2x(run_player_45[i])

for i in range(len(run_player_70)):
    run_player_70[i] = pygame.transform.scale2x(run_player_70[i])

for i in range(len(run_player_90)):
    run_player_90[i] = pygame.transform.scale2x(run_player_90[i])

for i in range(len(run_player_120)):
    run_player_120[i] = pygame.transform.scale2x(run_player_120[i])

for i in range(len(run_player_150)):
    run_player_150[i] = pygame.transform.scale2x(run_player_150[i])

for i in range(len(jump_player_45)):
    jump_player_45[i] = pygame.transform.scale2x(jump_player_45[i])

for i in range(len(jump_player_70)):
    jump_player_70[i] = pygame.transform.scale2x(jump_player_70[i])

for i in range(len(jump_player_90)):
    jump_player_90[i] = pygame.transform.scale2x(jump_player_90[i])

for i in range(len(jump_player_120)):
    jump_player_120[i] = pygame.transform.scale2x(jump_player_120[i])

for i in range(len(jump_player_150)):
    jump_player_150[i] = pygame.transform.scale2x(jump_player_150[i])

for i in range(len(idle_enemy_soldier)):
    idle_enemy_soldier[i] = pygame.transform.scale2x(idle_enemy_soldier[i])

for i in range(len(run_enemy_soldier)):
    run_enemy_soldier[i] = pygame.transform.scale2x(run_enemy_soldier[i])


class Entity:
    def __init__(self, x, y, width, height, location, move=(0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.move = list(move)
        self.animation_tick = 0
        self.animation_images = []
        self.collision = {"up": False, "bottom": False, "right": False, "left": False}
        self.fall_count = 1
        self.jump_tick = -1
        self.jumps = 0
        self.dash_count = 0
        self.right = True
        self.left = False
        self.idle = True
        self.run = False
        self.ang = 90
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.hp = 100
        self.money = 0
        self.location = location
        self.living_tick = 0

    def update(self):
        if self.animation_tick > 61:
            self.animation_tick = 0

        if self.collision['right'] and self.move[0] > 0:
            self.move[0] = 0
            self.dash_count = 0
        elif self.collision['left'] and self.move[0] < 0:
            self.move[0] = 0
            self.dash_count = 0

        if self.dash_count and self.move[1] > 0:
            self.y -= 3
        elif self.collision['bottom'] and self.move[1] > 0:
            self.fall_count = 0
            self.jumps = 0
            self.move[1] = 3
            self.y -= 3
        elif self.collision['up'] and self.move[1] < 0:
            self.move[1] = 0
            self.jump_tick = -1

        self.x += self.move[0]
        self.y += self.move[1]
        self.animation_tick += 1
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface, scroll):
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
                self.x = i.x - self.width - 2
            elif x_col and self.move[0] < 0:
                self.collision['left'] = True
                self.x = i.x + i.width + 2
        rect_y = pygame.Rect(self.x, self.y + self.move[1], self.width, self.height)
        for i in objects:
            rect_obj = pygame.Rect(i.x, i.y, i.width, i.height)
            y_col = rect_obj.colliderect(rect_y)
            if y_col and self.move[1] >= 0:
                self.collision['bottom'] = True
                self.y = i.y - self.height - 2
            if y_col and self.move[1] < 0:
                self.collision['up'] = True
                self.y = i.y + i.height + 2

    def dash(self):
        self.dash_count = 5
        self.move[1] = 3
        self.jump_tick = -1
        self.fall_count = 0

    def jump(self):
        if self.jumps == 1 or self.jumps == 2:
            if self.jump_tick >= 0:
                self.move[1] = -(self.jump_tick ** 2) / 10
                self.jump_tick -= 1


class Player(Entity):
    def __init__(self, x, y, width, height, location, move=(0, 0), hp=100):
        super(Player, self).__init__(x, y, width, height, location, move)
        self.shot_sound = pygame.mixer.Sound('data\\sounds\\player\\shot.wav')
        self.hp = hp
        self.location = location
        self.shooting_tick = 3
        self.shooting = False

    def draw(self, surface, scroll):
        image = image = idle_player_90[self.animation_tick // 60]  # default_image

        mx, my = pygame.mouse.get_pos()
        start_pos = (self.x + self.width // 2, self.y + self.height // 2)
        ang = math.atan2(mx + scroll[0] - start_pos[0], my + scroll[1] - start_pos[1])
        self.ang = abs(math.degrees(ang))

        if self.ang < 57:
            offset = 0.0052
            if self.idle:
                image = idle_player_45[self.animation_tick // 60]
            elif self.run:
                offset = 0.015
                image = run_player_45[self.animation_tick // 8]
            elif self.jumps:
                image = jump_player_45[self.animation_tick // 60]
        elif 57 <= self.ang < 80:
            offset = 0.0087
            if self.idle:
                image = idle_player_70[self.animation_tick // 60]
            elif self.run:
                image = run_player_70[self.animation_tick // 8]
            elif self.jumps:
                image = jump_player_70[self.animation_tick // 60]
        elif 80 <= self.ang < 105:
            offset = 0.0087
            if self.idle:
                image = idle_player_90[self.animation_tick // 60]
            elif self.run:
                image = run_player_90[self.animation_tick // 8]
            elif self.jumps:
                image = jump_player_90[self.animation_tick // 60]
        elif 105 <= self.ang < 135:
            offset = 0.0087
            if self.idle:
                image = idle_player_120[self.animation_tick // 60]
            elif self.run:
                offset = 0.0174
                image = run_player_120[self.animation_tick // 8]
            elif self.jumps:
                image = jump_player_120[self.animation_tick // 60]
        elif 135 <= self.ang < 165:
            offset = 0.032
            if self.idle:
                image = idle_player_150[self.animation_tick // 60]
            elif self.run:
                image = run_player_150[self.animation_tick // 8]
            elif self.jumps:
                image = jump_player_150[self.animation_tick // 60]
        elif 165 <= self.ang:
            offset = 0.0434
            if self.idle:
                image = idle_player_180[self.animation_tick // 60]
            elif self.run:
                offset = 0.026
                image = run_player_150[self.animation_tick // 8]
            elif self.jumps:
                image = jump_player_150[self.animation_tick // 60]

        if self.left:
            image = pygame.transform.flip(image, True, False)

        surface.blit(image, (self.x - scroll[0], self.y - scroll[1] - int(offset * WINDOW_HEIGHT)))

    def shot(self, scroll):
        mx, my = pygame.mouse.get_pos()
        start_pos = (self.x + self.width // 2, self.y + self.height // 2)
        rot = math.atan2(my + scroll[1] - start_pos[1], mx + scroll[0] - start_pos[0])
        move = math.cos(rot) * 10, math.sin(rot) * 10
        bullet = Bullet(start_pos[0], start_pos[1], 1, 1, self.location, move=move)
        self.play_shot_sound()
        return bullet

    def play_shot_sound(self):
        self.shot_sound.play()

    def get_damage(self, damage):
        self.hp -= damage


class Enemy(Entity):
    pass


class Enemy1(Enemy):
    def draw(self, surface, scroll):
        pygame.draw.rect(surface, (255, 0, 0),
                         (self.x - scroll[0], self.y - scroll[1], self.width, self.height))

    def find_player(self, player):
        if self.x < player.x:
            self.move[0] = 5
        else:
            self.move[0] = -5


class Enemy2(Enemy):
    def update(self):
        self.animation_tick += 1
        self.x += self.move[0]
        self.y += self.move[1]

    def draw(self, surface, scroll):
        pygame.draw.rect(surface, (155, 0, 0),
                         (self.x - scroll[0], self.y - scroll[1], self.width, self.height))

    def find_player(self, player):
        if self.x < player.x:
            self.move[0] = 5
        else:
            self.move[0] = -5
        if self.y < player.y:
            self.move[1] = 5
        else:
            self.move[1] = -5


class Bullet(Entity):
    def update(self):
        self.x += self.move[0]
        self.y += self.move[1]
        self.living_tick += 1

    def draw(self, surface, scroll):
        pygame.draw.circle(surface, (0, 132, 255), (self.x - scroll[0], self.y - scroll[1]), 5)

    def check_collisions_with_entity(self, entities):
        for i in entities:
            if i.location == self.location:
                if (self.x + self.width > i.x > self.x) or (i.x < self.x < i.x + i.width):
                    if self.y + self.height > i.y > self.y or i.y < self.y < i.y + i.height:
                        return i
        return None

    def check_collision_with_walls(self, walls):
        for i in walls:
            if (self.x + self.width > i.x > self.x) or (i.x < self.x < i.x + i.width):
                if self.y + self.height > i.y > self.y or i.y < self.y < i.y + i.height:
                    return i
        return None

    def update(self):
        super(Bullet, self).update()
        self.living_tick += 1


class EnemySoldier(Enemy):
    def __init__(self, x, y, width, height, location, hp, move=(0, 0)):
        super(EnemySoldier, self).__init__(x, y, width, height, location, move=move)
        self.patrolling = True
        self.patrolling_tick = 0
        self.patrolling_direction = 1
        self.idling_tick = 0
        self.vision_rect = pygame.Rect(0, 0, 1400, 80)
        self.vision_rect.center = (self.x, self.y)
        self.engaging = False
        self.engaging_tick = 1
        self.shot_sound = pygame.mixer.Sound('data\\sounds\\player\\shot.wav')
        self.hp = hp

    def __str__(self):
        return 'EnemySoldier'

    def update(self):
        if not self.collision['bottom'] and self.jump_tick == -1:
            self.move[1] = self.fall_count ** 2 / 10
            if self.fall_count < 15:
                self.fall_count += 1
        super().update()
        self.vision_rect.center = self.x, self.y

    def draw(self, surface, scroll):
        image = idle_enemy_soldier[0]  # default_image

        if self.idle:
            image = idle_enemy_soldier[self.animation_tick // 60]
        elif self.run:
            image = run_enemy_soldier[self.animation_tick // 8]

        if self.left:
            image = pygame.transform.flip(image, True, False)

        surface.blit(image, (self.x - scroll[0], self.y - scroll[1]))

    def find_player(self, player):
        if self.x < player.x:
            self.move[0] = 5
        else:
            self.move[0] = -5
        if self.y < player.y:
            self.move[1] = 5
        else:
            self.move[1] = -5

    def play_shot_sound(self):
        self.shot_sound.play()

    def ai(self, player):
        if self.idle:
            self.move[0] = 0
            self.idling_tick += 1
            if self.idling_tick == 160:
                self.idle = False
                self.patrolling = True
                self.idling_tick = 0

        if self.vision_rect.colliderect(player.rect):
            self.engaging = True

        if self.engaging:
            if player.x > self.x:
                self.right = True
                self.left = False
            else:
                self.right = False
                self.left = True
            self.idle = True
            self.patrolling = False
            self.engaging_tick += 1
            if self.engaging_tick == 100:
                self.engaging_tick = 1
                self.engaging = False
                self.patrolling = True
                self.idle = False

    def shot(self):
        if self.left:
            bullets = [EnemyBullet(self.x, self.y + self.height // 2, 1, 1, self.location, move=(-6, 0)),
                       EnemyBullet(self.x, self.y + self.height // 2, 1, 1, self.location, move=(-6, -3)),
                       EnemyBullet(self.x, self.y + self.height // 2, 1, 1, self.location, move=(-6, 3))]
        elif self.right:
            bullets = [EnemyBullet(self.x + self.width, self.y + self.height // 2, 1, 1, self.location, move=(6, 0)),
                       EnemyBullet(self.x + self.width, self.y + self.height // 2, 1, 1, self.location, move=(6, -3)),
                       EnemyBullet(self.x + self.width, self.y + self.height // 2, 1, 1, self.location, move=(6, 3))]
        self.play_shot_sound()
        return bullets


class EnemyBullet(Bullet):
    def draw(self, surface, scroll):
        pygame.draw.circle(surface, 'red', (self.x - scroll[0], self.y - scroll[1] + self.height // 2), radius=7)

    def check_collisions_with_player(self, player):
        if player.location == self.location:
            if (self.x + self.width > player.x > self.x) or (player.x < self.x < player.x + player.width):
                if self.y + self.height > player.y > self.y or player.y < self.y < player.y + player.height:
                    player.get_damage(random.randrange(15, 25))
                    return True
        return False


class Particle:
    def __init__(self, x, y, width, height, move=(0, 0), ticks=600, physics=True,
                 color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.move = list(move)
        self.ticks = ticks
        self.physics = physics
        self.color = color

    def update(self):
        self.ticks -= 1
        if self.physics:
            if self.move[0] > 0:
                self.move[0] -= 1
            elif self.move[0] < 0:
                self.move[0] += 1
            self.move[1] += 1
        self.x += self.move[0]
        self.y += self.move[1]

    def draw(self, screen, scroll):
        rect = pygame.Rect(self.x - scroll[0], self.y - scroll[1],
                           self.width, self.height)
        pygame.draw.ellipse(screen, self.color, rect)


class Boss(Entity):
    def __init__(self, x, y, width, height, location, hp=1000, move=(0, 0)):
        super(Boss, self).__init__(x, y, width, height, location, move)
        self.hp = hp
        self.vision_rect = pygame.Rect(0, 0, 700, 80)
        self.vision_rect.center = (self.x, self.y)
        self.engaging_tick = 0
        self.r = 300
        self.die = False

    def draw(self, surface, scroll):
        rect = boss.get_rect(center=(self.x - scroll[0], self.y - scroll[1]))
        surface.blit(boss, rect)

    def __str__(self):
        return 'Boss'

    def ai(self, player):
        if player.x > self.x:
            self.x += 5
        if player.x < self.x:
            self.x -= 5
        self.engaging_tick += 1

    def shot(self):
        bullets = [EnemyBullet(self.x, self.y, 1, 1, self.location, move=(random.randint(-3, 3), random.randint(-3, 3)))
                   for _ in range(7)]
        return bullets
