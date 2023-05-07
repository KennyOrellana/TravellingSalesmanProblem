import pygame

from src.core.orchestrator import Orchestrator
from src.environment.settings import Settings
from src.models.environment import Environment
from src.simulations.ant_behaviour import AntBehaviour


def create_simulations():
    return [
        AntBehaviour(),  # add more ants
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
        clock.tick(Settings.FPS)

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

        pygame.time.delay(Settings.DELAY)


if __name__ == "__main__":
    main()
