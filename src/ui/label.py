import pygame

from src.environment.settings import Settings


class Label:
    def __init__(self, x, y, text, font_size=Settings.TEXT_SIZE, color=Settings.TEXT_COLOR, font=None):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.font_size = font_size
        self.font = font if font else pygame.font.Font(None, font_size)

    def draw(self, screen):
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.x, self.y))
