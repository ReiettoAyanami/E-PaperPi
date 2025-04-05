from PIL import ImageDraw
from Gettable import Gettable
from Settable import Settable

class Brush(Gettable, Settable):

    def __init__(self, canvas_reference: callable):
        self._brush:ImageDraw = ImageDraw.Draw(canvas_reference())
        self.__canvas_reference = canvas_reference

    def get(self) -> ImageDraw:
        return self._brush
    
    def set(self, brush: ImageDraw):
        self._brush = brush

    @property
    def canvas_reference(self) -> callable:
        return self.__canvas_reference
