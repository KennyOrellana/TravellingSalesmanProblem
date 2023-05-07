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
        pygame.draw.circle(screen, Settings.CURRENT_NODE_COLOR, (self.x, self.y), Settings.NODE_RADIUS)
