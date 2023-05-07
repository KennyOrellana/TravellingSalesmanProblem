from src.ui.canvas import Canvas


# Create another orchestrator to execute simulation as fast as possible on multiple threads
class Orchestrator:
    def __init__(self, environment, simulations):
        self.playing = False
        self.canvas = Canvas()
        self.environment = environment
        self.simulations = simulations
        self.start()

    def start(self):
        self.playing = True
        for simulation in self.simulations:
            simulation.start(self.canvas, self.environment)

    def pause(self):
        self.playing = False
        for simulation in self.simulations:
            simulation.pause()

    def tick(self):
        self.canvas.clear()
        # if self.playing:
        for simulation in self.simulations:
            simulation.tick()
