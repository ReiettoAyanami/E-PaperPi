from PIL import ImageDraw
from src.Laser.Gettable import Gettable
from src.Laser.Settable import Settable
from ..Laser.AttributeReference import AttributeReference

class Brush(Gettable, Settable):

    def __init__(self, canvas_reference: AttributeReference):
        self._brush:ImageDraw = ImageDraw.Draw(canvas_reference.get())

    def get(self) -> ImageDraw:
        return self._brush
    
    def set(self, brush: ImageDraw):
        self._brush = brush
