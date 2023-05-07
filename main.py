import pygame

from src.core.orchestrator import Orchestrator
from src.environment.settings import Settings
from src.models.environment import Environment
from src.algorithms.ant_behaviour import AntBehaviour


def create_simulation():
    return [AntBehaviour()]


def create_simulations():
    return [
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
        AntBehaviour(),  # add more ants
    ]


def create_environment():
    return Environment()


def main():
    pygame.init()

    orchestrator = Orchestrator(create_environment(), create_simulation())

    pygame.display.update()

    pause = False
    run = True
    counter = 0

    # Create a clock object and set the desired FPS
    clock = pygame.time.Clock()

    while run:
        # Limit the game loop to the desired FPS
        clock.tick(Settings.FPS)

        orchestrator.tick()
        if not pause:
            counter += 1
            if counter % 2 == 0 and Settings.DELAY == 0:
                orchestrator.add_ant()

            pygame.time.delay(Settings.DELAY)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    # orchestrator.add_ant()
                    pause = not pause
                    # started = True


if __name__ == "__main__":
    main()
