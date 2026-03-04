"""
Day 07 - Part 03
Project: Hangman (Step 3)

Objective:
1) Use a while loop to let the user guess again until they win.
2) Preserve previous correct guesses in the display string.
"""

# =========================
# --- Setup ---
# =========================

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Create placeholder with blanks
placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"

print(placeholder)

# =========================
# --- Game Loop ---
# =========================

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You Win!")