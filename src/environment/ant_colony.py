from src.algorithms.ant import Ant
from src.algorithms.ant_demo import AntDemo
from src.environment.settings import Settings
from src.ui.manager import Manager


class AntColony(Manager):
    def __init__(self, canvas, environment, demo=False):
        super().__init__(canvas, environment)
        self.demo = demo
        self.matrix = AntColony.create_pheromone_matrix(Settings.NUM_NODES)
        if demo:
            self.ants = self.create_ants(1)
        else:
            self.ants = self.create_ants(Settings.INITIAL_ANTS)  # Create n instances of Ant
        self.total_ants = len(self.ants)

    @staticmethod
    def create_pheromone_matrix(n, initial_value=Settings.PHEROMONE_INITIAL):
        matrix = [[initial_value for _ in range(n)] for _ in range(n)]
        return matrix

    def followed_path(self, i, j):
        self.matrix[i][j] += Settings.PHEROMONE_INTENSITY

    def get_pheromone_value(self, node1, node2):
        return self.matrix[node1][node2]

    def tick(self):
        for index, ant in reversed(list(enumerate(self.ants))):
            if ant.total_distance > 0:
                self.ants.pop(index)
            else:
                ant.tick()

        self.dissipate_pheromone()

    def dissipate_pheromone(self, evaporation_rate=Settings.PHEROMONE_EVAPORATION):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] *= (1 - evaporation_rate)
                self.matrix[j][i] *= (1 - evaporation_rate)
                if self.matrix[i][j] < 1:
                    self.matrix[i][j] = 1
                if self.matrix[j][i] < 1:
                    self.matrix[j][i] = 1

    def create_ants(self, n):  # Create n instances of Ant
        if not self.demo:
            return [Ant(self) for _ in range(n)]
        else:
            return [AntDemo(self) for _ in range(n)]

    def add_iteration(self):
        self.total_ants += 1
        self.ants.extend(self.create_ants(1))
