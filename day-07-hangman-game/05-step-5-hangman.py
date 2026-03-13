import random

from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

# TODO-3: print the logo at the start
print(logo)

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []  # track ALL guesses (correct + wrong)

while not game_over:

    # TODO-6: show lives left
    print(f"****************************{lives}/6 LIVES LEFT****************************")

    guess = input("Guess a letter: ").lower()

    # TODO-4: if user already guessed this letter, tell them and do NOT deduct a life
    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
        print(stages[lives])
        continue
    else:
        guessed_letters.append(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO-5: wrong guess feedback + reduce life
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            # TODO-7: reveal correct word
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    # win condition
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: print stage based on lives
    print(stages[lives])