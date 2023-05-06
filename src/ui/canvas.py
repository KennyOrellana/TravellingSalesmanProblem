import pygame

from src.environment.settings import Settings


class Canvas:
    def __init__(self):
        self.screen = pygame.display.set_mode(self.get_screen_size(), pygame.FULLSCREEN)
        self.screen.fill(Settings.BACKGROUND_COLOR)
        pygame.display.set_caption("Node Drawing Canvas")

    def clear(self):
        self.screen.fill(Settings.BACKGROUND_COLOR)

    @staticmethod
    def get_screen_size():
        screen_info = pygame.display.Info()
        return screen_info.current_w, screen_info.current_h
