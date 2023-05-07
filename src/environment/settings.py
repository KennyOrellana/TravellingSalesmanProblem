import pygame


class Settings:
    NUM_NODES = 50
    FPS = 120
    # DELAY = 0  # 10_000 // FPS
    DELAY = 100_000 // FPS
    PADDING = 50

    NODE_RADIUS = 10
    LINE_THICKNESS = 2  # NODE_RADIUS // 2
    NODE_OPTIONS_THICKNESS = NUM_NODES // 2

    BACKGROUND_COLOR = pygame.Color('#F7F9FC')
    TEXT_COLOR = pygame.Color('#0AB75B')

    NODE_COLOR = pygame.Color('#0262E4')
    CURRENT_NODE_COLOR = pygame.Color('#0C203D')

    NODE_OPTIONS_COLOR = pygame.Color('#858F9E')
    SELECTED_NODE_COLOR = pygame.Color('#0C203D')

    DESIRABILITY_POWER = 2.3
    PHEROMONE_POWER = 2
