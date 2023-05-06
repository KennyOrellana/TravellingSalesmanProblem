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
        for ant in self.ants:
            for node in self.environment.nodes:
                ant.draw_line_to_node(self.canvas.screen, node)
