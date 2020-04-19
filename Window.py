import pygame

pygame.init()


class Window:
    def __init__(self, width, height, title, background=(0, 0, 0)):
        self.width = width
        self.height = height
        self.background = background
        self.win_obj = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        self.surf = pygame.Surface((width, height), pygame.SRCALPHA)

    def get_size(self):
        return self.width, self.height

    def get_background(self):
        return self.background

    def get_surf(self):
        return self.surf

    def get_title(self):
        return pygame.display.get_caption()

    def set_size(self, width, height):
        self.win_obj = None
        self.surf = None
        self.win_obj = pygame.display.set_mode((width, height))
        self.surf = pygame.Surface((width, height))
        self.width, self.height = width, height

    def set_background(self, background):
        self.background = background

    def set_surf(self, width, height):
        self.surf = None
        self.surf = pygame.Surface((width, height))

    def set_title(self, title):
        pygame.display.set_caption(title)

    def draw(self, obj, pos_x, pos_y):
        self.win_obj.blit(obj, (pos_x, pos_y))

    def draw_surface(self, pos_x, pos_y):
        self.win_obj.blit(self.surf, (pos_x, pos_y))

    def fill_surface(self, color):
        self.surf.fill(color)

    def fill_window(self):
        self.win_obj.fill(self.background)

    def update(self):
        pygame.display.flip()

    def __del__(self):
        self.width = None
        self.height = None
        self.title = None
        self.win_obj = None
        self.surf = None
