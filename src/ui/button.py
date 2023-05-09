import pygame


class Button:
    def __init__(self, title, position, callback, width=200, height=60, font_size=36,
                 button_color=(0, 200, 0), text_color=(255, 255, 255)):
        self.title = title
        self.position = position
        self.callback = callback
        self.width = width
        self.height = height
        self.font_size = font_size
        self.button_color = button_color
        self.text_color = text_color
        self.rect = pygame.Rect(position[0], position[1], width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.button_color, self.rect)

        font = pygame.font.Font(None, self.font_size)
        text_surface = font.render(self.title, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)

        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()
