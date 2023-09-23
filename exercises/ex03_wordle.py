"""Structured Wordle."""

__author__ = "730656248"

def contains_char(search_str: str, sing_chr: str) -> bool:
    """Searches for the single character in the string"""
    assert len(sing_chr) == 1
    search_idx: int = 0
    while search_idx < len(search_str):
        if search_str[search_idx] == sing_chr:
            return True
        else:
            search_idx += 1
    return False      
        