import lxml.etree as et
from opigen.colors import Color


class OpiStates:

    """Render states of MultiStateLed.
    """
    def __init__(self, color_renderer):
        self._cr = color_renderer

    def render(self, widget_node, tag_name: str, states_model: list[tuple[int, str, Color]]):
        states_node = et.SubElement(widget_node, "states")
        for value, label, color in states_model:
            state_node = et.SubElement(states_node, "state")
            et.SubElement(state_node, "value").text = str(value)
            et.SubElement(state_node, "label").text = label
            self._cr.render(state_node, 'color', color)
