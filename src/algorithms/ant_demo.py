from src.algorithms.ant import Ant
from src.environment.settings import Settings


# Use diferent color for each ant
class AntDemo(Ant):
    def __init__(self, manager):
        super().__init__(manager)

    def tick(self):
        self.draw_current_path()

        if len(self.visited_nodes) == self.manager.environment.total_nodes:
            self.compute_distance()
            self.manager.ant_finished(self)
        elif self.next_node_index is None:
            self.next_node_index = self.find_next_node()
        else:
            self.find_next_node()  # Only to redraw the option lines
            self.manager.draw_next_node(self, self.next_node_index)
            self.move_to_next_node()

    def next_node_option(self, available_nodes, normalized_desirabilities):
        for index, node in enumerate(self.manager.environment.nodes):
            if index in available_nodes:
                position = available_nodes.index(index)
                self.draw_line_to_node(
                    self.manager.canvas.screen,
                    node,
                    line_thickness=int(
                        round(Settings.NODE_OPTIONS_THICKNESS * normalized_desirabilities[position])),
                )
