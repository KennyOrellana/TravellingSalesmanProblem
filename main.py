import pygame

from src.core.orchestrator import Orchestrator
from src.environment.settings import Settings
from src.models.environment import Environment


def main():
    pygame.init()

    orchestrator = Orchestrator(Environment())
    # orchestrator = Orchestrator(Environment(), AntColony())

    pygame.display.update()

    pause = False
    run = True

    # Create a clock object and set the desired FPS
    clock = pygame.time.Clock()

    while run:
        # Limit the game loop to the desired FPS
        clock.tick(Settings.FPS)

        orchestrator.tick()
        if not pause:
            orchestrator.add_iteration()

            # pygame.time.delay(Settings.DELAY)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    pause = not pause
                    # orchestrator.add_iteration()


if __name__ == "__main__":
    main()
