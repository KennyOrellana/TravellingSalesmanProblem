import pygame

from src.core.orchestrator import Orchestrator
from src.core.orchestrator_demo import OrchestratorDemo
from src.environment.settings import Settings
from src.ui.gui import GUI


def main():
    gui_manager = GUI()
    orchestrator = OrchestratorDemo(gui_manager)

    pygame.display.update()

    run = True

    # Create a clock object and set the desired FPS
    clock = pygame.time.Clock()

    while run:
        if Settings.RESET:
            gui_manager.reset()
            Settings.RESET = False
            orchestrator = Orchestrator(gui_manager)

        # Limit the game loop to the desired FPS
        # if Settings.DEMO:
        #     clock.tick(10)
        # else:
        #     clock.tick(120)
        clock.tick(Settings.FPS)

        orchestrator.tick()
        if not Settings.PAUSED:
            orchestrator.add_iteration()

        pygame.display.flip()

        if Settings.DEMO:
            pygame.time.delay(Settings.DELAY)

        events = pygame.event.get()
        gui_manager.handle_events(events)

        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    Settings.PAUSED = not Settings.PAUSED
                    # orchestrator.add_iteration()


if __name__ == "__main__":
    main()
