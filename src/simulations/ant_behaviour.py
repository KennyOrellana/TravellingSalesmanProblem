import math
import random

from src.environment.settings import Settings
from src.models.ant import Ant
from src.models.simulation import Simulation
from src.ui.manager import Manager


class AntBehaviour(Simulation):
    STEPS = 3

    def __init__(self):
        self.manager = None
        self.iteration = -1
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
        self.manager.draw_nodes()
        self.draw_current_path()
        self.manager.draw_ants()

        self.iteration += 1
        self.iteration %= self.STEPS

        if self.iteration == 1:
            self.draw_option_lines()
        elif self.iteration == 2:
            self.draw_option_lines()
            self.move_to_next_node()
        # else if self.iteration == 3:
        # animate transition

        # self.manager.tick()

    def draw_current_path(self):
        if len(self.visited_nodes) > 1:
            for i in range(len(self.visited_nodes) - 1):
                self.manager.environment.nodes[self.visited_nodes[i]].draw_line_to_node(
                    self.manager.canvas.screen,
                    self.manager.environment.nodes[self.visited_nodes[i + 1]],
                    Settings.NODE_COLOR, Settings.LINE_THICKNESS
                )

        if len(self.visited_nodes) == len(self.manager.environment.nodes):
            self.manager.environment.nodes[self.visited_nodes[-1]].draw_line_to_node(
                self.manager.canvas.screen,
                self.manager.environment.nodes[self.visited_nodes[0]],
                Settings.NODE_COLOR, Settings.LINE_THICKNESS
            )

    def draw_option_lines(self):
        available_nodes = []

        for index, node in enumerate(self.manager.environment.nodes):
            if index not in self.visited_nodes:
                available_nodes.append(index)

        if len(available_nodes) > 0:
            self.manager.draw_option_nodes(available_nodes)

    def move_to_next_node(self):
        if len(self.visited_nodes) != len(self.manager.environment.nodes):
            next_node_index = self.find_next_node()
            self.visited_nodes.append(next_node_index)
            self.manager.draw_next_node(next_node_index)
            self.manager.ants[0] = Ant.from_node(self.manager.environment.nodes[next_node_index])
            # self.ant = Ant.from_node(self.manager.environment.nodes[next_node_index])
            # self.manager.ants[0] = self.ant

    def find_next_node(self):
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
