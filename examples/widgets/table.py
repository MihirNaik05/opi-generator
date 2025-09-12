from opigen import scripts
from opigen import widgets
from opigen.table_columns import Column
from opigen.contrib import Display
from opigen.renderers import Renderer

TB_SCRIPT_TEXT = """from org.csstudio.display.builder.runtime.script import PVUtil
data = []
for i, pv in enumerate(pvs):
    row = [str(i), pv.getName(), PVUtil.getString(pv)]
    data.append(row)
widget.setValue(data)"""

def main():
    screen = Display(name="Table Widget")
    table = widgets.Table(20, 20, 800, 300)
    table.show_toolbar = False
    table.add_column(Column("ID", 50, False))
    table.add_column(Column("Name", 250, False))
    table.add_column(Column("Value", 300, False))

    script = scripts.Script(script_text=TB_SCRIPT_TEXT)
    script.add_pv("sim://sine")
    script.add_pv("sim://noise")
    script.add_pv("sim://ramp")
    table.add_script(script)

    screen.add_child(table)

    r = Renderer(screen)
    r.to_bob("table.bob")


if __name__ == "__main__":
    main()
