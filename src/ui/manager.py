import pygame

from src.environment.settings import Settings


class Manager:
    # Probably manager don't nee to know about ants
    def __init__(self, canvas, environment):
        self.canvas = canvas
        self.environment = environment
        self.best_ant = None

    def draw_nodes(self):
        for node in self.environment.nodes:
            node.draw(self.canvas.screen)

    def draw_ants(self, ant):
        # for ant in self.ants:
        ant.draw(self.canvas.screen, Settings.CURRENT_NODE_COLOR)

    def ant_finished(self, ant):
        if self.best_ant is None or ant.total_distance < self.best_ant.total_distance:
            self.best_ant = ant
            print("New best ant: ", self.best_ant.total_distance)

        print("Best ant: ", self.best_ant.total_distance, "Ant finished: ", ant.total_distance)

    def tick(self):
        if self.best_ant is not None:
            self.draw_nodes()
            self.best_ant.draw_current_path(Settings.TEXT_COLOR)

    def draw_next_node(self, ant, next_node_index):
        ant.draw_line_to_node(self.canvas.screen, self.environment.nodes[next_node_index],
                              Settings.SELECTED_NODE_COLOR, Settings.LINE_THICKNESS)

    def draw_summary(self, total_ants):
        font = pygame.font.Font(None, 36)
        total_ants_text = f"Total ants: {total_ants:,}"
        if self.best_ant:
            formatted_distance = format(self.best_ant.total_distance, ',.2f')
            shortest_distance_text = f"Shortest distance: {formatted_distance}"
        else:
            shortest_distance_text = "Shortest distance: N/A"

        total_ants_surface = font.render(total_ants_text, True, Settings.TEXT_COLOR)
        shortest_distance_surface = font.render(shortest_distance_text, True, Settings.TEXT_COLOR)

        self.canvas.screen.blit(total_ants_surface, (10, 10))
        self.canvas.screen.blit(shortest_distance_surface, (10, 50))

    def add_iteration(self):
        pass
