import math
import random

from src.environment.settings import Settings
from src.models.ant import Ant
from src.models.simulation import Simulation
from src.ui.manager import Manager


class AntBehaviour(Simulation):
    def __init__(self):
        self.manager = None
        self.iteration = 0
        self.ant = None
        self.visited_nodes = []

    def start(self, canvas, environment):
        self.manager = Manager(canvas, environment)
        self.manager.draw_nodes()
        initial_index = random.randint(0, len(self.manager.environment.nodes) - 1)
        self.ant = Ant.from_node(self.manager.environment.nodes[initial_index])
        self.manager.add_ant(self.ant)
        self.visited_nodes.append(initial_index)

    def tick(self):
        print("tick ant behaviour")
        # self.iteration += 1
        # if self.iteration > 1:
        self.manager.tick()

        if len(self.visited_nodes) != len(self.manager.environment.nodes):
            next_node_index = self.select_next_node()
            self.visited_nodes.append(next_node_index)
            self.manager.draw_next_node(next_node_index)
            self.manager.ants[0] = Ant.from_node(self.manager.environment.nodes[next_node_index])

    def select_next_node(self):
        desirabilities = []
        available_nodes = []

        for index, node in enumerate(self.manager.environment.nodes):
            if index not in self.visited_nodes:
                available_nodes.append(index)
                desirabilities.append(self.desirability(node))

        # Normalize desirabilities to sum to 1
        total_desirability = sum(desirabilities)
        normalized_desirabilities = [desirability / total_desirability for desirability in desirabilities]

        # Select the next node based on randomness of the desirabilities
        next_node_index = random.choices(available_nodes, normalized_desirabilities)[0]

        return next_node_index

    def desirability(self, node):
        distance = self.ant.distance_to(node)
        desirability = math.pow(1 / distance, Settings.DESIRABILITY_POWER)
        return desirability
