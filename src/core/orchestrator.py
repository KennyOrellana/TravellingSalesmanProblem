from src.environment.ant_colony import AntColony
from src.ui.canvas import Canvas


# Create another orchestrator to execute simulation as fast as possible on multiple threads
class Orchestrator:
    def __init__(self, environment):
        self.canvas = Canvas()
        self.environment = environment
        self.manager = AntColony(self.canvas, self.environment)

    def tick(self):
        self.canvas.clear()
        self.manager.tick()

    def add_iteration(self):
        self.manager.add_iteration()
