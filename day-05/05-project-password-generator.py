"""
Day 05 - Part 05
Project: Password Generator

Objective:
Build a random password generator using loops,
lists, and the random module.
"""

# =========================
# --- Problem Statement ---
# =========================

"""
The program will ask:
How many letters would you like in your password?
How many symbols would you like?
How many numbers would you like?

The objective is to take the inputs from the user and generate
a random password.

Easy Version:
Generate the password in sequence:
Letters → Symbols → Numbers

Hard Version:
Generate the password with all characters shuffled
so there is no predictable pattern.
"""

# =========================
# --- Setup ---
# =========================

import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

# =========================
# --- Easy Version ---
# =========================

picked_letter = ""
for n_letter in range(1, nr_letters + 1):
    picked_letter += random.choice(letters)

picked_number = ""
for n_number in range(1, nr_numbers + 1):
    picked_number += random.choice(numbers)

picked_symbol = ""
for n_symbol in range(1, nr_symbols + 1):
    picked_symbol += random.choice(symbols)

easy_password = picked_letter + picked_symbol + picked_number

print("Easy password:", easy_password)


# =========================
# --- Hard Version ---
# =========================

password_list = []

for n_letter in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for n_number in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

for n_symbol in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print("Hard password:", password)