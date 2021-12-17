import math

import pygame

idle_player = [pygame.image.load('data\\images\\player\\idle\\idle_1.png'),
               pygame.image.load('data\\images\\player\\idle\\idle_2.png'),
               pygame.image.load('data\\images\\player\\idle\\idle_3.png'),
               pygame.image.load('data\\images\\player\\idle\\idle_4.png')]

run_player = [pygame.image.load('data\\images\\player\\run\\run_1.png'),
              pygame.image.load('data\\images\\player\\run\\run_2.png'),
              pygame.image.load('data\\images\\player\\run\\run_3.png'),
              pygame.image.load('data\\images\\player\\run\\run_4.png'),
              pygame.image.load('data\\images\\player\\run\\run_5.png'),
              pygame.image.load('data\\images\\player\\run\\run_6.png')]

jump_player = [pygame.image.load('data\\images\\player\\jump\\jump_1.png'),
               pygame.image.load('data\\images\\player\\jump\\jump_2.png'),
               pygame.image.load('data\\images\\player\\jump\\jump_3.png'),
               pygame.image.load('data\\images\\player\\jump\\jump_4.png')]

for i in range(len(idle_player)):
    idle_player[i] = pygame.transform.scale2x(idle_player[i])

for i in range(len(run_player)):
    run_player[i] = pygame.transform.scale2x(run_player[i])

for i in range(len(jump_player)):
    jump_player[i] = pygame.transform.scale2x(jump_player[i])


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
        self.fall_count = 1
        self.jump_tick = -1
        self.jumps = 0
        self.dash_count = 0
        self.side = RIGHT
        self.jump_count = 10
        self.is_jump = False
        self.right = True
        self.left = False
        self.idle = True
        self.run = False

    def update(self):
        if self.animation_tick >= 59:
            self.animation_tick = 0
        if not self.collision['bottom'] and not self.is_jump:
            self.move[1] = 10
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
    def __init__(self, x, y, width, height, move=(0, 0)):
        super(Player, self).__init__(x, y, width, height, move)
        self.shot_sound = pygame.mixer.Sound('data\\sounds\\player\\shot.wav')

    def draw(self, surface, scroll):
        # pygame.draw.rect(surface, (0, 255, 0), (self.x - scroll[0], self.y - scroll[1],
        #                              self.width, self.height))
        if self.idle and self.right:
            surface.blit(idle_player[self.animation_tick // 15], (self.x - scroll[0], self.y - scroll[1]))
        elif self.run and self.right:
            surface.blit(run_player[self.animation_tick // 10], (self.x - scroll[0], self.y - scroll[1] + 4))
        elif self.idle and self.left:
            image = idle_player[self.animation_tick // 15]
            image = pygame.transform.flip(image, True, False)
            surface.blit(image, (self.x - scroll[0], self.y - scroll[1]))
        elif self.run and self.left:
            image = run_player[self.animation_tick // 10]
            image = pygame.transform.flip(image, True, False)
            surface.blit(image, (self.x - scroll[0], self.y - scroll[1] + 4))
        elif self.is_jump and self.left:
            image = jump_player[self.animation_tick // 15]
            image = pygame.transform.flip(image, True, False)
            surface.blit(image, (self.x - scroll[0], self.y - scroll[1]))
        elif self.is_jump and self.right:
            surface.blit(jump_player[self.animation_tick // 15], (self.x - scroll[0], self.y - scroll[1]))


    def shot(self, scroll):
        mx, my = pygame.mouse.get_pos()
        start_pos = (self.x + self.width // 2, self.y + self.height // 2)
        rot = math.atan2(my + scroll[1] - start_pos[1], mx + scroll[0] - start_pos[0])
        move = math.cos(rot) * 10, math.sin(rot) * 10
        bullet = Bullet(start_pos[0], start_pos[1], 1, 1, move=move)
        self.play_shot_sound()
        return bullet

    def play_shot_sound(self):
        self.shot_sound.play()


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

    def draw(self, surface, scroll):
        pygame.draw.line(surface, (255, 255, 0), (self.x - scroll[0], self.y - scroll[1]),
                         (self.x - scroll[0] + self.width, self.y - scroll[1] + self.height))

    def check_collisions_with_entity(self, entities):
        for i in entities:
            if (self.x + self.width > i.x > self.x) or (i.x < self.x < i.x + i.width):
                if self.y + self.height > i.y > self.y or i.y < self.y < i.y + i.height:
                    return i
        return None
