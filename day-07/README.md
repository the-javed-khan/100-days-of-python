# Day 07 - Project Hangman
 
--------------------------------------------------------

## Part 01 – Hangman Step 1 (TODO 1–3)

### What I Learned in Practice
- Used random.choice() to select a word from a list
- Normalized user input using .lower()
- Looping through a string works like looping through a list
- Used if/else checks to compare guess against each character

--------------------------------------------------------

## Part 02 – Hangman Step 2 (Placeholder & Display)

### What I Learned in Practice
- Used range(len(word)) to create placeholders
- Built strings dynamically using +=
- Compared guessed letter with each character
- Revealed matching letters in correct positions
- Maintained hidden letters using "_"

--------------------------------------------------------

## Part 03 – Hangman Step 3 (While Loop + Preserve Letters)

### What I Learned in Practice
- Used a while loop to continue the game until completion
- Stored correct guesses in a list to preserve progress
- Rebuilt the display each turn without losing previous matches
- Used "_" in display as the condition for continuing the loop
- Triggered win condition once all blanks were filled

--------------------------------------------------------

## Part 04 – Hangman Step 4 (Lives & Stages)

### What I Learned in Practice
- Added a lives counter starting at 6
- Decreased lives when guess was not in the word
- Ended game when lives reached zero (lose condition)
- Printed ASCII hangman stages using stages[lives]
- Combined win and lose conditions in the main loop

--------------------------------------------------------

## Day 07 – Hangman Game

### Part 05 – Hangman Final (Modules & Game Improvements)

### What I Learned in Practice
- Imported data from external Python modules
- Used `word_list` from `hangman_words.py`
- Used ASCII art stages from `hangman_art.py`
- Printed game logo at the start of the program
- Implemented tracking of guessed letters
- Prevented life deduction on repeated guesses
- Added feedback when a guessed letter is not in the word
- Displayed remaining lives after each guess
- Revealed the correct word when the player loses
- Completed a fully playable command-line Hangman game