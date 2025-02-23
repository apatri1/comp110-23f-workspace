"""EX01 Chardle."""

__author__ = "730656248"

num_of_instances: int = 0
word: str = input("Enter a 5-character word: ")
if len(word) > 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(word) < 5:
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("Enter a single character: ")
if len(character) > 1:
    print("Error: Character must be a single character")
    exit()
if len(character) < 1:
    print("Error: Character must be a single character")
    exit()
print("Searching for " + character + " in " + word)

if word[0] == character:
    num_of_instances += 1
    print(character + " found at index 0")
if word[1] == character:
    num_of_instances += 1
    print(character + " found at index 1")
if word[2] == character:
    num_of_instances += 1
    print(character + " found at index 2")
if word[3] == character:
    num_of_instances += 1
    print(character + " found at index 3")
if word[4] == character:
    num_of_instances += 1
    print(character + " found at index 4")

if num_of_instances == 0:
    print("No instances of " + character + " found in " + word)
if num_of_instances == 1:
    print("1 instance of " + character + " found in " + word)
if num_of_instances > 1:
    print(str(num_of_instances) + " instances of " + character + " found in " + word)