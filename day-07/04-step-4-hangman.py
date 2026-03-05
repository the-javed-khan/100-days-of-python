"""
Day 07 - Part 04
Project: Hangman (Step 4)

Objective:
1) Track remaining lives (start at 6).
2) Reduce lives when the guess is wrong.
3) End game when lives reach 0 (lose condition).
4) Print hangman ASCII stage based on remaining lives.
"""

# =========================
# --- Setup ---
# =========================

import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

# =========================
# --- Game Variables ---
# =========================

lives = 6
chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"

print(placeholder)

game_over = False
correct_letters = []

# =========================
# --- Game Loop ---
# =========================

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

    # TODO-2: reduce lives if guess is wrong
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")

    # win condition
    if "_" not in display:
        game_over = True
        print("You win.")

    # TODO-3: show stage based on remaining lives
    print(stages[lives])