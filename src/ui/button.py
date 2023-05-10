import pygame
import pygame


class Button:
    def __init__(self, title, position, callback, width=200, height=36, font_size=24,
                 button_color=(0, 200, 0), text_color=(255, 255, 255)):
        self.title = title
        self.position = position
        self.callback = callback
        self.width = width
        self.height = height
        self.font_size = font_size
        self.button_color = button_color
        self.text_color = text_color
        self.corner_radius = height // 2
        self.rect = pygame.Rect(position[0], position[1], width, height)

    def draw(self, screen):
        # Draw left and right semi-circles
        pygame.draw.circle(screen, self.button_color,
                           (self.position[0] + self.corner_radius, self.position[1] + self.height // 2),
                           self.corner_radius)
        pygame.draw.circle(screen, self.button_color,
                           (self.position[0] + self.width - self.corner_radius, self.position[1] + self.height // 2),
                           self.corner_radius)

        # Draw the middle part of the button
        pygame.draw.rect(screen, self.button_color, (
        self.position[0] + self.corner_radius, self.position[1], self.width - 2 * self.corner_radius, self.height))

        # Draw the text
        font = pygame.font.Font(None, self.font_size)
        text_surface = font.render(self.title, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)

        screen.blit(text_surface, text_rect)

    # The rest of the Button class implementation remains unchanged
