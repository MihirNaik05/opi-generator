from opigen.renderers import Renderer
from opigen.contrib import Display, VerticalLine
from opigen.contrib import HorizontalLine
from opigen.opimodel.widgets import LineStyles
from itertools import cycle


def main():
    screen = Display(name="Lines Widget")

    x0, y0 = 20, 20
    thickness = 2
    length = 400
    line_styles = cycle(LineStyles)
    # H lines
    for i in range(10):
        line = HorizontalLine(x0, y0, length, thickness=thickness, style=next(line_styles))
        y0 += 15
        thickness += 1
        screen.add_child(line)

    # V lines
    x0, y0 = 20 + length + 50, 20
    thickness = 2
    for i in range(10):
        line = VerticalLine(x0, y0, length, thickness=thickness, style=next(line_styles))
        x0 += 15
        thickness += 1
        screen.add_child(line)

    #
    Renderer(screen, auto_resize=True).to_bob("lines.bob")


if __name__ == "__main__":
    main()