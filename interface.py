import pygame


class Button:
    def __init__(self, surface, x, y, width, height, text, func, font_size=36, font_color=(255, 255, 255),
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
