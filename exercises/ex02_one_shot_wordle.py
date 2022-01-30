"""trying to figure out how to do wordle!"""

__author__ = 730408031

secret_word = str("python")
guess = input(f"What is your {len(secret_word)}-letter guess? ")
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

sw_index = 0
g_index = 0
yellow_count = 0

while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")
while g_index < len(secret_word):
    if secret_word[g_index] == guess[g_index]:
        print(green_box)
    else:
        sw_index = 0
        while sw_index < len(secret_word):
            if secret_word[sw_index] == guess[g_index]:
                print(yellow_box)
                sw_index = len(secret_word)
                yellow_count += 1
            else:
                sw_index += 1
        if yellow_count < 1:
            print(white_box)
        yellow_count = 0
    g_index += 1
if guess != str(secret_word):
    print("Not quite. Play again soon!")
    
else:
    print("Woo! You got it!")
    quit()
