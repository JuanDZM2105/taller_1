from abc import ABC, abstractmethod

class IStatisticsService(ABC):

    @abstractmethod
    def generate_statistics(self):
        pass