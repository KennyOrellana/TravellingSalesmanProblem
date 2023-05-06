import pygame

from src.environment.settings import Settings


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, Settings.NODE_COLOR, (self.x, self.y), Settings.NODE_RADIUS)
