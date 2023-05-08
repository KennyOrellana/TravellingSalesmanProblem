import pygame

from src.environment.settings import Settings


class Drawer:
    def __init__(self, canvas, environment):
        self.canvas = canvas
        self.environment = environment

    def draw_nodes(self):
        for node in self.environment.nodes:
            node.draw(self.canvas.screen)

    def draw_path(self, nodes, color=Settings.NODE_COLOR):
        size = len(nodes)
        if size > 1:
            for i in range(len(nodes) - 1):
                self.environment.nodes[nodes[i]].draw_line_to_node(
                    self.canvas.screen,
                    self.environment.nodes[nodes[i + 1]],
                    color, Settings.LINE_THICKNESS
                )

        if size == self.environment.total_nodes:
            self.environment.nodes[nodes[-1]].draw_line_to_node(
                self.canvas.screen,
                self.environment.nodes[nodes[0]],
                color, Settings.LINE_THICKNESS
            )

    def draw_summary(self, total_ants):
        font = pygame.font.Font(None, 36)
        total_ants_text = f"Total ants: {total_ants:,}"

        if self.environment.shortest_path_size:
            formatted_distance = format(self.environment.shortest_path_size, ',.2f')
            shortest_distance_text = f"Shortest distance: {formatted_distance} kms"
        else:
            shortest_distance_text = "Shortest distance: N/A"

        total_ants_surface = font.render(total_ants_text, True, Settings.TEXT_COLOR)
        shortest_distance_surface = font.render(shortest_distance_text, True, Settings.TEXT_COLOR)

        self.canvas.screen.blit(total_ants_surface, (10, 10))
        self.canvas.screen.blit(shortest_distance_surface, (10, 50))
