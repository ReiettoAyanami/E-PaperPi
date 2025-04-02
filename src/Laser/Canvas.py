
from src.Laser.Brush import Brush
from src.Laser.AttributeReference import AttributeReference
from PIL.Image import Image as PILImage
from src.Laser.Gettable import Gettable
from src.Laser.Settable import Settable

"""
TODO:
    Painter paints with the brush on the canvas.


    Canvas contiene la Pil.Image
    Brush contiene ImageDraw
    Painter (Image e Text per esempio) chiamerá le funzioni di Brush e quindi conterrá brush

"""

class Canvas(Gettable, Settable):
    def __init__(self, width: int = 0, height: int = 0, mode:str = '1'):
        self._canvas:PILImage = PILImage.new(mode, (height, width), 255)
        self._canvas_reference:AttributeReference = AttributeReference(self.get)
        self._brush:Brush = Brush(self._canvas_reference)
        self._brush_reference:AttributeReference = AttributeReference(self._brush.get)
        self.width = width
        self.height = height
        self.mode = mode

    def __reset_brush(self):
        self._brush = Brush(self._canvas_reference)
        self._brush_reference = AttributeReference(self._brush.get)
    def __reset_canvas(self):
        #only resets the canvas
        self._canvas = PILImage.new(self.mode, (self.height, self.width), 255)
        self._canvas_reference = AttributeReference(self.get)
        

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
        self._canvas_reference = AttributeReference(self.get)
        self.__reset_brush()

    @property
    def height(self) -> int:
        return self._canvas.height
    
    @height.setter
    def height(self, height: int):
        self._canvas = PILImage.new('1', (height, self.width), 255)
        self._canvas_reference = AttributeReference(self.get)
        self.__reset_brush()

    @property
    def mode(self) -> str:
        return self._canvas.mode
    
    @mode.setter
    def mode(self, mode: str):
        self._canvas = PILImage.new(mode, (self.height, self.width), 255)
        self._canvas_reference = AttributeReference(self.get)
        self.__reset_brush()
    
