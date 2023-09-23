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

def emojified(user_guess: str, secret_word: str) -> str:
    """String of emoji boxes whose color determines the accuracy of the guess"""
    assert len(user_guess) == len(secret_word)
    result: str = ""
    word_idx: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while word_idx < len(secret_word):
        if secret_word[word_idx] == user_guess[word_idx]:
            result += GREEN_BOX
            word_idx += 1           
        elif contains_char(secret_word, user_guess[word_idx]) == True:
            result += YELLOW_BOX
            word_idx += 1
        else:
            result += WHITE_BOX
            word_idx += 1
    return result