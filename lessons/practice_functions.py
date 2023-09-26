"""Practice Writing Functions."""

def mimic(my_words: str) -> str:
    """Given the string my_words, outputs the same string"""
    return my_words

mimic("Hello!")

print(mimic("Hello!"))
# Two ways to print something using this function
my_words: str = "Hello!"
response: str = mimic(my_words)
print(response)

def mimic_letter(my_words: str = input("Input a word: "), letter_idx: int = input("Input an index: ")) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx >= len(my_words):
        return "Too high of an index"
    # We don't need an else because if we got to this point it means idx is valid
    # as soon as we return, it exits
    return my_words[letter_idx]
    
print(mimic_letter("hi",0))