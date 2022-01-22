"""EX01 - Chardle - A cute step toward Wordle."""

instances: int = 0
word: str = input("Enter a 5-character word: ")
if len(word) == 5:
    single_character: str = input("Enter a single character: ")
    if len(single_character) == 1:
        print("Searching for " + single_character + " in " + word)
        if word[0] == single_character:
            print(single_character + " found at index 0")
            instances = instances + 1
        if word[1] == single_character:
            print(single_character + " found at index 1")
            instances = instances + 1
        if word[2] == single_character:
            print(single_character + " found at index 2")
            instances = instances + 1
        if word[3] == single_character:
            print(single_character + " found at index 3")
            instances = instances + 1
        if word[4] == single_character:
            print(single_character + " found at index 4")
            instances = instances + 1
        if instances == 1:
            print("1 instance of " + single_character + " found in " + word)
        else:
            if instances == 0:
                print("No instances of " + single_character + " found in " + word)
            else:
                print(str(instances) + " instances of " + single_character + " found in " + word)
    else:
        print("Error: Character must be a single character.")
        exit()
else:
    print("Error: Word must contain 5 characters.")
    exit()

__author__ = "730408031"