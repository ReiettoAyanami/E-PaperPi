from PIL import ImageDraw
from src.Laser.Display import Display

class Rectangle:
    def __init__(self, display, rect, outline=None, fill=None, outline_width=1):
        self._display = display
        self._rect = rect
        self._outline = outline
        self._fill = fill
        self._outline_width = outline_width

    def render(self):
        self._display.painter.rectangle(
            self._rect,
            outline=self._outline,
            fill=self._fill,
            width=self._outline_width
        )

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, value):
        self._rect = value

    @property
    def outline(self):
        return self._outline

    @outline.setter
    def outline(self, value):
        self._outline = value

    @property
    def fill(self):
        return self._fill

    @fill.setter
    def fill(self, value):
        self._fill = value

    @property
    def outline_width(self):
        return self._outline_width

    @outline_width.setter
    def outline_width(self, value):
        self._outline_width = value

class Circle:
    def __init__(self, display, center, radius, outline=None, fill=None, outline_width=1):
        self._display = display
        self._center = center
        self._radius = radius
        self._outline = outline
        self._fill = fill
        self._outline_width = outline_width

    def render(self):
        # Calculate bounding box for the circle
        x, y = self._center
        r = self._radius
        bbox = (x - r, y - r, x + r, y + r)
        self._display.painter.ellipse(
            bbox,
            outline=self._outline,
            fill=self._fill,
            width=self._outline_width
        )

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, value):
        self._center = value

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def outline(self):
        return self._outline

    @outline.setter
    def outline(self, value):
        self._outline = value

    @property
    def fill(self):
        return self._fill

    @fill.setter
    def fill(self, value):
        self._fill = value

    @property
    def outline_width(self):
        return self._outline_width

    @outline_width.setter
    def outline_width(self, value):
        self._outline_width = value

class Line:
    def __init__(self, display, start, end, fill=None, width=1):
        self._display = display
        self._start = start
        self._end = end
        self._fill = fill
        self._width = width

    def render(self):
        self._display.painter.line(
            [self._start, self._end],
            fill=self._fill,
            width=self._width
        )

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value

    @property
    def fill(self):
        return self._fill

    @fill.setter
    def fill(self, value):
        self._fill = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value 