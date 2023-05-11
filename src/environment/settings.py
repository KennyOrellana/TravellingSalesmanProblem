import pygame


class Settings:
    COLOR1 = pygame.Color('#321055')
    COLOR2 = pygame.Color('#A391B7')
    COLOR3 = pygame.Color('#6CBDDC')
    # COLOR4 = pygame.Color('#E9F5F7')
    COLOR4 = pygame.Color('#DBEEF6')
    COLOR5 = pygame.Color('#4B6D2E')
    COLOR6 = pygame.Color('#EFF9E8')
    DIVIDER = pygame.Color('#DADCDE')

    RESET = False
    NUM_NODES = 100
    INITIAL_ANTS = 0
    FPS = 120
    DEMO = False
    PAUSED = True
    DELAY_DEFAULT = 1_000
    DELAY = DELAY_DEFAULT
    ANIMATION_SPEED = 0.05

    NODE_RADIUS = 10
    LINE_THICKNESS = 4  # NODE_RADIUS // 2
    NODE_OPTIONS_THICKNESS = NUM_NODES // 2

    SIDEBAR_WIDTH = 200
    BACKGROUND_COLOR = pygame.Color('#F7F9FC')
    # SIDEBAR_COLOR = pygame.Color('#F1F3F4')
    SIDEBAR_COLOR = pygame.Color('#F1F3F4')
    TITLE_COLOR = pygame.Color('#0a1225')
    TEXT_COLOR = pygame.Color('#5E5E5E')
    BUTTON_COLOR = COLOR3
    # TEXT_COLOR = pygame.Color('#0AB75B')
    TEXT_SIZE = 22

    # NODE_COLOR = pygame.Color('#0262E4')
    NODE_COLOR = COLOR1
    LINE_COLOR = COLOR2
    # CURRENT_NODE_COLOR = pygame.Color('#0C203D')

    NODE_OPTIONS_COLOR = pygame.Color('#858F9E')
    SELECTED_NODE_COLOR = pygame.Color('#0C203D')

    DESIRABILITY_POWER = 4
    PHEROMONE_POWER = 2
    PHEROMONE_INITIAL = 1
    PHEROMONE_INTENSITY = 10
    PHEROMONE_EVAPORATION = 0.3

    # UI
    UI_PADDING = 10
    LABEL_WIDTH = 170
    BUTTON_WIDTH = 85
    BUTTON_WIDTH_FULL = 180
    BUTTON_HEIGHT = 20
    ROW_PADDING = 20
    PADDING = 50
