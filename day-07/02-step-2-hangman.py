"""
Day 07 - Part 02
Project: Hangman (Step 2)

Objective:
1) Create a placeholder string with "_" for each letter.
2) Reveal correctly guessed letters in the correct position.
"""

# =========================
# --- Setup ---
# =========================

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

# =========================
# --- TODO-1: Create Placeholder ---
# =========================

"""
Create an empty string called placeholder.
For each letter in chosen_word, add "_".
"""

placeholder = ""

for _ in range(len(chosen_word)):
    placeholder += "_"

print("Word to guess:", placeholder)


# =========================
# --- TODO-2: Create Display ---
# =========================

"""
Create an empty string called display.
Reveal guessed letters in correct positions.
"""

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print("Current display:", display)