from opigen.renderers import Renderer
from opigen.contrib import Display, VerticalLine
from opigen.contrib import HorizontalLine
from opigen.opimodel.widgets import LineStyles
from itertools import cycle
from opigen import colors
from opigen.opimodel.utils import filter_attributes


def main():
    screen = Display(name="Lines Widget")

    x0, y0 = 20, 20
    thickness = 2
    length = 400
    line_styles = cycle(LineStyles)
    phoebus_colors = cycle(filter_attributes(colors, "PHOEBUS_*").values())
    # H lines
    for i in range(10):
        line = HorizontalLine(x0, y0, length, thickness=thickness, style=next(line_styles))
        line.set_line_color(next(phoebus_colors))
        line.set_arrow_style("to")
        line.set_arrow_length(10)
        y0 += 15
        thickness += 0.5
        screen.add_child(line)

    # V lines
    x0, y0 = 20 + length + 50, 20
    thickness = 2
    for i in range(10):
        line = VerticalLine(x0, y0, length, thickness=thickness, style=next(line_styles))
        line.set_line_color(next(phoebus_colors))
        line.set_arrow_style("from")
        line.set_arrow_length(10)
        x0 += 15
        thickness += 0.5
        screen.add_child(line)

    #
    Renderer(screen, auto_resize=True).to_bob("lines.bob")


if __name__ == "__main__":
    main()