from PIL import ImageDraw
from PIL import Image as PILImage


class Image:
    def __init__(self,image, image_path = ''):
        self._image_path: str = image_path
        self._image = PILImage.open(image_path)
        self._local_painter: ImageDraw = ImageDraw.Draw(self._image)

    def __get_local_painter_ref(self) -> ImageDraw:
        return self._local_painter

    @property
    def local_painter_reference(self) -> callable:
        return self.__get_local_painter_ref

    @property
    def image(self) -> PILImage:
        return self._image

    # Wrapper for PILImage attributes
    @property
    def format(self):
        return self._image.format

    @property
    def mode(self):
        return self._image.mode

    @property
    def size(self):
        return self._image.size

    @property
    def width(self):
        return self._image.width

    @property
    def height(self):
        return self._image.height

    @property
    def info(self):
        return self._image.info

    @property
    def palette(self):
        return self._image.palette

    # Wrapper for PILImage methods
    def convert(self, mode, **kwargs):
        self._image.convert(mode, **kwargs)

    def copy(self):
        self._image = self._image.copy()

    def crop(self, box):
        self._image = self._image.crop(box)

    def filter(self, filter):
        self._image.filter(filter)

    def getpixel(self, xy):
        return self._image.getpixel(xy)

    def putpixel(self, xy, value):
        self._image.putpixel(xy, value)

    def resize(self, size, resample=None, box=None, reducing_gap=None):
        self._image = self._image.resize(size, resample=resample, box=box, reducing_gap=reducing_gap)

    def rotate(self, angle, resample=0, expand=0, center=None, translate=None, fillcolor=None):
        self._image = self._image.rotate(angle, resample=resample, expand=expand, center=center, translate=translate, fillcolor=fillcolor)

    def save(self, fp, format=None, **params):
        self._image.save(fp, format=format, **params)

    def show(self, title=None):
        self._image.show(title=title)

    def thumbnail(self, size, resample=3, reducing_gap=None):
        self._image.thumbnail(size, resample=resample, reducing_gap=reducing_gap)

    def transpose(self, method):
        self._image = self._image.transpose(method)

    def close(self):
        self._image.close()

    def seek(self, frame):
        self._image.seek(frame)

    def tell(self):
        self._image = self._image.tell()

    def paste(self, im, box=None, mask=None):
        self._image.paste(im, box, mask)

    def paste_self(self, target, box=None, mask=None):
        target.paste(self._image, box, mask)

    def split(self):
        return self._image.split()

    def tobytes(self, encoder_name="raw", *args):
        return self._image.tobytes(encoder_name, *args)

    def tobitmap(self, name="image"):
        return self._image.tobitmap(name)

    def transform(self, size, method, data=None, resample=0, fill=1, fillcolor=None):
        return self._image.transform(size, method, data, resample, fill, fillcolor)

    def verify(self):
        self._image.verify()

    def load(self):
        return self._image.load()

    def point(self, lut, mode=None):
        return self._image.point(lut, mode)

    def quantize(self, colors=256, method=None, kmeans=0, palette=None, dither=None):
        return self._image.quantize(colors, method, kmeans, palette, dither)

    def reduce(self, factor, box=None):
        return self._image.reduce(factor, box)

    def getbands(self):
        return self._image.getbands()

    def getbbox(self):
        return self._image.getbbox()

    def getchannel(self, channel):
        return self._image.getchannel(channel)

    def entropy(self):
        return self._image.entropy()


