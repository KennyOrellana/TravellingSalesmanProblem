from abc import ABC, abstractmethod


# Probably must be renamed
class Simulation(ABC):
    @abstractmethod
    def start(self, canvas, environment, manager):
        pass

    @abstractmethod
    def tick(self):
        pass
