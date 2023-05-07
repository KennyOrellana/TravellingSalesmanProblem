import pygame


class Settings:
    FPS = 30
    DELAY = 10_000 // FPS
    PADDING = 50

    NODE_RADIUS = 10
    LINE_THICKNESS = NODE_RADIUS // 2

    BACKGROUND_COLOR = pygame.Color('#F7F9FC')

    NODE_COLOR = pygame.Color('#0262E4')
    CURRENT_NODE_COLOR = pygame.Color('#0C203D')

    NODE_OPTIONS_COLOR = pygame.Color('#858F9E')
    SELECTED_NODE_COLOR = pygame.Color('#0C203D')

    DESIRABILITY_POWER = 2.3
