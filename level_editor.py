import sys

import pygame

size = (1024, 576)
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Level editor")

from entities import EnemySoldier
from location import Wall, BackgroundTile


CELL_SIZE = (128, 128)
FONT = pygame.font.SysFont('arial', 10)


class BaseWidget:
    def __init__(self, x, y, width, height, parent=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.parent = parent
        self.widgets = []
        self.surface = pygame.Surface((width, height))
        self.hovered = False

    def resize(self, width, height):
        self.width = width
        self.height = height

    def move(self, x, y):
        self.x = x
        self.y = y

    def set_hovered(self, hovered):
        self.hovered = hovered
        for i in self.widgets:
            i.set_hovered(hovered)

    def update(self, event):
        pass

    def draw(self, surface):
        pass


class MainWindow(BaseWidget):
    def __init__(self, x, y, width, height, parent=None):
        super().__init__(x, y, width, height, parent)
        self.widgets = []

        self.cells_widget = CellsWidget(0, 23, 200, height - 23, self)
        self.widgets.append(self.cells_widget)
        self.menu_bar = NavigationBar(0, 0, width, 22, self)
        self.widgets.append(self.menu_bar)
        self.level_widget = LevelWidget(201, 23, width, height, self)
        self.widgets.append(self.level_widget)

        self.message = None

    def get_filename(self):
        self.message = PopUpMessage(400, 200, 200, 200, 
                                    'Введите название файла', self)
        self.widgets.append(self.message)

    def open_file(self, filename):
        self.widgets.remove(self.message)
        self.message = None
        if filename is None:
            return None
        self.level_widget.open_file(filename)

    def save_file(self):
        pass

    def new_file(self):
        pass

    def update(self, event):
        for i in self.widgets:
            i.update(event)

    def draw(self, surface):
        for i in self.widgets:
            i.draw(self.surface)
        if self.message:
            self.message.draw(self.surface)
        surface.blit(self.surface, self.rect)


class LevelWidget(BaseWidget):
    def __init__(self, x, y, width, height, parent):
        super().__init__(x, y, width, height, parent)
        self.game_objects = []
        self.walls = []
        self.background_tiles = []
        self.enemies = []
        self.size = None
        self.tp_zones = {}

        self.scroll = [0, 0]
        self.zoom = 1

    def open_file(self, file_name):
        level = []
        self.tp_zones = {}
        self.game_objects = []
        self.walls = []
        self.background_tiles = []
        self.enemies = []
        file = open(file_name, 'r')
        level = [i for i in file.read().split('\n')]
        if level[-1]:
            self.enemies = list(map(eval, level[-1].split('; ')))
        level = list(map(lambda x: x.split(), level[:-1]))
        for y, row in enumerate(level):
            for x, cell in enumerate(row):
                if cell == "@":
                    self.walls.append(Wall(x * CELL_SIZE[0], y * CELL_SIZE[1]))
                elif cell == '-':
                    back_tile = BackgroundTile(x * CELL_SIZE[0], y * CELL_SIZE[1])
                    self.background_tiles.append(back_tile)
                elif cell[:-1].isdigit():
                    if cell in self.tp_zones:
                        if y * CELL_SIZE[1] == self.tp_zones[cell][1]:
                            self.tp_zones[cell][2] += CELL_SIZE[0]
                        else:
                            self.tp_zones[cell][3] += CELL_SIZE[1]
                    else:
                        self.tp_zones[cell] = [x * CELL_SIZE[0], y * CELL_SIZE[1],
                                               CELL_SIZE[0], CELL_SIZE[1]]
                    back_tile = BackgroundTile(x * CELL_SIZE[0], y * CELL_SIZE[1])
                    self.background_tiles.append(back_tile)

        self.size = (x * CELL_SIZE[0], y * CELL_SIZE[1])
        self.game_objects.extend(enemies)
        self.game_objects.extend(walls)
        self.game_objects.extend(background_tiles)
        file.close()

    def update(self, event):
        if event.type == pygame.MOUSEWHEEL:
            self.zoom += event.y / 100
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
        elif event.type == pygame.MOUSEBUTTONUP:
            pass

    def draw(self, surface):
        for i in self.game_objects:
            i.draw(self.surface, self.scroll)
        surface.blit(self.surface, self.rect)


class CellsWidget(BaseWidget):
    def __init__(self, x, y, width, height, parent=None):
        super().__init__(x, y, width, height, parent)
        self.items = [EnemySoldier, Wall, BackgroundTile]

        self.scroll_bar = ScrollBar(width - 25, 5, 20, height - 10)
        self.scroll = 0

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.scroll_bar.rect.collidepoint(event.pos):
                event.pos = (event.pos[0] - self.scroll_bar.x, 
                             event.pos[1] - self.scroll_bar.y - self.y)
                self.scroll_bar.update(event)
        elif event.type == pygame.MOUSEMOTION:
            if self.scroll_bar.hovered:
                event.pos = (event.pos[0] - self.scroll_bar.x, 
                             event.pos[1] - self.scroll_bar.y - self.y)
                self.scroll_bar.update(event)
                self.scroll = scroll_bar.scroll
        elif event.type == pygame.MOUSEBUTTONUP:
            self.scroll_bar.set_hovered(False)

    def draw(self, surface):
        pygame.draw.rect(self.surface, (75, 255, 25), 
                         (0, 0, self.width, self.height), 
                         width=5)
        self.scroll_bar.draw(self.surface)
        for i in range(len(self.items)):
            pygame.draw.rect(self.surface, (150, 150, 50),
                             (10, i * 138 + 10 + self.scroll, 128, 128))
        surface.blit(self.surface, self.rect)

    def draw_items(self, surface):
        pass


class NavigationBar(BaseWidget):
    def __init__(self, x, y, width, height, parent=None):
        super().__init__(x, y, width, height, parent)

        self.open_btn = Button(1, 1, 100, height - 2,
                               "Открыть файл", self.open_file)
        self.widgets.append(self.open_btn)

        self.save_btn = Button(102, 1, 100, height - 2, 
                               "Сохранить файл", self.save_file)
        self.widgets.append(self.save_btn)

        self.new_btn = Button(203, 1, 100, height - 2, 
                              "Новый файл", self.new_file)
        self.widgets.append(self.new_btn)

    def open_file(self):
        self.parent.get_filename()

    def save_file(self):
        self.parent.save_file()

    def new_file(self):
        self.parent.get_filename()

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in self.widgets:
                if i.rect.collidepoint(event.pos):
                    i.update(event)
                    i.func()

        elif event.type == pygame.MOUSEMOTION:
            for i in self.widgets:
                if i.rect.collidepoint(event.pos):
                    i.set_hovered(True)
                else:
                    i.set_hovered(False)

    def draw(self, surface):
        pygame.draw.rect(self.surface, (200, 200, 200), self.rect)
        for i in self.widgets:
            i.draw(self.surface)
        surface.blit(self.surface, self.rect)


class PopUpMessage(BaseWidget):
    FONT = pygame.font.SysFont('arial', 14)

    def __init__(self, x, y, width, height, title, parent=None):
        super().__init__(x, y, width, height, parent)

        self.ok_btn = Button(5, y - 25, 20, 20, "OK", None)
        self.widgets.append(self.ok_btn)

        self.canc_btn = Button(width - 25, height - 25, 20, 20,
                               "CANCEL", None)
        self.widgets.append(self.canc_btn)

        self.text_line = LineEdit(10, 25, width - 20, 20)
        self.widgets.append(self.text_line)

        self.surface = pygame.Surface((self.width, self.height))
        self.title = title

    def close(self, result):
        self.parent.open_file(result)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            event.pos = (event.pos[0] - self.x, event.pos[1] - self.y)
            for i in self.widgets:
                if i.rect.collidepoint(event.pos):
                    i.update(event)
                    print('button pressed')
                    if i == self.ok_btn:
                        print("button ok")
                        self.close(self.text_line.text)
                    elif i == self.canc_btn:
                        print("button canc")
                        self.close(None)
        elif event.type == pygame.KEYDOWN:
            self.text_line.update(event)

    def draw(self, surface):
        pygame.draw.rect(self.surface, (50, 50, 50),
                         (0, 0, self.width, self.height))
        pygame.draw.rect(self.surface, (50, 125, 150), 
                         (0, 0, self.width, 20))
        text_surface = self.FONT.render(self.title, True, (0, 0, 0))
        self.surface.blit(text_surface, (5, 5))
        for i in self.widgets:
            i.draw(self.surface)
        surface.blit(self.surface, self.rect)


class ScrollBar(BaseWidget):
    def __init__(self, x, y, width, height, parent=None):
        super().__init__(x, y, width, height, parent)

        self.pols = pygame.Rect(0, 0, self.width, 20)
        self.first_pos_mouse = None
        self.scroll = 0

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.pols.collidepoint(event.pos):
                self.set_hovered(True)
                self.first_pos_mouse = event.pos
        elif event.type == pygame.MOUSEMOTION:
            if self.hovered:
                d_y = event.pos[1] - self.first_pos_mouse[1]
                self.pols = self.pols.move(0, d_y)
                self.pols.y = max(0, self.pols.y)
                self.pols.bottom = min(self.height, self.pols.bottom)
                self.first_pos_mouse = (self.first_pos_mouse[0],
                                        self.first_pos_mouse[1] + d_y)
                self.scroll += d_y

    def draw(self, surface):
        pygame.draw.rect(self.surface, (75, 75, 75),
                         (0, 0, self.width, self.height))
        pygame.draw.rect(self.surface, (125, 125, 125), self.pols)
        surface.blit(self.surface, self.rect)


class Button(BaseWidget):
    FONT = pygame.font.SysFont('arial', 12)

    def __init__(self, x, y, width, height, text, func, parent=None):
        super().__init__(x, y, width, height, parent)
        self.text = text
        self.hovered = False
        self.func = func

    def set_hovered(self, hovered):
        self.hovered = hovered

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    def draw(self, surface):
        if self.hovered:
            pygame.draw.rect(self.surface, (150, 150, 150), 
                             (0, 0, self.width, self.height))
        else:
            pygame.draw.rect(self.surface, (180, 180, 180), 
                             (0, 0, self.width, self.height))
        text = self.FONT.render(self.text, True, (255, 255, 255))
        pos_x = (self.width - text.get_width()) // 2
        pos_y = (self.height - text.get_height()) // 2
        self.surface.blit(text, (pos_x, pos_y))
        surface.blit(self.surface, self.rect)


class LineEdit(BaseWidget):
    FONT = pygame.font.SysFont('arial', 12)

    def __init__(self, x, y, width, height, parent=None):
        super().__init__(x, y, width, height, parent)

        self.text = ''

    def update(self, event):
        if event.type != pygame.KEYDOWN:
            return None
        self.text += event.unicode

    def draw(self, surface):
        pygame.draw.rect(self.surface, (255, 255, 255),
                         (0, 0, self.width, self.height))
        text_surface = self.FONT.render(self.text, True, (0, 0, 0))
        self.surface.blit(text_surface, (5, 5))
        surface.blit(self.surface, self.rect)


class GameObject:
    def __init__(self, x, y, width, height, image, name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.image = image
        self.name = name


main_window = MainWindow(0, 0, size[0], size[1])
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        main_window.update(event)
        main_window.draw(screen)
        pygame.display.update()

    clock.tick(60)
