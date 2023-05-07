from abc import ABC, abstractmethod


# Probably must be renamed
class Simulation(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def tick(self):
        pass
