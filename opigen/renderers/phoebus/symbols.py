import lxml.etree as et


class OpiSymbols(object):

    def render(self, widget_node, tag_name, symbols_model: list[str]):
        symbols_node = et.SubElement(widget_node, "symbols")
        for sym_path in symbols_model:
            et.SubElement(symbols_node, "symbol").text = sym_path

