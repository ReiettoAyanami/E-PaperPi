from abc import ABC, abstractmethod
from Settable import Settable
from Gettable import Gettable
from Brush import Brush

class Painter(ABC):

    def __init__(self, brush:callable):
        self.__brush:Brush = Brush

    @abstractmethod
    def paint(self, **kwargs):
        pass
    
    @property
    def brush(self) -> Brush:
        return self.__brush
    