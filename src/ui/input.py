import pygame
from pygame.locals import *


class InputNumber:
    def __init__(self, x, y, width, height, initial_value=0, font_size=32, font_color=(0, 0, 0), bg_color=(255, 255, 255), variable=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.bg_color = bg_color
        self.font_color = font_color
        self.font_size = font_size
        self.font = pygame.font.Font(None, self.font_size)
        self.variable = variable

        if self.variable:
            self.text = str(self.variable.get())
        else:
            self.text = str(initial_value)
        self.surface = self.font.render(self.text, True, self.font_color)

    def event_handler(self, event):
        if event.type == KEYDOWN:
            if event.key in (K_RETURN, K_KP_ENTER):
                if self.variable:
                    self.variable.set(int(self.text))
            elif event.key == K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.unicode.isdigit():
                self.text += event.unicode

            self.surface = self.font.render(self.text, True, self.font_color)

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect)
        text_rect = self.surface.get_rect(center=self.rect.center)
        screen.blit(self.surface, text_rect)
