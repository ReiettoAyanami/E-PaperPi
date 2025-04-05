
from PIL import Image as PILImage,ImageDraw,ImageFont, ImageOps
from Canvas import Canvas
from include.waveshare_epd.epd4in2_V2 import EPD
FastRefresh1_5s:int = 0
FastRefresh1s:int = 1
DisplayHorizontal:int = 0
DisplayVertical:int = 1
class Display:
    def __init__(self, display_driver:EPD ,canvas:Canvas = None, orientation:int=DisplayHorizontal):
        self.init_modes = ('standard', 'grayscale', 'fast')
        self.GRAYS:list[int] = [display_driver.GRAY1, display_driver.GRAY2, display_driver.GRAY3, display_driver.GRAY4]
        self.WHITE:int = display_driver.GRAY1
        self.BLACK:int = display_driver.GRAY4
        self.__display_driver = display_driver
        self.__canvas:Canvas = canvas if canvas is not None else Canvas(width=display_driver.width, height=display_driver.height, mode= '1')
        self.__canvas.width = display_driver.width
        self.__canvas.height = display_driver.height
        self.orientation = orientation
        self.width = self.__display_driver.width if self.orientation == DisplayHorizontal else self.__display_driver.height
        self.height = self.__display_driver.height if self.orientation == DisplayHorizontal else self.__display_driver.width
        self.__current_mode = 'standard'
        
    def start(self, mode:str = 'standard', fast_start_seconds:int = FastRefresh1_5s):
        self.__display_driver.init()
        self.__display_driver.Clear()
        self.__current_mode = mode
        init_mode = {self.init_modes[0]:self.__display_driver.init,self.init_modes[1]:self.__display_driver.Init_4Gray, self.init_modes[2]:self.__display_driver.init_fast}
        if(mode != 'fast'): 
            init_mode[mode]()
        else:
            init_mode[mode](fast_start_seconds)
        self.reset_canvas()
        
    
    def clear_display(self):
        self.__display_driver.init()
        self.__display_driver.Clear()
    
    def render(self, partial:bool=False):
        if(partial):
            self.__display_driver.display_Partial(self.__display_driver.getbuffer(self.__canvas.get()))
        elif self.__current_mode == 'grayscale':
            if self.orientation == DisplayHorizontal:
                self.__display_driver.display_4Gray(self.__display_driver.getbuffer_4Gray(self.__canvas.get()))
            elif self.orientation == DisplayVertical:
                self.__display_driver.display_4Gray(self.__display_driver.getbuffer_4Gray(ImageOps.mirror(self.__canvas.get())))
                
        elif self.__current_mode == 'fast':
            self.__display_driver.display_Fast(self.__display_driver.getbuffer(self.__canvas.get()))
        else:
            self.__display_driver.display(self.__display_driver.getbuffer(self.__canvas.get()))

    def reset_canvas(self):
        if(self.__current_mode != 'grayscale'):
            self.__canvas.reset(mode='1', dimensions=(self.width, self.height), color=255)
        else:    
            self.__canvas.reset(mode='L', dimensions=(self.width, self.height), color=255)

    def stop(self):
        self.__display_driver.Clear()
        self.__display_driver.sleep()
    
    @property
    def display_driver(self):
        return self.__display_driver
    @property
    def base_layer(self):
        return self.__base_layer
    @property
    def canvas(self):
        return self.__canvas
    @property
    def current_mode(self):
        return self.__current_mode
    @property
    def current_mode(self):
        return self.__current_mode
    @current_mode.setter
    def current_mode(self, mode: str):

        if mode not in self.init_modes:
            raise ValueError(f"Invalid mode: {mode}. Valid modes are: {list(self.init_modes)}")
        self.__current_mode = mode

        if mode == 'grayscale':
            self.__display_driver.Init_4Gray()
            self.__canvas.mode = 'L'
        elif mode == 'fast':
            self.__display_driver.init_fast()
            self.__canvas.mode = '1'
        else:
            self.__display_driver.init()
            self.__canvas.mode = '1'


        