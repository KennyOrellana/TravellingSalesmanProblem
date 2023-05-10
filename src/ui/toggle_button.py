import pygame

from src.ui.button import Button


class ToggleButton(Button):
    def __init__(self, title, toggled_title, position, callback, width=200, height=36, font_size=24,
                 button_color=(0, 200, 0), text_color=(255, 255, 255)):
        super().__init__(title, position, callback, width, height, font_size, button_color, text_color)
        self.toggled_title = toggled_title
        self.is_toggled = False

    def draw(self, screen):
        # Choose the appropriate title based on the is_toggled state
        display_title = self.toggled_title if self.is_toggled else self.title
        print(self.is_toggled, self.title, self.toggled_title, display_title)

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
        text_surface = font.render(display_title, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)

        screen.blit(text_surface, text_rect)

    def on_click(self):
        self.is_toggled = not self.is_toggled
        super().on_click()
