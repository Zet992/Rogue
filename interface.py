import pygame

from settings import WINDOW_SIZE


class Button:
    def __init__(self, surface, x, y, width, height, text, func, image=None, font_size=36, font_color=(255, 255, 255),
                 hover_font_color=(66, 245, 96), border_radius=8):
        self.surface = surface
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.func = func
        self.font_size = font_size
        self.font_color = font_color
        self.font = pygame.font.Font(None, self.font_size)
        self.text = text
        self.image = image
        self.hover_font_color = hover_font_color
        self.hovered = False
        self.button_pressed_sound = pygame.mixer.Sound('data\\sounds\\interface\\button_pressed.wav')
        self.border_radius = border_radius

    def draw(self):
        pygame.draw.rect(self.surface, (115, 155, 235), (self.x, self.y, self.width, self.height),
                         border_radius=self.border_radius)
        if not self.hovered:
            self.title = self.font.render(str(self.text), 1, self.font_color)
            text_rect = self.title.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        else:
            self.title = self.font.render(str(self.text), 1, self.hover_font_color)
            text_rect = self.title.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.surface.blit(self.title, text_rect)

        if self.image:
            x = (self.width - self.image.get_width()) // 2 + self.x
            y = (self.height - self.image.get_height()) // 2 + self.y
            self.surface.blit(self.image, (x, y))

    def check_click(self, x_cursor, y_cursor):
        if self.x < x_cursor < self.x + self.width and self.y < y_cursor < self.y + self.height:
            return True
        return False

    def check_hover(self, x_cursor, y_cursor):
        if self.x < x_cursor < self.x + self.width and self.y < y_cursor < self.y + self.height:
            self.hovered = True
        else:
            self.hovered = False

    def clicked(self):
        self.button_pressed_sound.play()
        self.func()


class RadioButton(Button):
    def __init__(self, surface, x, y, width, height, text, func, on_image=None, off_image=None,
                 font_size=36, font_color=(255, 255, 255),
                 hover_font_color=(66, 245, 96), border_radius=8, is_active=False):
        super().__init__(surface, x, y, width, height, text, func, on_image,
                         font_size, font_color, hover_font_color,
                         border_radius)

        self.on_image = on_image
        self.off_image = off_image
        self.is_active = is_active

    def set_is_active(self, is_active):
        self.is_active = is_active
        if self.is_active:
            self.image = self.on_image
        else:
            self.image = self.off_image


    def clicked(self):
        self.set_is_active(not self.is_active)
        self.button_pressed_sound.play()
        self.func()


class HealthBar:
    def __init__(self):
        self.width = int(WINDOW_SIZE[0] * 0.0977)
        self.height = int(WINDOW_SIZE[1] * 0.026)

    def draw(self, surface, hp):
        pygame.draw.rect(surface, 'green', (
            10, 10, 10 + int(self.width * hp // 100),
            10 + self.height))
        pygame.draw.rect(surface, 'black', (
            10, 10, 10 + self.width,
            10 + self.height), 3)


class MoneyCounter:
    def __init__(self):
        self.image = pygame.image.load('data\\images\\bonuses\\money\\money_1.png')
        self.image = pygame.transform.scale2x(self.image)
        self.font = pygame.font.Font(None, 32)

    def draw(self, surface, money):
        title = self.font.render(str(money), 1, (255, 72, 72))
        text_rect = title.get_rect(center=(62, 61))
        surface.blit(self.image, (10, 45))
        surface.blit(title, text_rect)
