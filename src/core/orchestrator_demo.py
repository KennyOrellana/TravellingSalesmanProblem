from src.core.orchestrator import Orchestrator
from src.environment.settings import Settings


class OrchestratorDemo(Orchestrator):
    def __init__(self, gui):
        super().__init__(gui)
        self.counter = 0

    def tick(self):
        if Settings.DEMO:
            self.counter += 1
            if self.counter % Settings.DELAY == 0:
                super().tick()
        else:
            super().tick()
