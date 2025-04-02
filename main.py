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
    text_layer = Text(painter_reference=display.painter_reference,text="Hello, E-Paper!", position=(10, 10), font=roboto24)
    bbox = text_layer.bbox
    text_layer.render()
    print(f"Bounding box: {bbox}")
    display.draw_rectangle(rect=bbox,outline_color=display.BLACK, outline_width=2, color=None)
    # # cambia la modalitá di rendering e disegna un rettangolo
    display.render()
    display.current_mode = 'grayscale'
    display.draw_rectangle(rect=((display.width//2,display.height//2),(display.width - 1,display.height - 1)), outline_color=display.GRAYS[2], outline_width=2, color=None)
    text_layer.fill = display.GRAYS[2]
    text_layer.position = (20, 20)
    text_layer.render()
    print("Ma qui ci arrivo?")
    
    # Crea un'immagine con Laser.Image e mettila a schermo
    image_layer = LaserImage(image_path='./output_copy.png')
    image_layer.resize((display.width // 2, display.height // 2 ), Image.LANCZOS)
    image_layer.convert('L')
    #image_layer.paste_self(target=display.base_layer)
    display.base_layer.save('./output_aaa.png')
    # Renderizza il contenuto sul display
    display.render()

if __name__ == "__main__":
    main()
    epdconfig.module_exit(cleanup=True)
    exit()