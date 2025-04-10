from PIL import ImageDraw
from src.Laser.Display import Display

class Text:
    def __init__(self, display, position, text, fill=None, font=None, anchor=None, spacing=4, align='left', direction=None, features=None, language=None, 
                stroke_width=0, stroke_fill=None, embedded_color=False, font_size=None):
        self._display = display
        self._position = position
        self._text = text
        self._fill = fill
        self._font = font
        self._anchor = anchor
        self._spacing = spacing
        self._align = align
        self._direction = direction
        self._features= features
        self._language = language
        self._stroke_width = stroke_width
        self._stroke_fill = stroke_fill
        self._embedded_color = embedded_color
        self._font_size=font_size

    def render(self):
        self._display.painter.text(
            xy=self._position,
            text=self._text,
            fill=self._fill,
            font=self._font,
            anchor=self._anchor,
            spacing=self._spacing,
            align=self._align,
            direction=self._direction,
            features=self._features,
            language=self._language,
            stroke_width=self._stroke_width,
            stroke_fill=self._stroke_fill,
            embedded_color=self._embedded_color
        )

    def render_multiline(self):
        self._display.painter.multiline_text(
            xy=self._position,
            text=self._text,
            fill=self._fill,
            font=self._font,
            anchor=self._anchor,
            spacing=self._spacing,
            align=self._align,
            direction=self._direction,
            features=self._features,
            language=self._language,
            stroke_width=self._stroke_width,
            stroke_fill=self._stroke_fill,
            embedded_color=self._embedded_color
        )

    @property
    def bbox(self):
        return self._display.painter.textbbox(
            xy=self._position, 
            text=self._text, 
            font=self._font, 
            anchor=self._anchor, 
            spacing=self._spacing, 
            align=self._align, 
            direction=self._direction, 
            features=self._features, 
            language=self._language, 
            stroke_width=self._stroke_width, 
            embedded_color=self._embedded_color, 
            font_size=self._font_size
        )

    @property
    def bbox_multiline(self):
        return self._display.painter.multiline_textbbox(
            xy=self._position, 
            text=self._text, 
            font=self._font, 
            anchor=self._anchor, 
            spacing=self._spacing, 
            align=self._align, 
            direction=self._direction, 
            features=self._features, 
            language=self._language, 
            stroke_width=self._stroke_width, 
            embedded_color=self._embedded_color, 
            font_size=self._font_size
        )

    @property
    def textlength(self):
        return self._display.painter.textlength(
            text=self._text, 
            font=self._font, 
            direction=self._direction, 
            features=self._features, 
            language=self._language, 
            embedded_color=self._embedded_color, 
            font_size=self._font_size
        )

    @property
    def painter(self):
        return self._display.painter

    @painter.setter
    def painter(self, value):
        self._display.painter = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def fill(self):
        return self._fill

    @fill.setter
    def fill(self, value):
        self._fill = value

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        self._font = value

    @property
    def anchor(self):
        return self._anchor

    @anchor.setter
    def anchor(self, value):
        self._anchor = value

    @property
    def spacing(self):
        return self._spacing

    @spacing.setter
    def spacing(self, value):
        self._spacing = value

    @property
    def align(self):
        return self._align

    @align.setter
    def align(self, value):
        self._align = value

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value

    @property
    def features(self):
        return self._features

    @features.setter
    def features(self, value):
        self._features = value

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value

    @property
    def stroke_width(self):
        return self._stroke_width

    @stroke_width.setter
    def stroke_width(self, value):
        self._stroke_width = value

    @property
    def stroke_fill(self):
        return self._stroke_fill

    @stroke_fill.setter
    def stroke_fill(self, value):
        self._stroke_fill = value

    @property
    def embedded_color(self):
        return self._embedded_color

    @embedded_color.setter
    def embedded_color(self, value):
        self._embedded_color = value

    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, value):
        self._font_size = value


