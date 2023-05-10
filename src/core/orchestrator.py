from src.environment.ant_colony import AntColony
from src.environment.drawer import Drawer
from src.environment.settings import Settings


class Orchestrator:
    def __init__(self, gui):
        self.gui = gui
        self.canvas = gui.canvas
        self.environment = gui.environment
        self.manager = AntColony(self.canvas, self.environment)
        self.drawer = Drawer(self.canvas, self.environment)

    def tick(self):
        self.gui.tick()
        self.manager.tick()

        self.gui.draw_summary(self.manager.total_ants)

        if self.environment.shortest_path_size is not None:
            self.drawer.draw_path(self.environment.shortest_path, Settings.LINE_COLOR)

    def add_iteration(self):
        self.manager.add_iteration()
