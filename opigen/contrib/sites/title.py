#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module maintains the resources for site customization.
"""

import os
from opigen.contrib import GroupingContainer
from opigen.opimodel.borders import Border, BorderStyle
from opigen import colors, widgets, fonts
from opigen.opimodel.widgets import HA_LEFT, HA_RIGHT, VA_BOTTOM, VA_TOP
from opigen.contrib import TextUpdate


def make_title(title: str, width: int, contact: str, **kws):
    """Make a title group

    Keyword Arguments
    -----------------
    x0 : int
        The x coordinate of the top left point, defaults 5.
    y0 : int
        The y coordinate of the top left point, defaults 0.
    height : int
        The height of the entire widget to create, defaults 80.
    phone : str
        Phone number to be reached.
    email : str
        Email account to be reached.
    affiliation : str
        Affiliation for the contact.
    clock_pv : str
        PV used for clock display.
    """
    x0 = kws.get('x0', 5)
    y0 = kws.get('y0', 0)
    height = kws.get('height', 80)
    clock_pv = kws.get('clock_pv', "PHY:DATETIME_NOW")
    title_group = GroupingContainer(x0, y0, width, height, '')
    title_group.set_border(Border(BorderStyle.LINE, 1, colors.ASBESTOS, False))
    _x, _y = 10, 10
    _w, _h = width - _x, 45

    # left most area: title
    title_w, title_h = 0.9 * _w, _h
    title_lbl = widgets.Label(_x, _y, title_w, title_h, title)
    title_lbl.set_font(fonts.TITLE)
    title_lbl.horizontal_alignment = HA_LEFT
    title_group.add_child(title_lbl)

    # right most area: datetime string
    datetime_w, datetime_h = _w, _h
    datetime_x = _w - datetime_w
    datetime_text = TextUpdate(datetime_x, _y, datetime_w, datetime_h, clock_pv)
    datetime_text.transparent = True
    datetime_text.horizontal_alignment = HA_RIGHT
    datetime_text.vertical_alignment = VA_BOTTOM
    datetime_text.set_font(fonts.MONOSPACE)
    title_group.add_child(datetime_text)

    contact_list = [contact, ]
    if kws.get('affiliation', None) is not None:
        contact_list.append(f"{kws.get('affiliation')}")
    if kws.get('phone', None) is not None:
        contact_list.append(f"Telephone: {kws.get('phone')}")
    if kws.get('email', None) is not None:
        contact_list.append(f"Email: {kws.get('email')}")
    contact_str = '\n├'.join(contact_list[:-1])
    contact_str += f'\n└{contact_list[-1]}'

    # contact info
    w_lbl, h_lbl = 25, 25
    contact_lbl = widgets.Label(_w - w_lbl, 0, w_lbl, h_lbl, "☎")
    contact_lbl.tooltip = contact_str
    contact_lbl.transparent = True
    # contact_lbl.set_border(Border(BorderStyle.NONE, 1, colors.ASBESTOS, False))
    contact_lbl.horizontal_alignment = HA_RIGHT
    contact_lbl.vertical_alignment = VA_BOTTOM
    contact_lbl.set_font(fonts.HEADER_5)
    title_group.add_child(contact_lbl)

    # bottom: horizontal line
    line_y = _y + _h
    for i in (8, 4, 2):
        hline = widgets.Line(_x, line_y, _w, line_y, i)
        # hline.set_line_color(colors.SILVER)
        title_group.add_child(hline)
        line_y += (i + 1)

    return title_group


def make_my_title(title, width, contact="Tong Zhang", phone="x7421", email="zhangt@frib.msu.edu", affiliation="Accelerator Physics Department", **kws):
    return make_title(title, width, contact=contact, phone=phone, email=email, affiliation=affiliation, **kws)


def make_title_macro(title: str, width: int,
                     x0: int = 5, y0: int = 0, height: int = 80,
                     contact: str = "$(CONTACT)", phone: str = "$(PHONE)",
                     email: str = "$(EMAIL)", affiliation: str = "$(AFFILIATION)",
                     clock_pv: str = "$(CLOCK_PV=PHY:DATETIME_NOW)"):
    return make_title(title, width,
                      contact=contact, phone=phone, email=email, affiliation=affiliation,
                      x0=x0, y0=y0, height=height, clock_pv=clock_pv)
