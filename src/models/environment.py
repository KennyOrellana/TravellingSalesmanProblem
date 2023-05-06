import random

from src.models.node import Node
from src.environment.settings import Settings
from src.ui.canvas import Canvas


class Environment:
    def __init__(self, nodes=None, num_nodes=10):
        if nodes is None:
            (width, height) = Canvas.get_screen_size()
            self.nodes = [
                Node(
                    random.randint(Settings.PADDING, width - Settings.PADDING),
                    random.randint(Settings.PADDING, height - Settings.PADDING),
                )
                for _ in range(num_nodes)
            ]
        else:
            self.nodes = nodes

        self.shortest_path = []
        self.shortest_path_size = None

    def update_shortest_path(self, new_path, new_path_size):
        self.shortest_path = new_path
        self.shortest_path_size = new_path_size

    def __str__(self):
        nodes_str = "\n".join([f"Node {i}: ({node.x}, {node.y})" for i, node in enumerate(self.nodes)])
        return f"Nodes:\n{nodes_str}\nShortest path: {self.shortest_path}\nShortest path size: {self.shortest_path_size}"
