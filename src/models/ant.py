import pygame

from src.environment.settings import Settings
from src.models.node import Node


class Ant(Node):
    def __init__(self, x, y):
        super().__init__(x, y)

    @classmethod
    def from_node(cls, node):
        return cls(node.x, node.y)

    def draw(self, screen):
        ant_color = Settings.ANT_COLOR
        ant_color.a = Settings.ANT_ALPHA
        pygame.draw.circle(screen, ant_color, (self.x, self.y), Settings.NODE_RADIUS)


