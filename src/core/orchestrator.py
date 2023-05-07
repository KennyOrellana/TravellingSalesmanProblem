from src.environment.ant_colony import AntColony
from src.environment.drawer import Drawer
from src.environment.settings import Settings
from src.ui.canvas import Canvas


# Create another orchestrator to execute simulation as fast as possible on multiple threads
class Orchestrator:
    def __init__(self, environment):
        self.canvas = Canvas()
        self.environment = environment
        self.manager = AntColony(self.canvas, self.environment)
        self.drawer = Drawer(self.canvas, self.environment)

    def tick(self):
        self.canvas.clear()
        self.manager.tick()

        self.drawer.draw_summary(self.manager.total_ants)

        if self.environment.shortest_path_size is not None:
            self.drawer.draw_nodes()
            self.drawer.draw_path(self.environment.shortest_path, Settings.TEXT_COLOR)

    def add_iteration(self):
        self.manager.add_iteration()
