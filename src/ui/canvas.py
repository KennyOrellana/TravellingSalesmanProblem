import pygame

from src.environment.settings import Settings


class Canvas:
    def __init__(self):
        self.screen = pygame.display.set_mode(self.get_screen_size(), pygame.FULLSCREEN)
        self.screen.fill(Settings.BACKGROUND_COLOR)
        self.screen_width, self.screen_height = self.screen.get_size()
        pygame.display.set_caption("Node Drawing Canvas")

    def clear(self):
        self.screen.fill(Settings.BACKGROUND_COLOR)

    @staticmethod
    def get_screen_size():
        pygame.init()
        screen_info = pygame.display.Info()
        return screen_info.current_w, screen_info.current_h

    def get_screen_height(self):
        if self.screen_height is None:
            self.screen_height = self.get_screen_size()[0]

        return self.screen_height
