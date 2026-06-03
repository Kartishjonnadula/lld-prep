from abc import abstractmethod, ABC


class Sink(ABC):
    @abstractmethod
    def write(self):
        pass
