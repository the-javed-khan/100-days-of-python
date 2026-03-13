"""
Day 07 - Part 01
Project: Hangman (Step 1)

Objective:
Start building Hangman step-by-step by:
1) Choosing a random word.
2) Taking user input for a guess.
3) Checking the guess against each letter in the chosen word.
"""

# =========================
# --- Setup ---
# =========================

import random

word_list = ["aardvark", "baboon", "camel"]  # (sample list for early steps)

# =========================
# --- TODO-1 ---
# =========================

"""
Randomly choose a word from the word_list
and assign it to a variable called chosen_word.
Then print it.
"""

chosen_word = random.choice(word_list)
print(chosen_word)

# =========================
# --- TODO-2 ---
# =========================

"""
Ask the user to guess a letter and assign their answer
to a variable called guess. Make it lowercase.
"""

guess = input("Guess a letter: ").lower()

# =========================
# --- TODO-3 ---
# =========================

"""
Check if the letter the user guessed is one of the letters
in the chosen_word.

Loop through each letter in chosen_word and print:
- "Right" if the letter matches guess
- "Wrong" if it does not
"""

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")