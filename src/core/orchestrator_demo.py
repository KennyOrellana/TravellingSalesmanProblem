from src.core.orchestrator import Orchestrator
from src.environment.ant_colony import AntColony
from src.environment.drawer import Drawer
from src.environment.settings import Settings
from src.ui.canvas import Canvas


# Create another orchestrator to execute simulation as fast as possible on multiple threads
class OrchestratorDemo(Orchestrator):
    def __init__(self, gui):
        super().__init__(gui, demo=True)
        self.counter = 0

    def tick(self):
        self.counter += 1
        if self.counter % Settings.DELAY == 0:
            super().tick()

    def add_iteration(self):
        pass
