"""CQ07 creating point class."""

from __future__ import annotations

__author__ = "730656248"


class Point:
    x: float
    y: float
    def __init__(self, x_init: float, y_init: float):
        """My constructor."""
        self.x = x_init
        self.y = y_init

    
    def scale_by(self, factor: int) -> None:
        """Mutates a point."""
        self.x = self.x * factor
        self.y = self.y * factor


    def scale(self, factor: int) -> Point:
        """Creates a new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point