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
        self.jump_count = 10
        self.is_jump = False

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
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y,
                                                self.width,
                                                self.height))


class Enemy(Entity):
    pass


class Enemy1(Enemy):
    pass


class Enemy2(Enemy):
    pass
