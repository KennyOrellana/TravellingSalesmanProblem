import math
import random

from src.environment.settings import Settings
from src.models.node import Node


# Use diferent color for each ant
class Ant(Node):
    def __init__(self, manager):
        initial_index = random.randint(0, manager.environment.total_nodes - 1)
        initial_node = manager.environment.nodes[initial_index]
        super().__init__(initial_node.x, initial_node.y)
        self.manager = manager
        self.visited_nodes = [initial_index]
        self.total_distance = 0

    def tick(self):
        if self.total_distance == 0:  # Only draw when haven't finished
            self.draw_current_path()
            self.manager.draw_ants(self)

            self.move_to_next_node()

            if self.total_distance > 0:
                self.manager.ant_finished(self)

    def draw_current_path(self, color=Settings.NODE_COLOR):

        if len(self.visited_nodes) > 1:
            for i in range(len(self.visited_nodes) - 1):
                self.manager.environment.nodes[self.visited_nodes[i]].draw_line_to_node(
                    self.manager.canvas.screen,
                    self.manager.environment.nodes[self.visited_nodes[i + 1]],
                    color, Settings.LINE_THICKNESS
                )

        if len(self.visited_nodes) == len(self.manager.environment.nodes):
            self.total_distance = self.polygon_distance()
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
            self.manager.followed_path(self.visited_nodes[-1], next_node_index)
            self.visited_nodes.append(next_node_index)
            self.manager.draw_next_node(self, next_node_index)
            next_node = self.manager.environment.nodes[next_node_index]
            self.x = next_node.x
            self.y = next_node.y

    def find_next_node(self):
        desirabilities = []
        available_nodes = []

        for index, node in enumerate(self.manager.environment.nodes):
            if index not in self.visited_nodes:
                available_nodes.append(index)
                desirabilities.append(self.desirability(index, node))

        # Normalize desirabilities to sum to 1
        total_desirability = sum(desirabilities)
        normalized_desirabilities = [desirability / total_desirability for desirability in desirabilities]

        self.draw_option_nodes(available_nodes, normalized_desirabilities)

        # Select the next node based on randomness of the desirabilities
        next_node_index = random.choices(available_nodes, normalized_desirabilities)[0]

        return next_node_index

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

    def polygon_distance(self) -> float:
        total_distance = 0
        for i in range(Settings.NUM_NODES):
            current_node = self.manager.environment.nodes[self.visited_nodes[i]]
            next_node = self.manager.environment.nodes[
                self.visited_nodes[(i + 1) % Settings.NUM_NODES]]  # Wraps around to the first node after the last node
            total_distance += current_node.distance_to(next_node)
        return total_distance
