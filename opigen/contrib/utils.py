# -*- coding: utf-8 -*-
import math


def generate_arrow_points(p1: tuple[int, int], length: int = 100, thickness: int = 4,
                          head_fraction: float = 0.2,
                          angle1: float = 30.0, angle2: float = 70.0) -> list[tuple[int, int]]:
    """ Generate a list of (x, y) points forming an arrow shape.

                  p2
    p4               p3
    |---------------------> p1
    p5               p6
                  p7

    - total length: p1 -> mid (p4, p5), in pixel
    - head length: p1->p2, in pixel
    - angle1: p1 w.r.t. head length, in degree
    - angle2: p2->p3 extended at length w.r.t. length, in degree

    Parameters
    ----------
    p1 : tuple[int, int]
        The tip of the arrow.
    length : int, optional
        The total length of the arrow, by default 100.
    thickness : int, optional
        The thickness of the arrow, by default 4.
    head_fraction : float, optional
        The faction of the total length as the head length, measured from p1 to p2, by default 0.2.
    angle1 : float, optional
        The angle from total length to head length in degree, by default 30.0.
    angle2 : float, optional
        The angle from line p2, p3 w.r.t. line p3, p4, in degree, by default 70.0.
    """
    x1, y1 = p1
    theta1 = math.radians(angle1)
    theta2 = math.radians(angle2)

    head_length = head_fraction * length
    # p2
    x2 = x1 - head_length * math.cos(theta1)
    y2 = y1 - head_length * math.sin(theta1)

    # p3
    x3 = x2 + (head_length * math.cos(theta1) - thickness / 2) / math.tan(theta2)
    y3 = y1 - thickness / 2

    # p4
    x4 = x1 - length
    y4 = y1 - thickness / 2

    # p5
    x5, y5 = x4, y4 + thickness

    # p6
    x6, y6 = x3, y3 + thickness

    # p7
    x7, y7 = x2, y2 + 2 * head_length * math.sin(theta1)

    return [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6), (x7, y7)]


def rotate_points(center: tuple[int, int], points: list[tuple[int, int]], angle: float) -> list[tuple[int, int]]:
    """Rotate a list of (x, y) points by a given angle in degrees w.r.t. a given center point."""
    import math
    cx, cy = center
    radians = math.radians(angle)
    cos_val = math.cos(radians)
    sin_val = math.sin(radians)
    rotated_points = []
    for x, y in points:
        dx, dy = x - cx, y - cy
        new_x = cx + dx * cos_val - dy * sin_val
        new_y = cy + dx * sin_val + dy * cos_val
        rotated_points.append((int(new_x), int(new_y)))
    return rotated_points