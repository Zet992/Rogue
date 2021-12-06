import pygame


CELL_SIZE = (64, 64)


class Location:
    def __init__(self, name):
        self.map = []
        self.walls = []
        self.load_map(name)

    def load_map(self, name):
        file = open("data/rooms/" + name, 'r')
        self.map = [i.split() for i in file.read().split('\n')]
        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                if cell == "@":
                    self.walls.append(Wall(x * 64, y * 64))


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = CELL_SIZE[0]
        self.height = CELL_SIZE[1]

    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, (100, 100, 100),
                         (self.x, self.y, CELL_SIZE[0], CELL_SIZE[1]))
