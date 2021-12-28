import pygame


CELL_SIZE = (128, 128)
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = (1024, 576)


class Location:
    def __init__(self, name):
        self.map = []
        self.walls = []
        self.tp_zones = []
        self.size = (0, 0)
        self.step = (450, 300)
        self.max_scroll = (WINDOW_SIZE[0] - CELL_SIZE[0], WINDOW_SIZE[1] - CELL_SIZE[1])
        self.name = name
        self.load_map(name)
        self.scroll = [0, 0]

    def load_map(self, name):
        file = open("data/rooms/" + name, 'r')
        self.map = [i.split() for i in file.read().split('\n')]
        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                if cell == "@":
                    self.walls.append(Wall(x * CELL_SIZE[0], y * CELL_SIZE[1]))
                elif cell[:-1].isdigit():
                    self.tp_zones.append((pygame.Rect(x * CELL_SIZE[0], y * CELL_SIZE[1],
                                                     CELL_SIZE[0], CELL_SIZE[1]), cell))
        self.size = (x * CELL_SIZE[0], y * CELL_SIZE[1])

    def update_scroll(self, player):
        if player.x - self.scroll[0] != self.step[0]:
            self.scroll[0] = player.x - self.step[0]
        if player.y - self.scroll[1] != self.step[1]:
            self.scroll[1] = player.y - self.step[1]

        if self.scroll[0] < 0:
            self.scroll[0] = 0
        elif self.scroll[0] > self.size[0] - self.max_scroll[0]:
            self.scroll[0] = self.size[0] - self.max_scroll[0]
        if self.scroll[1] < 0:
            self.scroll[1] = 0
        elif self.scroll[1] > self.size[1] - self.max_scroll[1]:
            self.scroll[1] = self.size[1] - self.max_scroll[1]


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = CELL_SIZE[0]
        self.height = CELL_SIZE[1]

    def update(self):
        pass

    def draw(self, surface, scroll):
        pygame.draw.rect(surface, (100, 100, 100),
                         (self.x - scroll[0], self.y - scroll[1], CELL_SIZE[0], CELL_SIZE[1]))
