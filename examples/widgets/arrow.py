#
# Use lines to compose an arrow
#
from opigen.contrib import Display
from opigen import widgets, colors
from opigen.renderers import Renderer

from opigen.contrib import Arrow


def main():
    screen = Display(name="Arrow Widget", width=800, height=600)

    # a new arrow pointing to p1, and rotated 45 degree close-wise
    p1 = (100, 100)
    new_arrow = Arrow(*p1, length=100, thickness=4, head_fraction=0.25, angle1=20, angle2=80, rotate=45)
    screen.add_child(new_arrow)

    # A clone of the arrow, move right by 400px, then rotate 90 degree w.r.t. p1,
    # set the color to green
    arrow1 = new_arrow.clone()
    arrow1.x += 400
    arrow1.rotate(90, arrow1.map_to_local(p1))
    arrow1.set_color(colors.GREEN)
    screen.add_child(arrow1)

    #
    Renderer(screen, auto_resize=True).to_bob("arrow.bob")


if __name__ == "__main__":
    main()
