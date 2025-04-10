from src.include.waveshare_epd.epd4in2_V2 import *
from PIL import Image as PILImage,ImageDraw,ImageFont, ImageOps

FastRefresh1_5s:int = 0
FastRefresh1s:int = 1
DisplayHorizontal:int = 0
DisplayVertical:int = 1

class Display:
    def __init__(self, display_driver:EPD = None, default_font:ImageFont=None, orientation:int=DisplayHorizontal):
        self.init_modes = ('standard', 'grayscale', 'fast')
        self.GRAYS:list[int] = [display_driver.GRAY1, display_driver.GRAY2, display_driver.GRAY3, display_driver.GRAY4]
        self.WHITE:int = display_driver.GRAY1
        self.BLACK:int = display_driver.GRAY4
        self.__display_driver = display_driver
        self.__base_layer:Image= None
        self.__painter:ImageDraw = None
        self.orientation = orientation
        self.width = self.__display_driver.width if self.orientation == DisplayHorizontal else self.__display_driver.height
        self.height = self.__display_driver.height if self.orientation == DisplayHorizontal else self.__display_driver.width
        self.font:ImageFont = default_font
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
        self.reset_base_layer()


    def clear_display(self):
        self.__display_driver.init()
        self.__display_driver.Clear()
    
    def render(self, partial:bool=False):
        if(partial):
            self.__display_driver.display_Partial(self.__display_driver.getbuffer(self.__base_layer))
        elif self.__current_mode == 'grayscale':
            if self.orientation == DisplayHorizontal:
                self.__display_driver.display_4Gray(self.__display_driver.getbuffer_4Gray(self.__base_layer))
            elif self.orientation == DisplayVertical:
                self.__display_driver.display_4Gray(self.__display_driver.getbuffer_4Gray(ImageOps.mirror(self.__base_layer)))
                
        elif self.__current_mode == 'fast':
            self.__display_driver.display_Fast(self.__display_driver.getbuffer(self.__base_layer))
        else:
            self.__display_driver.display(self.__display_driver.getbuffer(self.__base_layer))

    def reset_base_layer(self):
        if(self.__current_mode != 'grayscale'):
            self.__base_layer = PILImage.new('1', (self.width, self.height), 255)
        else:
            self.__base_layer = PILImage.new('L', (self.width, self.height), 255)     
        self.__painter = ImageDraw.Draw(self.__base_layer)   

    def stop(self):
        self.__display_driver.Clear()
        self.__display_driver.sleep()
    
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
            self.__base_layer = self.__base_layer.convert('L')
            self.__painter = ImageDraw.Draw(self.__base_layer)
        elif mode == 'fast':
            self.__display_driver.init_fast()
            self.__base_layer = self.__base_layer.convert('1')
            self.__painter = ImageDraw.Draw(self.__base_layer)
        else:
            self.__display_driver.init()
            self.__base_layer = self.__base_layer.convert('1')
            self.__painter = ImageDraw.Draw(self.__base_layer)
    
    @property
    def base_layer(self):
        return self.__base_layer

    @property
    def painter(self):
        return self.__painter

    
        
        
        
