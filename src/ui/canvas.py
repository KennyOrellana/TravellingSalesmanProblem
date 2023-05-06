import pygame

from src.environment.settings import Settings


class Canvas:
    def __init__(self):
        self.screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
        pygame.display.set_caption("Node Drawing Canvas")

    def clear(self):
        self.screen.fill(Settings.BACKGROUND_COLOR)
