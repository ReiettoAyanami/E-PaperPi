from abc import ABC, abstractmethod
class Gettable(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def get(self):
        pass