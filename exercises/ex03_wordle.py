"""Structured Wordle."""

__author__ = "730656248"

def contains_char(search_str: str, sing_chr: str) -> bool:
    """Searches for the single character in the string."""
    assert len(sing_chr) == 1
    search_idx: int = 0
    while search_idx < len(search_str):
        if search_str[search_idx] == sing_chr:
            return True
        else:
            search_idx += 1
    return False      

def emojified(user_guess: str, secret_word: str) -> str:
    """String of emoji boxes whose color determines the accuracy of the guess."""
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

def input_guess(expc_len: int) -> str:
    guess: str = input(f"Enter a {expc_len} character word: ")
    while (expc_len < len(guess)) or (expc_len > len(guess)):
        guess = input(f"That wasn't {expc_len} chars! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    user_turns: int = 1
    user_won: bool = False
    while (user_turns <= 6) and (user_won is False):
        guess: str = input_guess(len(secret))
        print(f"=== Turn {user_turns}/6 ===")
        print(emojified(guess, secret))
        if guess == secret:
            user_won = True
            print(f"You won in {user_turns}/6 turns!")
        user_turns += 1
        if (user_turns == 7) and (user_won is False):
            print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()


