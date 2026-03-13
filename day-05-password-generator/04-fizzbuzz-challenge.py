"""
Day 05 - Part 04
Challenge: FizzBuzz

Objective:
Use loops, conditionals, and modulo operations
to recreate the FizzBuzz game logic.
"""

# =========================
# --- Problem Statement ---
# =========================

"""
You are going to write a program that automatically prints the solution
to the FizzBuzz game.

Rules:
- Print numbers from 1 to 100 (inclusive).
- If number is divisible by 3 → print "Fizz"
- If number is divisible by 5 → print "Buzz"
- If number is divisible by both 3 and 5 → print "FizzBuzz"
- Otherwise print the number itself.

Example output start:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...
"""

# =========================
# --- Final Solution ---
# =========================

for num in range(1, 101):
    if (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)