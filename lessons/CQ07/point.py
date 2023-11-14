"""CQ07 creating point class."""

from __future__ import annotations

__author__ = "730656248"


class Point:
    """Class to represent (x,y) coordinate point."""

    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """My constructor."""
        self.x = x_init
        self.y = y_init

    def __str__(self) -> str:
        """Magic method."""
        output: str = f"x: {self.x}; y: {self.y}"
        return output
    
    def scale_by(self, factor: int) -> None:
        """Mutates a point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creates a new point."""
        return Point(self.x * factor, self.y * factor) 

    def __mul__(self, factor: int | float) -> Point:
        """Operator overload, multiplication."""
        return Point(self.x * factor, self.y * factor)   

    def __add__(self, factor: int | float) -> Point:
        """Operator overload, addition."""
        return Point(self.x + factor, self.y + factor)
        