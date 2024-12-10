from opigen.contrib import Display
from opigen import Renderer
from opigen.opimodel.widgets import MultiStateLed
from opigen import colors


def main():
    screen = Display(name='MultiStateLed')

    mled = MultiStateLed(20, 20, 100, 30,
                         "loc://ramp(0, 3, 1)")
    mled.add_state(0, "State 1", colors.RED)
    mled.add_state(1, "State 2", colors.BLUE)
    mled.add_state(2, "State 3", colors.GREEN)

    screen.add_child(mled)

    Renderer(screen, auto_resize=True).to_bob("multi_state_led.bob")


if __name__ == "__main__":
    main()