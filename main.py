from include.waveshare_epd.epd4in2_V2 import *
from src.Laser.Display import *
from PIL import Image as PILImage,ImageDraw,ImageFont
from src.Laser.Image import Image as LaserImage
from src.Laser.Text import Text
from include.waveshare_epd.epd4in2_V2 import *

def main():
    # Inizializza il display
    roboto24 =  ImageFont.truetype(font='./roboto.ttf',size=24)

    display = Display(display_driver=EPD(), default_font=roboto24, orientation=DisplayVertical)
    display.start(mode='standard')

    # Renderizza il contenuto sul display
    display.stop()

if __name__ == "__main__":
    main()
    epdconfig.module_exit(cleanup=True)
    exit()