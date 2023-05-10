import pygame

from src.environment.settings import Settings


class Label:
    def __init__(self, x, y, text, font_size=Settings.TEXT_SIZE, color=Settings.TEXT_COLOR, font=None, max_width=None, align='left'):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.font_size = font_size
        self.font = font if font else pygame.font.Font(None, font_size)
        self.max_width = max_width
        self.align = align

    def draw(self, screen):
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        if self.align == 'center':
            text_rect.centerx = self.x + ((self.max_width - Settings.UI_PADDING) // 2 if self.max_width is not None else 0)
        elif self.align == 'right':
            text_rect.right = self.x + (self.max_width if self.max_width is not None else 0)
        else:
            text_rect.left = self.x
        text_rect.y = self.y
        screen.blit(text_surface, text_rect)
