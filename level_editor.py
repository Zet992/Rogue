import sys

import pygame


size = (1024, 568)
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Level editor")


class BaseWidget:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

    def resize(self, width, height):
        self.width = width
        self.height = height

    def move(self, x, y):
        self.x = x
        self.y = y

    def update(self, event):
        pass

    def draw(self, surface):
        pass


class MainWindow(BaseWidget):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.widgets = []

        self.level_widget = LevelWidget(0, 0, width, height)
        self.widgets.append(self.level_widget)
        self.cells_widget = CellsWidget(0, 0, 200, height)
        self.widgets.append(self.cells_widget)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in self.widgets:
                if i.rect.collidepoint(event.pos):
                    i.update(event)

    def draw(self, surface):
        for i in self.widgets:
            i.draw(surface)


class LevelWidget(BaseWidget):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.game_objects = []

    def draw(self, surface):
        for i in self.game_objects:
            i.draw(surface)


class CellsWidget(BaseWidget):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.items = []

    def draw(self, surface):
        pygame.draw.rect(surface, (75, 255, 25), self.rect, width=5)
        for i in self.items:
            self.draw_items(self, surface)

    def draw_items(self, surface):
        pass


class ScrollBar(BaseWidget):
    pass


class Button(BaseWidget):
    pass


class LineEdit(BaseWidget):
    pass


class GameObject:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)


main_window = MainWindow(0, 0, size[0], size[1])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        main_window.update(event)
        main_window.draw(screen)
        pygame.display.update()
