import lxml.etree as et
from .text import OpiText


class OpiColor(object):

    def render(self, widget_node, tag_name, color_model):
        parent_color_node = et.SubElement(widget_node, tag_name)
        color_node = et.SubElement(parent_color_node, 'color')
        color_node.set('red', str(color_model.red))
        color_node.set('green', str(color_model.green))
        color_node.set('blue', str(color_model.blue))
        if color_model.name is not None:
            color_node.set('name', color_model.name)
        if color_model.alpha is not None:
            color_node.set('alpha', str(color_model.alpha))


class OpiColorLinearMeter(object):

    def render(self, widget_node, tag_name, colors_model):
        colors_node = et.SubElement(widget_node, "colors")
        for attr_name, (is_color, attr_conf) in colors_model.items():
            if is_color:
                OpiColor().render(colors_node, attr_name, attr_conf)
            else:
                OpiText().render(colors_node, attr_name, attr_conf)

