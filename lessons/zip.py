"""Combining two lists into a dictionary."""

__author__ = "730656248"


def zip(list_str: list[str], list_int: list[int]) -> dict[str, int]:
    """Produces a dictionary where the keys and values are in the input lists."""
    if (len(list_str) != len(list_int)) or ((len(list_str) or len(list_int)) == 0):
        return dict()
    list_dict: dict[str, int] = dict()
    idx: int = 0
    while idx < len(list_str):
        list_dict[list_str[idx]] = (list_int[idx])
        idx += 1
    return list_dict
