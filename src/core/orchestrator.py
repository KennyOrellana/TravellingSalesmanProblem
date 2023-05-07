from src.algorithms.ant_behaviour import AntBehaviour
from src.environment.ant_colony import AntColony
from src.ui.canvas import Canvas
from src.ui.manager import Manager


# Create another orchestrator to execute simulation as fast as possible on multiple threads
class Orchestrator:
    def __init__(self, environment, simulations):
        self.playing = False
        self.canvas = Canvas()
        self.environment = environment
        self.simulations = simulations
        self.manager = AntColony(self.canvas, self.environment)
        self.start()

    def start(self):
        self.playing = True
        for simulation in self.simulations:
            simulation.start(self.canvas, self.environment, self.manager)

    def pause(self):
        self.playing = False
        for simulation in self.simulations:
            simulation.pause()

    def tick(self):
        self.canvas.clear()
        # if self.playing:
        for simulation in self.simulations:
            simulation.tick()

        self.manager.tick()
        self.manager.draw_summary(len(self.simulations))

    def add_ant(self):
        self.simulations.append(AntBehaviour())
        self.simulations[-1].start(self.canvas, self.environment, self.manager)
