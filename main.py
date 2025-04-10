from src.include.waveshare_epd.epd4in2_V2 import *
from src.Laser.Display import *
from PIL import Image as PILImage,ImageDraw,ImageFont
from src.Laser.Text import Text
from src.Laser.shapes import Rectangle, Circle, Line
from src.Laser.FileImage import FileImage


def main():
    # Initialize display
    roboto24 = ImageFont.truetype(font='./roboto.ttf',size=24)

    display = Display(display_driver=EPD(), default_font=roboto24, orientation=DisplayVertical)
    display.start(mode='standard')
    
    # Create and render text
    text_layer = Text(display=display,
                     position=(10, 10),
                     text="Hello, E-Paper!",
                     font=roboto24)
    bbox = text_layer.bbox
    text_layer.render()
    print(f"Bounding box: {bbox}")
    
    # Create and render rectangle around text
    rect = Rectangle(display=display,
                    rect=bbox,
                    outline=display.BLACK,
                    outline_width=2)
    rect.render()
    
    # Render the display
    display.render()
    
    # Switch to grayscale mode
    display.current_mode = 'grayscale'
    
    # Create and render a rectangle in grayscale
    rect = Rectangle(display=display,
                    rect=((display.width//2, display.height//2),
                          (display.width - 1, display.height - 1)),
                    outline=display.GRAYS[2],
                    outline_width=2)
    rect.render()
    
    # Update text properties and render
    text_layer.fill = display.GRAYS[2]
    text_layer.position = (20, 20)
    text_layer.render()
    print("Ma qui ci arrivo?")
    
    # Create and render an image
    image_layer = FileImage(display=display,image_path='./test.png', position=(0,0))
    image_layer.image.save('./Output0Image.png')
    image_layer.convert('L')
    image_layer.image.save('./Output1Image.png')
    image_layer.resize((display.width // 2, display.height // 2), Image.LANCZOS)
    image_layer.image.save('./Output2Image.png')
    image_layer.render()  # Render the image using the new render method
    display.base_layer.save('./output_aaa.png')
    
    # Render the final display
    display.render()

if __name__ == "__main__":
    main()
    epdconfig.module_exit(cleanup=True)
    exit()