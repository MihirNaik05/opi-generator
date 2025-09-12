#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from opigen import actions, colors, fonts, rules, widgets
from opigen.enums import (
    HA_RIGHT, HA_CENTER, HA_LEFT, VA_TOP, VA_MIDDLE, VA_BOTTOM,
    FormatType, BasicStyle
)
from opigen.contrib import Display, TextUpdate, TextEntry
from opigen.contrib import LedGreenDark as Led
from opigen import Renderer
from opigen.contrib.sites import make_my_title as make_title

import json
import os
import pandas as pd


def main(outfile: str, phoebus_enable: bool = False):
    if phoebus_enable:
        SlideButton = widgets.SlideButton
    else:
        from opigen.contrib import SlideButton
    #
    VIOLA_CWD = "/files/shared/ap/HLA/viola-config"
    VIOLA_CMD = f"/usr/bin/start_viola.sh --set-dir {VIOLA_CWD} --setting {VIOLA_CWD}/$(name)"

    LED_W = LED_H = 28
    df = pd.read_excel("devices.xlsx", sheet_name="FTC")

    x0, y0 = 5, 5
    width, height = 1760, 600
    vgap, hgap = 10, 8
    screen = Display(width, height, "ARIS CAM/VDs")

    # title
    h = 30
    title = make_title("ARIS Camera/Viewer Devices", width)
    screen.add_child(title)

    # add a hline
    hline1 = widgets.Line(x0, y0 + title.height + 5,
                          width, y0 + title.height + 5)
    hline1.set_bg_color(colors.CONCRETE)
    screen.add_child(hline1)

    # Add devices
    y1 = y0 + title.height + vgap
    w_name = 224
    w_ctrl = 280 # see below: _w1 + _w2 + .. + _w5
    w_type, x1 = 55, x0 + w_name + hgap + w_ctrl
    w_alias, x2 = 67, x1 + w_type + hgap
    w_txt_x, x3 = 100, x2 + w_alias + hgap
    w_txt_y, x4 = 100, x3 + w_txt_x + hgap
    w_txt_rx, x5 = 100, x4 + w_txt_y + hgap
    w_txt_ry, x6 = 100, x5 + w_txt_rx + hgap
    w_txt_cxy, x7 = 100, x6 + w_txt_ry + hgap
    w_txt_inten, x8 = 100, x7 + w_txt_cxy + hgap
    w_btn, x9 = 100, x8 + w_txt_inten + hgap
    w_conf, x10 = 350, x9 + w_btn + hgap

    # make header
    header_name = widgets.Label(x0, y1, w_name, h, "Name")

    #
    header_type = widgets.Label(x1, y1, w_type, h, "Type")
    header_type.horizontal_alignment = HA_CENTER
    header_alias = widgets.Label(x2, y1, w_alias, h, "Alias")
    header_x = widgets.Label(x3, y1, w_txt_x, h, "x0 [mm]")
    header_y = widgets.Label(x4, y1, w_txt_y, h, "y0 [mm]")
    header_rx = widgets.Label(x5, y1, w_txt_rx, h, "σx [mm]")
    header_ry = widgets.Label(x6, y1, w_txt_ry, h, "σy [mm]")
    header_cxy = widgets.Label(x7, y1, w_txt_cxy, h, "ρxy")
    header_inten = widgets.Label(x8, y1, w_txt_inten, h, "Intensity")
    header_btn = widgets.Label(x9, y1, w_btn, h, "Viola")
    header_conf = widgets.Label(x10, y1, w_conf, h, f"{VIOLA_CWD}/")
    for w in (header_name, header_type, header_alias, header_x, header_y,
              header_rx, header_ry, header_cxy, header_inten, header_btn,
              header_conf):
        w.set_font(fonts.HEADER_5)
        w.horizontal_alignment = HA_CENTER
        screen.add_child(w)

    #
    _w1, _x1 = 30, x0 + w_name + hgap / 2 # In?
    _w2, _x2 = 50, _x1 + _w1 + hgap / 2   # light ctrl
    _w3, _x3 = 30, _x2 + _w2 + hgap / 2   # light on?
    _w4, _x4 = 60, _x3 + _w3 + hgap / 2   # acquire status
    _w41, _x41 = 20, _x4 + _w4 + hgap / 2 # start acquire, btn
    _w42, _x42 = 20, _x41 + _w41 + hgap * 1.5 # stop acquire, btn
    _w5, _x5 = 20, _x42 + _w42 + hgap * 1.5   # full control page, open linked opi

    header_in_sts = widgets.Label(_x1, y1, _w1, h, "In?")
    header_lgt_ctrl = widgets.Label(_x2, y1, _w2 + _w3, h, "Light")
    # header_lgt_sts = widgets.Label(_x3, y1, _w3, h, "LGT?")
    header_daq_sts = widgets.Label(_x4, y1, _w4 + _w41 + _w42 + _w5, h, "Controls")
    for iw in (header_in_sts, header_lgt_ctrl, header_daq_sts):
        iw.set_font(fonts.HEADER_5)
        screen.add_child(iw)

    # add a hline
    hline2 = widgets.Line(x0, y1 + h + 3, width, y1 + h + 3)
    hline2.set_bg_color(colors.CONCRETE)
    screen.add_child(hline2)

    for _, row in df.iterrows():
        y1 += h + vgap
        # name
        name, type, alias = row.Name, row.Type, row.Alias
        x_pv, y_pv, rx_pv, ry_pv, cxy_pv, inten_pv = \
                row.X, row.Y, row.XRMS, row.YRMS, row.CXY, row.INTEN
        in_sts_pv = row.IN_STS
        lgt_ctl_pv, lgt_sts_pv = row.Light, row.Light_STS
        acq_sts_pv = row.Acquire_State
        acq_start_pv = row.Acquire_Start # set 1
        acq_stop_pv = row.Acquire_Stop   # set 0
        conf_pv = row.CONFIG
        #
        opi_path, opi_macros = row.OPI_PATH, json.loads(row.OPI_MACROS.strip("' "))

        # device name
        name_lbl = widgets.Label(x0, y1, w_name, h, name)
        name_lbl.horizontal_alignment = HA_CENTER

        # IN?, LGT_CTRL, LGT_STS?, DAQ?
        if in_sts_pv == '-':
            in_sts_led = widgets.Label(_x1, y1, LED_W, LED_H, '-')
        else:
            in_sts_led = Led(_x1, y1, LED_W, LED_H, in_sts_pv)
        in_sts_led.horizontal_alignment = HA_CENTER
        screen.add_child(in_sts_led)
        #
        if lgt_ctl_pv == '-':
            lgt_ctrl_btn = widgets.Label(_x2, y1, _w2, h, "-")
            lgt_sts_led = widgets.Label(_x3, y1, _w3, h, "-")
        else:
            lgt_ctrl_btn = SlideButton(_x2, y1, _w2, LED_H, lgt_ctl_pv)
            lgt_ctrl_btn.auto_size = True
            lgt_sts_led = Led(_x3, y1, LED_W, LED_H, lgt_sts_pv)
        lgt_ctrl_btn.horizontal_alignment = HA_CENTER
        lgt_sts_led.horizontal_alignment = HA_CENTER
        screen.add_child(lgt_ctrl_btn)
        screen.add_child(lgt_sts_led)
        # acquire state
        acq_sts_text = TextUpdate(_x4, y1, _w4, h, acq_sts_pv)
        acq_sts_text.set_font(fonts.DEFAULT_SMALL)
        # 0: Idle, 1: Acquire, other.
        acq_sts_text.add_rule(
            rules.SelectionRule(
                "background_color",
                acq_sts_pv,
                "change background color",
                [(1, colors.GREEN), (0, colors.RED)],
                else_val=colors.ASBESTOS,
            ))
        screen.add_child(acq_sts_text)

        # start acquire button
        acq_start_btn = widgets.ActionButton(_x41, y1, h, h, u'\N{BLACK RIGHT-POINTING TRIANGLE}')
        acq_start_btn.tooltip = f"Start acquire for {name}"
        acq_start_btn.add_write_pv(acq_start_pv, 1, f"Write {acq_start_pv} 1")
        screen.add_child(acq_start_btn)
        # stop acquire button
        acq_stop_btn = widgets.ActionButton(_x42, y1, h, h, u'\N{BLACK SQUARE}')
        acq_stop_btn.tooltip = f"Stop acquire for {name}"
        acq_stop_btn.add_write_pv(acq_stop_pv, 0, f"Write {acq_stop_pv} 0")
        screen.add_child(acq_stop_btn)

        # full control
        dev_ctrl_btn = widgets.ActionButton(_x5, y1, h, h, u"\N{TRIGRAM FOR HEAVEN}")
        desc = f"Open CAM/VD engineering page for {name}"
        dev_ctrl_btn.tooltip = desc
        dev_ctrl_btn.add_open_opi(opi_path,
                                  mode=actions.OpenOpi.WORKBENCH_TAB,
                                  description=desc,
                                  macros=opi_macros)
        screen.add_child(dev_ctrl_btn)

        # device type
        type_lbl = widgets.Label(x1, y1, w_type, h, type)
        type_lbl.horizontal_alignment = HA_CENTER
        # device alias
        alias_lbl = widgets.Label(x2, y1, w_alias, h, alias)
        # x,y,rx,rx,cxy,inten
        x_txt = TextUpdate(x3, y1, w_txt_x, h, x_pv)
        y_txt = TextUpdate(x4, y1, w_txt_y, h, y_pv)
        rx_txt = TextUpdate(x5, y1, w_txt_rx, h, rx_pv)
        ry_txt = TextUpdate(x6, y1, w_txt_ry, h, ry_pv)
        cxy_txt = TextUpdate(x7, y1, w_txt_cxy, h, cxy_pv)
        inten_txt = TextUpdate(x8, y1, w_txt_inten, h, inten_pv)
        for _w in (x_txt, y_txt, rx_txt, ry_txt, cxy_txt, inten_txt):
            _w.precision = 3
            _w.precision_from_pv = False
            _w.show_units = False
            _w.horizontal_alignment = HA_RIGHT
            _w.set_font(fonts.MONOSPACE)
        inten_txt.format_type = FormatType.EXPONENTIAL
        # start viola button
        viola_btn = widgets.ActionButton(x9, y1, w_btn, h, "Open")
        viola_btn.pv_name = ""
        viola_btn.tooltip = "Open Viola with defined configuration."
        viola_btn.add_shell_command(VIOLA_CMD, "Start Viola", VIOLA_CWD)
        viola_btn.add_rule(
            rules.SelectionRule("name",
                                conf_pv,
                                "change name", [("true", "pvStr0")],
                                out_exp='true',
                                auto_fill_val=False))
        conf_input = TextEntry(x10, y1, w_conf, h, conf_pv)
        conf_input.horizontal_alignment = HA_CENTER

        #
        for i, w in enumerate((name_lbl, type_lbl, alias_lbl, x_txt, y_txt, rx_txt,
                               ry_txt, cxy_txt, inten_txt, viola_btn, conf_input)):
            if i not in (3, 4, 5, 6, 7, 8):
                w.set_font(fonts.DEFAULT)
            screen.add_child(w)

    # vline1: before Type column
    vline1 = widgets.Line(x1, title.height + vgap, x1, y1 + h)
    vline1.set_bg_color(colors.CONCRETE)
    screen.add_child(vline1)
    # vline2: before In? column
    vline2 = widgets.Line(name_lbl.x + name_lbl.width - 5, title.height + vgap,
                          name_lbl.x + name_lbl.width - 5, y1 + h)
    vline2.set_bg_color(colors.CONCRETE)
    screen.add_child(vline2)

    # add a hline
    hline3 = widgets.Line(x0, y1 + h + 5, width, y1 + h + 5)
    hline3.set_bg_color(colors.CONCRETE)
    screen.add_child(hline3)

    if phoebus_enable:
        # for Phoebus
        Renderer(screen, auto_resize=True).to_bob(outfile)
    else:
        # for CS-Studio
        Renderer(screen, auto_resize=True).to_opi(outfile)


if __name__ == "__main__":
    # Generate OPI file for Phoebus
    main("viola.bob", True)
    # Generate OPI file for CS-Studio
    main("viola.opi", False)
