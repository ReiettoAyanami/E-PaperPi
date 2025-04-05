
from Brush import Brush
from PIL.Image import Image as PILImage
from Gettable import Gettable
from Settable import Settable

class Canvas(Gettable, Settable):
    def __init__(self, width: int = 0, height: int = 0, mode:str = '1'):
        self._canvas:PILImage = PILImage.new(mode, (height, width), 255)
        self._brush:Brush = Brush(self._canvas_reference)
        self.width = width
        self.height = height
        self.mode = mode

    def reset_brush(self):
        self._brush = Brush(self._canvas_reference)
    def reset(self, mode:str = '1', dimensions:tuple[int, int] = (0, 0), color:int = 255):
        self._canvas = PILImage.new(mode, dimensions, color)

    def get(self) -> PILImage:
        return self._canvas
    
    def set(self, canvas: PILImage):
        self._canvas = canvas
    
    @property
    def brush(self) -> Brush:
        return self._brush
    
    @property
    def width(self) -> int:
        return self._canvas.width
    
    @width.setter
    def width(self, width: int):
        self._canvas = PILImage.new('1', (self.height, width), 255)
        self.__reset_brush()

    @property
    def height(self) -> int:
        return self._canvas.height
    
    @height.setter
    def height(self, height: int):
        self._canvas = PILImage.new('1', (height, self.width), 255)
        self.__reset_brush()

    @property
    def mode(self) -> str:
        return self._canvas.mode
    
    @mode.setter
    def mode(self, mode: str):
        self._canvas.convert(mode)
        self.__reset_brush()
    
