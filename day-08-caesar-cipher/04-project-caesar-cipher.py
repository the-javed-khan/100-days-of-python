"""
Day 08 - Part 04
Lesson: Caesar Cipher

Objective:
Build an encryption and decryption program using the Caesar Cipher.

Project Progression Covered:
- Create an encrypt() function that shifts letters forward.
- Fix overflow when shifting past 'z'.
- Create a decrypt() function that shifts letters backward.
- Combine both encrypt and decrypt logic into one caesar() function.
- Import and print the logo from art.py.
- Preserve numbers, symbols, and spaces without modifying them.
- Allow the user to restart the program using a loop.
"""

# =============================
# --- Lesson Theory Practice ---
# =============================

# TODO-1:
# Import and print the logo from art.py when the program starts.
from art import logo

print(logo)

# Alphabet list used in the Caesar Cipher project.
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Project theory notes:
# 1. Encryption shifts each letter forward in the alphabet.
# 2. Decryption shifts each letter backward in the alphabet.
# 3. Modulo (%) prevents index errors when shifting beyond the alphabet range.
# 4. Non-alphabet characters should remain unchanged.
# 5. A while loop allows the program to restart until the user chooses to stop.


# =========================
# --- Lesson Application ---
# =========================

# TODO-1:
# Create a function called caesar() that takes original_text,
# shift_amount, and encode_decode as inputs.

# TODO-2:
# If the direction is "encode", shift letters forward.
# If the direction is "decode", shift letters backward.

# TODO-3:
# Keep numbers, symbols, and spaces unchanged.

# TODO-4:
# Allow the user to restart the cipher program.

def caesar(original_text, shift_amount, encode_decode):
    output_text = ""

    # For decoding, reverse the shift direction.
    if encode_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        # Keep spaces, symbols, and numbers unchanged.
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount

            # Wrap around the alphabet using modulo.
            shifted_position %= len(alphabet)

            output_text += alphabet[shifted_position]

    print(f"Here is the {encode_decode}d result: {output_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Normalize large shift values to stay within alphabet bounds
    shift = shift % 26

    caesar(original_text=text, shift_amount=shift, encode_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

    if restart == "no":
        should_continue = False
        print("Goodbye!")
