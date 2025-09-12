# -*- coding: utf-8 -*-
from enum import Enum

class LineStyle:
    SOLID = 0
    DASH = 1
    DOT = 2
    DASHDOT = 3
    DASHDOTDOT = 4


LineStyles: list[str] = ["solid", "dash", "dot", "dashdot", "dashdotdot"]
LineStyleEnums: list[int] = [0, 1, 2, 3, 4]


def str2LineStyle(s: str) -> int:
    """ Convert string to LineStyle enum.
    """
    if s not in LineStyles:
        return LineStyle.SOLID
    return LineStyleEnums[LineStyles.index(s)]


LineArrowStyles: list[str] = ['none', 'from', 'to', 'both']
LineArrowStyleEnums: list[int] = [0, 1, 2, 3]


def str2LineArrowStyle(s: str) -> int:
    """ Return enum value of LineArrowStyle.
    """
    if s not in LineArrowStyles:
        s = "none"
    return LineArrowStyleEnums[LineArrowStyles.index(s)]


class RotationStep(Enum):
    # zero degree
    D0 = 0
    # 90 degree
    D90 = 1
    # 180 degree
    D180 = 2
    # -90 degree
    D_90 = 3


class TraceType:
    NONE = 0
    LINE = 1
    STEP = 2
    ERROR_BARS = 3
    LINE_ERROR_BARS = 4
    BARS = 5


TraceTypes: list[str] = ["none", "line", "step", "errorbars", "line_errorbars", "bars"]
TraceTypesEnum: list[int] = [0, 1, 2, 3, 4, 5]


def str2TraceType(s: str) -> int:
    """ Return enum value of TraceType
    """
    if s not in TraceTypes:
        s = "step"
    return TraceTypesEnum[TraceTypes.index(s)]


class ResizeBehaviour:
    # for LinkingContainer (BOY)
    RESIZE_OPI_TO_FIT_CONTAINER = 0  # Size *.opi to fit the container
    RESIZE_CONTAINER_TO_FIT_OPI = 1  # Size the container to fit *.opi
    CROP = 2  # Don't resize anything, crop if *.opi too large
    SCROLL = 3  # Don't resize anything, add scrollbars if *.opi too large


class ResizeBehaviour_Embeded:
    # for embedded display (Phoebus)
    NO_RESIZE = 0  # no resize, add scroll if needed
    RESIZE_OPI_TO_FIT_CONTAINER = 1  # Size content to fit widget
    RESIZE_CONTAINER_TO_FIT_OPI = 2  # Size widget to match content
    STRETCH_OPI_TO_FIT_CONTAINER = 3  # Stretch content to fit widget
    CROP = 4  # Crop content


ResizeBehaviour_MAP = {
    ResizeBehaviour.RESIZE_OPI_TO_FIT_CONTAINER:
    ResizeBehaviour_Embeded.RESIZE_OPI_TO_FIT_CONTAINER,
    ResizeBehaviour.RESIZE_CONTAINER_TO_FIT_OPI:
    ResizeBehaviour_Embeded.RESIZE_CONTAINER_TO_FIT_OPI,
    ResizeBehaviour.CROP: ResizeBehaviour_Embeded.CROP,
    ResizeBehaviour.SCROLL: ResizeBehaviour_Embeded.NO_RESIZE,
}


class FormatType:
    DEFAULT = 0
    DECIMAL = 1
    EXPONENTIAL = 2
    HEX_32 = 3
    STRING = 4
    HEX_64 = 5
    COMPACT = 6
    ENGINEERING = 7
    SEXAGESIMAL = 8
    SEXAGESIMAL_HMS = 9
    SEXAGESIMAL_DMS = 10


class FormatType_PHOEBUS:
    DEFAULT = 0
    DECIMAL = 1
    EXPONENTIAL = 2
    ENGINEERING = 3
    HEXADECIMAL = 4
    COMPACT = 5
    STRING = 6
    SEXAGESIMAL = 7
    SEXAGESIMAL_HMS = 8
    SEXAGESIMAL_DMS = 9


# for phoebus (BOY to BOB)
FormatType_MAP = {
    FormatType.DEFAULT: FormatType_PHOEBUS.DEFAULT,
    FormatType.DECIMAL: FormatType_PHOEBUS.DECIMAL,
    FormatType.EXPONENTIAL: FormatType_PHOEBUS.EXPONENTIAL,
    FormatType.HEX_32: FormatType_PHOEBUS.HEXADECIMAL,
    FormatType.STRING: FormatType_PHOEBUS.STRING,
    FormatType.HEX_64: FormatType_PHOEBUS.HEXADECIMAL,
    FormatType.COMPACT: FormatType_PHOEBUS.COMPACT,
    FormatType.ENGINEERING: FormatType_PHOEBUS.ENGINEERING,
    FormatType.SEXAGESIMAL: FormatType_PHOEBUS.SEXAGESIMAL,
    FormatType.SEXAGESIMAL_HMS: FormatType_PHOEBUS.SEXAGESIMAL_HMS,
    FormatType.SEXAGESIMAL_DMS: FormatType_PHOEBUS.SEXAGESIMAL_DMS,
}


class BasicStyle:
    # ActionButton, TextEntry
    CLASSIC = 0
    NATIVE = 1


class HAlign:
    """Enum describing horizontal alignment

    This is typically used with the horizontal_alignment property.
    """
    LEFT = 0
    CENTER = 1
    RIGHT = 2


class VAlign:
    """Enum describing vertical alignment

    This is typically used with the vertical_alignment property.
    """
    TOP = 0
    MIDDLE = 1
    BOTTOM = 2


HA_RIGHT = HAlign.RIGHT
HA_CENTER = HAlign.CENTER
HA_LEFT = HAlign.LEFT
VA_TOP = VAlign.TOP
VA_MIDDLE = VAlign.MIDDLE
VA_BOTTOM = VAlign.BOTTOM


class PointType:
    NONE = 0
    SQUARE = 1
    CIRCLE = 2
    DIAMOND = 3
    X = 4
    TRIANGLE = 5

PointTypes: list[str] = ["none", "square", "sq", "circle", "o", "diamond", "d", "x", "triangle", "t"]
PointTypesEnum: list[int] = [0, 1, 1, 2, 2, 3, 3, 4, 5, 5]


def str2PointType(s: str) -> int:
    """ Return enum of PointType from a string.
    """
    if s not in PointTypes:
        s = "square"
    return PointTypesEnum[PointTypes.index(s)]


class GroupBoxBorderStyle:
    # group box border style for phoebus
    GROUP_BOX = 0
    TITLE_BAR = 1
    LINE = 2
    NONE = 3


# phoebus does not support border style.
class BorderStyle:
    NONE = 0
    LINE = 1
    RAISED = 2
    LOWERED = 3
    ETCHED = 4
    RIDGED = 5
    BUTTON_RAISED = 6
    BUTTON_PRESSED = 7
    DOT = 8
    DASH = 9
    DASH_DOT = 10
    DASH_DOT_DOT = 11
    TITLE_BAR = 12
    GROUP_BOX = 13
    ROUND_RECTANGLE_BACKGROUND = 14
    EMPTY = 15


# only for phoebus group widget
BorderStyle_GroupBoxStyle_MAP = {
    BorderStyle.GROUP_BOX: GroupBoxBorderStyle.GROUP_BOX,
    BorderStyle.TITLE_BAR: GroupBoxBorderStyle.TITLE_BAR,
    BorderStyle.LINE: GroupBoxBorderStyle.LINE,
    BorderStyle.NONE: GroupBoxBorderStyle.NONE
}