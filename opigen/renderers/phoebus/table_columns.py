import lxml.etree as et
from opigen.opimodel.table_columns import Column
from .text import OpiText

_boolean_str_map = {False: 'false', True: 'true'}

class OpiColumns:

    def render(self, widget_node, tag_name: str, columns: list[Column]) -> None:
        columns_node = et.SubElement(widget_node, "columns")
        for column in columns:
            column_node = et.SubElement(columns_node, "column")
            OpiText().render(column_node, "name", column.name)
            OpiText().render(column_node, "width", f"{column.width:.0f}")
            OpiText().render(column_node, "editable", _boolean_str_map[column.editable])
