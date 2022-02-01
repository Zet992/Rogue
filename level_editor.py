import sys

import pygame


size = (1024, 576)
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
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.widgets = []

        self.cells_widget = CellsWidget(0, 23, 200, height - 23)
        self.widgets.append(self.cells_widget)
        self.menu_bar = NavigationBar(0, 0, width, 22)
        self.widgets.append(self.menu_bar)
        self.level_widget = LevelWidget(0, 0, width, height)
        self.widgets.append(self.level_widget)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            collided = False
            for i in self.widgets:
                if i.rect.collidepoint(event.pos) and not collided:
                    i.update(event)
                    collided = True
        elif event.type == pygame.MOUSEMOTION:
            collided = False
            for i in self.widgets:
                if i.rect.collidepoint(event.pos) and not collided:
                    i.update(event)
                    collided = True
                else:
                    i.set_hovered(False)

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

        self.scroll_bar = ScrollBar(x + width - 25, y + 5, 20, height - 10)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.scroll_bar.rect.collidepoint(event.pos):
                event.pos = (event.pos[0] - self.scroll_bar.x, 
                             event.pos[1] - self.scroll_bar.y - self.y)
                self.scroll_bar.update(event)
        elif event.type == pygame.MOUSEMOTION:
            if self.scroll_bar.rect.collidepoint(event.pos):
                event.pos = (event.pos[0] - self.scroll_bar.x, 
                             event.pos[1] - self.scroll_bar.y - self.y)
                self.scroll_bar.update(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.scroll_bar.rect.collidepoint(event.pos):
                self.scroll_bar.set_hovered(False)

    def draw(self, surface):
        pygame.draw.rect(self.surface, (75, 255, 25), 
                         (0, 0, self.width, self.height), 
                         width=5)
        self.scroll_bar.draw(self.surface)
        for i in self.items:
            self.draw_items(self, self.surface)
        surface.blit(self.surface, self.rect)

    def draw_items(self, surface):
        pass


class NavigationBar(BaseWidget):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

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
        level_name = ''
        file_name = 'data/rooms/' + level_name

    def save_file(self):
        pass

    def new_file(self):
        pass

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


class PopUpMessage(BaseWidget):
    FONT = pygame.font.SysFont('arial', 10)

    def __init__(self, x, y, width, height, title):
        super().__init__(x, y, width, height)

        self.ok_btn = Button(5, y - 25, 20, 20)
        self.widgets.append(self.ok_btn)

        self.canc_btn = Button(x - 25, y - 25, 20, 20)
        self.widgets.append(self.canc_btn)

        self.text_line = LineEdit(25, 25, 80, 20)
        self.widgets.append(self.text_line)

        self.surface = pygame.Surface((self.width, self.height))
        self.title = title

    def close(self, result):
        pass

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in self.widgets:
                if i.collidepoint(event.pos):
                    i.update(event)
                    if i == self.ok_btn:
                        self.close(self.text_line.text)
                    elif i == self.canc_btn:
                        self.close(None)

    def draw(self, surface):
        pygame.draw.rect(self.surface, (255, 255, 255), 
                         (self.x, self.y, self.width, 20))
        text_surface = FONT.render(self.title, True, (0, 0, 0))
        self.surface.blit(text_surface, (5, 5))
        for i in self.widgets:
            i.draw(self.surface)
        surface.blit(self.surface, self.rect)


class ScrollBar(BaseWidget):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.pols = pygame.Rect(0, 0, self.width, 20)
        self.first_pos_mouse = None

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            print(self.pols.x, self.pols.y, self.pols.width, self.pols.height)
            if self.pols.collidepoint(event.pos):
                print('collided')
                self.set_hovered(True)
                self.first_pos_mouse = event.pos
        elif event.type == pygame.MOUSEMOTION:
            if self.hovered:
                d_y = event.pos[1] - self.first_pos_mouse[1]
                self.pols = self.pols.move(0, d_y)
                if self.pols.y < 0:
                    self.pols.y = 0
                elif self.pols.y + self.pols.height > self.height:
                    self.pols.y = self.height - self.pols.height
                self.first_pos_mouse = (self.first_pos_mouse[0],
                                        self.first_pos_mouse[1] + d_y)

    def draw(self, surface):
        pygame.draw.rect(self.surface, (75, 75, 75),
                         (0, 0, self.width, self.height))
        pygame.draw.rect(self.surface, (125, 125, 125), self.pols)
        surface.blit(self.surface, self.rect)


class Button(BaseWidget):
    FONT = pygame.font.SysFont('arial', 12)

    def __init__(self, x, y, width, height, text, func):
        super().__init__(x, y, width, height)
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
            pygame.draw.rect(surface, (150, 150, 150), self.rect)
        else:
            pygame.draw.rect(surface, (180, 180, 180), self.rect)
        text = self.FONT.render(self.text, True, (255, 255, 255))
        pos_x = self.x + (self.width - text.get_width()) // 2
        pos_y = self.y + (self.height - text.get_height()) // 2
        surface.blit(text, (pos_x, pos_y))


class LineEdit(BaseWidget):
    FONT = pygame.font.SysFont('arial', 12)

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.text = ''

    def update(self, event):
        if event.type != pygame.KEYDOWN:
            return None
        self.text += event.unicode

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
        text_surface = self.FONT.render(self.text, True, (0, 0, 0))
        surface.blit(text_surface, (self.x + 5, self.y + 5))


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
