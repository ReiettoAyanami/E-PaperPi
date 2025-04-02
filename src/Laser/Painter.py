from abc import ABC, abstractmethod
from src.Laser.Settable import Settable
from src.Laser.Gettable import Gettable

class Painter(ABC, Settable, Gettable):

    def __init__(self):
        pass

    @abstractmethod
    def paint(self):
        pass
    