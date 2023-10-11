"""Exercise 04 Utility Functions."""

__author__ = "730656248"


def all(input: list[int], num: int) -> bool:
    """Checks if all the ints in the list equal the given int."""
    if len(input) == 0:
        return False
    list_idx: int = 0
    while len(input) > list_idx:
        if input[list_idx] != num:
            return False
        else:
            list_idx += 1
    return True


def max(input: list[int]) -> int:
    """Finds the max int in a list of ints."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    input_idx: int = 0
    max_int: int = input[0]
    while input_idx < len(input):
        current_int: int = input[input_idx]
        if current_int > max_int:
            max_int = current_int
        input_idx += 1
    return (max_int)


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Determines if two lists are equal."""
    if (len(list_1) == 0) and (len(list_2) == 0):
        return True     
    if (len(list_1) == 0) or (len(list_2) == 0):
        return False
    list_idx: int = 0
    while (list_idx < len(list_1)) and (list_idx < len(list_2)):
        if list_1[list_idx] != list_2[list_idx]:
            return False
        else:
            list_idx += 1
    return True