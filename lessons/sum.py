"""Challenge Question 06."""

__author__ = "730656248"


def w_sum(vals: list[float]) -> float:
    """Finds the sum of the items in the list."""
    sum: float = 0
    idx: int = 0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Uses for ... in loop to find the sum."""
    sum: float = 0
    for num in vals:
        sum += num
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Uses for... in range loop to find the sum."""
    sum: float = 0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum