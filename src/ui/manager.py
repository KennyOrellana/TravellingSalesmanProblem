from src.environment.settings import Settings


class Manager:
    def __init__(self, canvas, environment):
        self.canvas = canvas
        self.environment = environment
        self.ants = []

    def draw_nodes(self):
        for node in self.environment.nodes:
            node.draw(self.canvas.screen)

    def draw_ants(self):
        for ant in self.ants:
            ant.draw(self.canvas.screen)

    def add_ant(self, ant):
        self.ants.append(ant)
        self.draw_ants()

    def tick(self):
        print("TODO: tick manager")

    def draw_option_nodes(self, available_nodes):
        for ant in self.ants:
            for index, node in enumerate(self.environment.nodes):
                if index in available_nodes:
                    ant.draw_line_to_node(self.canvas.screen, node)

    def draw_next_node(self, next_node_index):
        self.ants[0].draw_line_to_node(self.canvas.screen, self.environment.nodes[next_node_index],
                                       Settings.NEXT_NODE_COLOR, Settings.NEXT_NODE_THICKNESS)
