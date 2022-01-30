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
        self.menu_bar = NavigationBar(0, 0, width, 22)
        self.widgets.append(self.menu_bar)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in self.widgets:
                if i.rect.collidepoint(event.pos):
                    i.update(event)
        elif event.type == pygame.MOUSEMOTION:
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


class NavigationBar(BaseWidget):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.widgets = []

        self.open_btn = Button(1, 1, 100, height - 2, "Открыть файл")
        self.widgets.append(self.open_btn)

        self.save_btn = Button(102, 1, 100, height - 2, "Сохранить файл")
        self.widgets.append(self.save_btn)

        self.new_btn = Button(203, 1, 100, height - 2, "Новый файл")
        self.widgets.append(self.new_btn)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in self.widgets:
                if i.rect.collidepoint(event.pos):
                    i.update(event)
        elif event.type == pygame.MOUSEMOTION:
            for i in self.widgets:
                if i.rect.collidepoint(event.pos):
                    i.set_hovered(True)
                else:
                    i.set_hovered(False)

    def draw(self, surface):
        pygame.draw.rect(surface, (200, 200, 200), self.rect)
        for i in self.widgets:
            i.draw(surface)


class ScrollBar(BaseWidget):
    pass


class Button(BaseWidget):
    FONT = pygame.font.SysFont('arial', 12)

    def __init__(self, x, y, width, height, text):
        super().__init__(x, y, width, height)
        self.text = text
        self.hovered = False

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    def draw(self, surface):
        if self.hovered:
            pygame.draw.rect(surface, (150, 150, 150), self.rect)
        else:
            pygame.draw.rect(surface, (180, 180, 180), self.rect)
        text = self.FONT.render(self.text, True, (255, 255, 255))
        pos_x = self.x + (self.width - text.get_width()) // 2
        pos_y = self.y + (self.height - text.get_height()) // 2
        surface.blit(text, (pos_x, pos_y))

    def set_hovered(self, hovered):
        self.hovered = hovered

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
