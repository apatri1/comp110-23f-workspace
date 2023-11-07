"""Test my zip function."""

__author__ = "730656248"

from lessons.zip import zip


def test_empty_list() -> None:
    """Testing with empty arguments."""
    assert zip([], []) == {}


def test_two_args() -> None:
    """Testing with two complete arguments."""
    assert zip(["Vanilla", "Chocolate"], [3, 11]) == {'Vanilla': 3, 'Chocolate': 11}


def test_three_keys() -> None:
    """Testing zip with three str and three int."""
    assert zip(["Bob", "John", "Bill"], [23, 27, 16]) == {'Bob': 23, 'John': 27, 'Bill': 16}