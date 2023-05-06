from src.models.ant import Ant
from src.models.simulation import Simulation
from src.ui.manager import Manager


class AntBehaviour(Simulation):
    def __init__(self):
        self.manager = None
        self.iteration = 0
        self.ant = None

    def start(self, canvas, environment):
        self.manager = Manager(canvas, environment)
        self.manager.draw_nodes()
        self.ant = Ant.from_node(self.manager.environment.nodes[0])
        self.manager.add_ant(self.ant)

    def tick(self):
        print("tick ant behaviour")
        self.iteration += 1
        if self.iteration > 1:
            self.manager.tick()
