from src.environment.settings import Settings
from src.ui.manager import Manager


class AntColony(Manager):
    def __init__(self, canvas, environment):
        super().__init__(canvas, environment)
        self.matrix = AntColony.create_pheromone_matrix(Settings.NUM_NODES)

    @staticmethod
    def create_pheromone_matrix(n, initial_value=1.0):
        matrix = [[initial_value for _ in range(n)] for _ in range(n)]
        return matrix

    def followed_path(self, i, j):
        self.matrix[i][j] += 1
        self.matrix[j][i] += 1

    def get_pheromone_value(self, node1, node2):
        return self.matrix[node1][node2]

    def tick(self):
        super().tick()
        self.dissipate_pheromone()

    def dissipate_pheromone(self, evaporation_rate=0.5):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] *= (1 - evaporation_rate)
                self.matrix[j][i] = self.matrix[i][j]
                if self.matrix[i][j] < 1:
                    self.matrix[i][j] = 1
                    self.matrix[j][i] = 1
