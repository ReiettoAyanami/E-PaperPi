from PIL import ImageDraw
from PIL import Image as PILImage
from Painter import Painter
from Canvas import Canvas
from Brush import Brush
from Gettable import Gettable
from Settable import Settable

# TODO reworka perché Canvas é giá un Wrappper di PILImage, questo serve come interfaccia per IMageDraw
class IO_Image(Painter, Gettable, Settable):
    def __init__(self,brush:callable, image_path:str = None):
        super().__init__(brush)
        self.__image:PILImage = PILImage.open(image_path) if image_path is not None else PILImage.new('1', (0, 0), 255)
        self.__image_path:str = image_path
    
    def paint(self, **kwargs):
        super().paint(**kwargs)
        self.__brush().bitmap((kwargs['x'], kwargs['y']), self.__brush().canvas_reference(), fill=255)

    def get(self) -> PILImage:
        return self.__image
    
    def set(self, image_path:str):
        self.__image = PILImage.open(image_path)
        self.__image_path = None
    
    @property
    def image_path(self) -> PILImage:
        return self.__image_path

    

        

