import pygame

from src.environment.settings import Settings


class Manager:
    def __init__(self, canvas, environment):
        self.canvas = canvas
        self.environment = environment
        self.best_ant = None

    def ant_finished(self, ant):
        if self.environment.shortest_path_size is None or ant.total_distance < self.environment.shortest_path_size:
            self.environment.update_shortest_path(ant.visited_nodes, ant.total_distance)

    def draw_next_node(self, ant, next_node_index):
        ant.draw_line_to_node(self.canvas.screen, self.environment.nodes[next_node_index],
                              Settings.SELECTED_NODE_COLOR, Settings.LINE_THICKNESS)

    def add_iteration(self):
        pass

    def get_node_at(self, index):
        return self.environment.nodes[index]
