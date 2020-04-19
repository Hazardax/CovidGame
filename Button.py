import pygame

pygame.init()


class Button:
    def __init__(self, pos_x, pos_y, width, height):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.color = (255, 255, 255, 255)
        self.height = height

    def get_pos(self):
        return self.pos_x, self.pos_y

    def get_size(self):
        return self.width, self.height

    def get_color(self):
        return self.color

    def set_pos(self, pos_x, pos_y):
        self.pos_x, self.pos_y = pos_x, pos_y

    def set_size(self, width, height):
        self.width, self.height = width, height

    def set_color(self, color):
        self.color = color

    def intersects(self):
        if self.pos_x < pygame.mouse.get_pos()[0] < self.pos_x + self.width \
                and self.pos_y < pygame.mouse.get_pos()[1] < self.pos_y + self.height:
            return True
        return False

    def draw(self, window):
        pygame.draw.rect(window.get_surf(), self.color, (self.pos_x, self.pos_y, self.width, self.height))

    def is_pressed(self):
        if pygame.mouse.get_pressed()[0] and self.pos_x < pygame.mouse.get_pos()[0] < self.pos_x + self.width \
                and self.pos_y < pygame.mouse.get_pos()[1] < self.pos_y + self.height:
            return True
        return False

    def __del__(self):
        self.pos_x = None
        self.pos_y = None
        self.width = None
        self.color = None
        self.height = None
