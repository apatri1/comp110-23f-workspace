"""Dictionary related functions exercise."""

__author__ = "730656248"


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the items in a list."""
    inverse_dict: dict[str, str] = dict()
    for key in inp_dict:
        if inp_dict[key] not in inverse_dict:
            inverse_dict[inp_dict[key]] = key
        else:
            raise KeyError("A dictionary cannot have duplicate keys!")
    return inverse_dict
            

def favorite_color(inp_dict: dict[str, str]) -> str:
    """Determines the most popular favorite color."""
    color_dict: dict[str, int] = dict()
    for key in inp_dict:
        if inp_dict[key] not in color_dict:
            color_dict[inp_dict[key]] = 1
        else:
            color_dict[inp_dict[key]] += 1
    max: int = 0
    match_key: str = ""
    for key in color_dict:
        if color_dict[key] > max:
            max = color_dict[key]
            match_key = key
    return match_key


def count(inp_list: list[str]) -> dict[str, int]:
    """Will return a dict counting the str."""
    count_dict: dict[str, int] = dict()
    for item in inp_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


def alphabetizer(inp_list: list[str]) -> dict[str, list[str]]:
    """Given a list, it will produce a dict that organizes words alphabetically."""
    idx: int = 0
    alp_dict: dict[str, list[str]] = dict()
    while idx < len(inp_list):
        current_word: str = inp_list[idx].lower()
        if current_word[0] in alp_dict:
            alp_dict[(current_word[0])].append(current_word)
        else:
            alp_dict[(current_word[0])] = [current_word]
        idx += 1
    return alp_dict
        

def update_attendance(days_dict: dict[str, list[str]], day: [str], student: [str]) -> dict[str, list[str]]:
    """Updates the current attendance dictionary."""
    if day in days_dict:
        days_dict[day].append(student)
    else:
        days_dict[day] = [student]
    return days_dict
