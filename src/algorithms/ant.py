import math
import random

from src.environment.settings import Settings
from src.models.node import Node


class Ant(Node):
    def __init__(self, manager):
        initial_index = random.randint(0, manager.environment.total_nodes - 1)
        initial_node = manager.environment.nodes[initial_index]
        super().__init__(initial_node.x, initial_node.y)
        self.manager = manager
        self.visited_nodes = [initial_index]
        self.total_distance = 0
        self.next_node_index = None

    def tick(self):
        # self.draw_current_path()

        if len(self.visited_nodes) == self.manager.environment.total_nodes:
            self.compute_distance()
            self.manager.ant_finished(self)
        else:
            self.next_node_index = self.find_next_node()
            self.move_to_next_node()

    def draw_current_path(self, color=Settings.NODE_COLOR):
        if len(self.visited_nodes) == 1:
            return

        for i in range(len(self.visited_nodes) - 1):
            self.manager.get_node_at(self.visited_nodes[i]).draw_line_to_node(
                self.manager.canvas.screen,
                self.manager.environment.nodes[self.visited_nodes[i + 1]],
                color, Settings.LINE_THICKNESS
            )

    def move_to_next_node(self):
        self.manager.followed_path(self.visited_nodes[-1], self.next_node_index)
        self.visited_nodes.append(self.next_node_index)
        next_node = self.manager.environment.nodes[self.next_node_index]
        self.x = next_node.x
        self.y = next_node.y
        self.next_node_index = None

    def find_next_node(self):
        desirabilities = []
        available_nodes = []

        for index, node in enumerate(self.manager.environment.nodes):
            if index not in self.visited_nodes:
                available_nodes.append(index)
                desirabilities.append(self.desirability(index, node))

        # If there is only one node left, return it
        if len(available_nodes) == 0:
            return self.visited_nodes[0]

        # Normalize desirabilities to sum to 1
        total_desirability = sum(desirabilities)
        normalized_desirabilities = [desirability / total_desirability for desirability in desirabilities]

        self.next_node_option(available_nodes, normalized_desirabilities)

        # Select the next node based on randomness of the desirabilities
        next_node_index = random.choices(available_nodes, normalized_desirabilities)[0]

        return next_node_index

    def next_node_option(self, available_nodes, normalized_desirabilities):
        pass

    def desirability(self, index, node):
        distance = self.distance_to(node)
        pheromone = self.manager.get_pheromone_value(self.visited_nodes[-1], index)
        desirability = math.pow(1 / distance, Settings.DESIRABILITY_POWER) * math.pow(pheromone,
                                                                                      Settings.PHEROMONE_POWER)
        return desirability

    def draw_option_nodes(self, available_nodes, normalized_desirabilities):
        for index, node in enumerate(self.manager.environment.nodes):
            if index in available_nodes:
                position = available_nodes.index(index)
                self.draw_line_to_node(
                    self.manager.canvas.screen,
                    node,
                    line_thickness=int(
                        round(Settings.NODE_OPTIONS_THICKNESS * normalized_desirabilities[position])),
                )

    def compute_distance(self):
        if len(self.visited_nodes) < self.manager.environment.total_nodes:
            return

        for i in range(self.manager.environment.total_nodes - 1):
            current_node = self.manager.get_node_at(self.visited_nodes[i])
            next_node = self.manager.get_node_at(self.visited_nodes[i + 1])
            self.total_distance += current_node.distance_to(next_node)

        # Handle the wrap-around case (from the last node to the first node)
        self.total_distance += self.manager.get_node_at(self.visited_nodes[-1]).distance_to(
            self.manager.get_node_at(self.visited_nodes[0]))

        self.manager.ant_finished(self)
