"""Dictionary unit tests."""

__author__ = "730656248"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


def test_empty_dict():
    """Tests invert with an empty dictionary."""
    assert invert({}) == {}


def test_invert():
    """Tests invert with a full dictionary."""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


def test_long_list():
    """Tests invert with a dictionary with more than 1 key."""
    assert invert({'apple': 'cat', 'pear': 'dog', 'orange': 'fish'}) == {'cat': 'apple', 'dog': 'pear', 'fish': 'orange'}


def test_keyerror():
    """Tests the KeyError for duplicate keys."""
    with pytest.raises(KeyError):
        inp_dict = {'chris': 'jordan', 'michael': 'jordan'}
        invert(inp_dict)


def test_same_fav():
    """Tests favorite_color when everyone has the same fav color."""
    assert favorite_color({"Marc": "blue", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_tie_fav():
    """Tests favorite_color when there is a tie."""
    assert favorite_color({'Sarah': 'red', 'Mike': 'yellow', 'Bob': 'red', 'Bill': 'yellow'}) == "red"


def test_empty_color():
    """Tests favorite_color if there is an empty color."""
    assert favorite_color({'Sarah': 'red', 'Mike': 'yellow', 'Bob': 'red', 'Bill': ''}) == "red"


def test_count():
    """Tests count with a full list."""
    assert count(["sally", "molly", "sally", "mark", "bill"]) == {'sally': 2, 'molly': 1, 'mark': 1, 'bill': 1}


def test_count_one_key():
    """Tests count when there is one key."""
    assert count(['billy']) == {'billy': 1}


def test_count_empty():
    """Tests count with an empty key."""
    assert count(['billy', 'bob', '']) == {'billy': 1, 'bob': 1, '': 1}


def test_alphabetizer():
    """Tests alphabetizer with a full list."""
    assert alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]) == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}


def test_alphabetizer_one():
    """Tests alphabetizer with one item in list."""
    assert alphabetizer(["cat"]) == {'c': ['cat']}


def test_alphabetizer_caps():
    """Tests alphabetizer with a full list and capital letters."""
    assert alphabetizer(["cat", "Apple", "boy", "angry", "Bad", "car"]) == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}


def test_update_attendance():
    """Tests update_attendance with a full dict."""
    attendance_log: dict = {"Monday": ["Bill", "Mike"], "Tuesday": ["Sarah"]}
    assert update_attendance(attendance_log, "Tuesday", "Bill") == {'Monday': ['Bill', 'Mike'], 'Tuesday': ['Sarah', 'Bill']}


def test_update_attendance_new_day():
    """Tests update_attendance with a new day not listed in the dict."""
    attendance_log: dict = {"Monday": ["Bill", "Mike"], "Tuesday": ["Sarah"]}
    assert update_attendance(attendance_log, "Wednesday", "Mike") == {'Monday': ['Bill', 'Mike'], 'Tuesday': ['Sarah'], 'Wednesday': ['Mike']}


def test_update_attendance_double():
    """Tests update_attendance when a name is going to be updated for a day twice."""
    attendance: dict = {"Monday": ["Bill", "Mike", "Shelly"], "Tuesday": ["Sarah", "Bill"]}
    assert update_attendance(attendance, "Tuesday", "Bill") == {'Monday': ['Bill', 'Mike', 'Shelly'], 'Tuesday': ['Sarah', 'Bill']}