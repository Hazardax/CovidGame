import pygame

pygame.init()


class Text:
    def __init__(self, pos_x, pos_y, size, content="text", font_name="Consolas", color=(255, 255, 255, 255)):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = size
        self.content = content
        self.color = color
        self.font_name = font_name
        self.font = pygame.font.SysFont(font_name, size)
        self.text_alpha = 50

    def get_pos(self):
        return self.pos_x, self.pos_y

    def get_size(self):
        return self.size

    def get_text(self):
        return self.content

    def get_color(self):
        return self.color

    def get_font(self):
        return self.font_name

    def get_alpha(self):
        return self.text_alpha

    def set_pos(self, pos_x, pos_y):
        self.pos_x, self.pos_y = pos_x, pos_y

    def set_size(self, size):
        self.size = size

    def set_text(self, content):
        self.content = content

    def set_color(self, color):
        self.color = color

    def set_font(self, font_name):
        self.font_name = None
        self.font = None

        self.font_name = font_name
        self.font = pygame.font.SysFont(font_name, self.size)

    def set_alpha(self, alpha):
        self.text_alpha = alpha

    def print(self, window):
        temp_text = self.font.render(self.content, False, self.color)
        temp_text.set_alpha(self.text_alpha)
        window.draw(temp_text, self.pos_x, self.pos_y)

    def instant_print(self, window, content):
        temp_text = self.font.render(content, False, self.color)
        temp_text.set_alpha(self.text_alpha)
        window.draw(temp_text, self.pos_x, self.pos_y)

    def __del__(self):
        self.pos_x = None
        self.pos_y = None
        self.size = None
        self.text = None
        self.color = None
        self.font_name = None
        self.font = None
        self.text = None
