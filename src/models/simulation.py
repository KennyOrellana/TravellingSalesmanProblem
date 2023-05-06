from abc import ABC, abstractmethod


class Simulation(ABC):
    @abstractmethod
    def start(self, canvas, environment):
        pass

    @abstractmethod
    def tick(self):
        pass
