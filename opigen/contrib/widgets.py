import opigen.opimodel.widgets as _widgets
from opigen import fonts, colors, rules, scripts
from opigen.opimodel.colors import Color
from opigen.opimodel.borders import Border, BorderStyle
import os

# default widget color configurations
DEFAULT_DISPLAY_BG = Color((255, 255, 255), "DISPLAY_BG")
DEFAULT_TEXTUPDATE_BG = Color((240, 240, 240), "TEXTUPDATE_BG")
DEFAULT_TEXTENTRY_BG = Color((236, 240, 241), "TEXTENTRY_BG")
DEFAULT_BORDER_COLOR = Color((0, 128, 255), "BORDER_BLUE")

# absolute path for resource files, e.g. images.
RES_DIRPATH = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                           'images'))


class ProgressBar(_widgets.ProgressBar):

    MINOR_COLOR = colors.CARROT
    MAJOR_COLOR = colors.ALIZARIN
    INVALID_COLOR = colors.INVALID
    NORMAL_COLOR = colors.EMERLAND
    def __init__(self, x: int, y: int, width: int, height: int,
                 pv_name: str, minimum: float = 0, maximum: float = 100,
                 limits_from_pv: bool = False,
                 border_alarm_sensitive: bool = False):
        super(self.__class__, self).__init__(x, y, width, height, pv_name,
                minimum, maximum, limits_from_pv, border_alarm_sensitive)
        self.fill_color = ProgressBar.NORMAL_COLOR
        self.add_rule(
                rules.SelectionRule(
                    "fill_color", pv_name, "Change color per severity",
                    # -1: invalid, 1: major, 2: minor
                    sevr_options=[
                        (-1, ProgressBar.INVALID_COLOR),
                        (1, ProgressBar.MAJOR_COLOR),
                        (2, ProgressBar.MINOR_COLOR)
                    ]))


class ActionButton(_widgets.ActionButton):
    def __init__(self, x, y, width, height, text):
        super(self.__class__, self).__init__(x, y, width, height, text)
        self.set_font(fonts.DEFAULT)


class SlideButton(_widgets.ImageBoolButton):

    # Emulates SlideButton in Phoebus

    def __init__(self, x, y, width, height, pv_name, alarm_sensitive=False):
        super(self.__class__, self).__init__(x, y, width, height, pv_name)
        self.on_image = ".images/toggle_on.png"
        self.off_image = ".images/toggle_off.png"
        self.transparency = True
        self.set_border(
            Border(BorderStyle.NONE, 1, DEFAULT_BORDER_COLOR, alarm_sensitive))

    def get_resources(self):
        """Get required resource files and distribute with the final generate OPI.
        """
        return [(os.path.abspath(os.path.join(RES_DIRPATH,
                                              os.path.basename(p))), p)
                for p in (self.on_image, self.off_image)]


class Display(_widgets.Display):

    def __init__(self, width=800, height=600, name=None):
        super(self.__class__, self).__init__(width, height)
        #
        self.set_bg_color(DEFAULT_DISPLAY_BG)
        if name is not None:
            self.name = name

    def get_opt_size(self):
        """Get the optimal size (width, height) to contain all the
        child widgets.
        """
        children_parent_not_group = []
        for i in self.get_children():
            if hasattr(i, "visible") and not i.visible:
                print(f"Skipping hidden widget: {i.name}")
                continue
            if isinstance(i.get_parent(), _widgets.GroupingContainer):
                print(f"Skipping group child widget: {i.name}")
                continue
            children_parent_not_group.append(i)
        xlist = [i.x for i in children_parent_not_group]
        xlist += [i.x + i.width for i in children_parent_not_group]
        ylist = [i.y for i in children_parent_not_group]
        ylist += [i.y + i.height for i in children_parent_not_group]
        min_x, max_x = min(xlist), max(xlist)
        min_y, max_y = min(ylist), max(ylist)
        opt_w = max_x - min_x
        opt_h = max_y - min_y
        return opt_w, opt_h

    def set_opt_size(self, dw: int = 15, dh: int = 15):
        """Adjust the display size to best contain all child widgets.
        """
        w, h = self.get_opt_size()
        self.width = w + dw
        self.height = h + dh

    def init_vars(self, vars: list[str]):
    #def init_vars(self, names: list[str], values: list, dtypes: list[str]):
        """Use to initialize a list of variables (e.g. loc variables).
        dtype: str or number
        As of now (2024/03/14, Display dose not support script.)
        """
        for var in vars:
            w = _widgets.TextEntry(0, 0, 0, 0, var)
            w.visible = False
            self.add_child(w)
#        script = scripts.Script(script_text="""from org.csstudio.display.builder.runtime.script import PVUtil
#        names = {}.split(",")
#        values = {}.split(",")
#        dtypes = {}.split(",")
#        for name, value, dtype in zip(names, values, dtypes):
#            PVUtil.createPV(name, 5000)
#            if dtype != 'str':
#                value = float(value)
#            PVUtil.writePV(name, value, 5000)
#        """.format(','.join(names), ','.join([str(v) for v in values]), ','.join(dtypes)))


class EmbeddedContainer(_widgets.EmbeddedContainer):

    def __init__(self, x, y, width, height, opi_file):
        super(self.__class__, self).__init__(x, y, width, height, opi_file)
        #
        self.set_bg_color(DEFAULT_DISPLAY_BG)


class GroupingContainer(_widgets.GroupingContainer):

    def __init__(self, x, y, width, height, name=None):
        _widgets.GroupingContainer.__init__(self, x, y, width, height, name)
        #
        self.set_bg_color(DEFAULT_DISPLAY_BG)
        # preset font
        _widgets.GroupingContainer.set_font(self, fonts.GROUPBOX_NAME)
        _widgets.GroupingContainer.set_border(self,
                Border(BorderStyle.GROUP_BOX, 1, colors.ASBESTOS, False))


class Label(_widgets.Label):
    def __init__(self, x, y, width, height, text):
        super(self.__class__, self).__init__(x, y, width, height, text)
        self.set_font(fonts.DEFAULT)


class TextUpdate(_widgets.TextUpdate):

    def __init__(self, x, y, width, height, pv_name, alarm_sensitive=True):
        super(self.__class__, self).__init__(x, y, width, height, pv_name)
        #
        self.set_bg_color(DEFAULT_TEXTUPDATE_BG)
        self.set_border(
            Border(BorderStyle.NONE, 0, DEFAULT_BORDER_COLOR, alarm_sensitive))
        self.set_font(fonts.DEFAULT)


class TextEntry(_widgets.TextEntry):

    def __init__(self, x, y, width, height, pv_name, border_alarm_sensitive: bool = True):
        super(self.__class__, self).__init__(x, y, width, height, pv_name)
        #
        self.set_bg_color(DEFAULT_TEXTENTRY_BG)
        self.set_font(fonts.DEFAULT)
        self.border_alarm_sensitive = border_alarm_sensitive
        self.phoebus_border_alarm_sensitive = border_alarm_sensitive


class Spinner(_widgets.Spinner):

    def __init__(self, x, y, width, height, pv_name):
        super(self.__class__, self).__init__(x, y, width, height, pv_name)
        #
        self.set_bg_color(DEFAULT_TEXTENTRY_BG)
        self.set_font(fonts.DEFAULT)


class Led(_widgets.Led):

    def __init__(self, x, y, width, height, pv_name, alarm_sensitive=False):
        super(self.__class__, self).__init__(x, y, width, height, pv_name)
        #
        self.effect_3d = False
        self.bulb_border = 1
        self.set_border(
            Border(BorderStyle.NONE, 1, DEFAULT_BORDER_COLOR, alarm_sensitive))
        self.off_color = colors.ALIZARIN
        self.on_color = colors.EMERLAND


class CheckBox(GroupingContainer):
    """CheckBox with background color support.
    """
    def __init__(self, x, y, width, height, text, pv_name, **kws):
        GroupingContainer.__init__(self, x, y, width + 5, height + 5, "")
        self.chkbox = chkbox = _widgets.CheckBox(
            kws.get("x0", 1), kws.get("y0", 1), width, height, text, pv_name)
        if kws.get("borderless", False):
            self.set_borderless()
        self.add_child(chkbox)
        self.set_font(fonts.DEFAULT)

    def set_borderless(self):
        self.set_border(
            Border(BorderStyle.NONE, 0, Color((255, 255, 255)), False))

    @property
    def pv_name(self):
        return self.chkbox.pv_name

    @pv_name.setter
    def pv_name(self, pv_name: str):
        self.chkbox.pv_name = pv_name

    def set_fg_color(self, c):
        self.chkbox.set_fg_color(c)

    def set_font(self, font):
        self.chkbox.set_font(font)
