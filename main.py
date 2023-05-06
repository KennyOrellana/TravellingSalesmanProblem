import sys

import pygame

from src.core.orchestrator import Orchestrator
from src.environment.settings import Settings
from src.models.environment import Environment
from src.models.node import Node
from src.models.simulation import Simulation
from src.simulations.ant_behaviour import AntBehaviour
from src.ui.canvas import Canvas
from src.ui.manager import Manager


def create_simulations():
    return [
        AntBehaviour(),
    ]


def create_environment():
    return Environment()


def main():
    pygame.init()

    orchestrator = Orchestrator(create_environment(), create_simulations())

    pygame.display.update()

    pause = True
    run = True

    # Create a clock object and set the desired FPS
    clock = pygame.time.Clock()

    while run:
        # Limit the game loop to the desired FPS
        # clock.tick(Settings.FPS)

        print("tick main")
        orchestrator.tick()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    pause = not pause
                    started = True


if __name__ == "__main__":
    main()
