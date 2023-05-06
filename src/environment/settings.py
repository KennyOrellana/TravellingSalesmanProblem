import pygame


class Settings:
    LINE_THICKNESS = 5
    FPS = 30
    DELAY = 5_000 // FPS
    PADDING = 50
    NODE_RADIUS = 10
    NODE_COLOR = (0xF45A47)  # HEX color for white
    BACKGROUND_COLOR = pygame.Color('#F7F5F7')  # HEX color for black
    LINE_COLOR = pygame.Color('#6C559A')
    NEXT_NODE_COLOR = pygame.Color('#927B90')
    NEXT_NODE_THICKNESS = 7
    ANT_COLOR = pygame.Color('#6C559A')
    ANT_ALPHA = int(255 * 0.66)
    DESIRABILITY_POWER = 2.3
