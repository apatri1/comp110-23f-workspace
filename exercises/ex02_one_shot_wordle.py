"""One Shot Wordle."""

__author__ = "730626548"

secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
word_idx: int = 0
result: str = ""
# In case the user writes a word < or > the secret word
while (len(guess) > len(secret)) or (len(guess) < len(secret)):
    guess = input(f"That was not {len(secret)} letters! Try again: ")
while word_idx < len(secret):
    if guess[word_idx] == secret[word_idx]:
        result += GREEN_BOX
        # The user got this character correct, skips to the next character
    if guess[word_idx] != secret[word_idx]:
        chr_exists_alt: bool = False
        alt_idx: int = 0
        while (chr_exists_alt is False) and (alt_idx < len(secret)):
            if guess[word_idx] == secret[alt_idx]:
                chr_exists_alt = True
        # It is true that this character exists somewhere in the secret word
            else:
                alt_idx += 1
        if chr_exists_alt is True:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
            # This character is not in the word at all
    word_idx += 1
print(result)
if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")