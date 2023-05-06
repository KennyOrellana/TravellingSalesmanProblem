class Manager:
    def __init__(self, canvas, nodes):
        self.canvas = canvas
        self.nodes = nodes

    def draw_nodes(self):
        for node in self.nodes:
            node.draw(self.canvas.screen)
