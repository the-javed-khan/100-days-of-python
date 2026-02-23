"""
Day 01 - Part 04
Lesson: Variables

Original Lesson Objective:
Learn to store values in variables and use them later in the program.
Understand how to use the len() function to calculate the length of input.
"""

# --- Lesson Code ---
username = input("What is your name? ")
length = len(username)
print(length)


"""
Task 1:

PAUSE 1:
Check the length of the user input.
Write everything in just 1 line of code.

PAUSE 2:
Split everything into variables.
Create one variable called 'username'
and one variable called 'length'.
Use the variable username in the len() calculation.
"""

# --- Task 1 Problem (Starter Code) ---
# print(len(input("What is your name?")))


# --- Task 1 Solution ---

# One-line version
print(len(input("What is your name? ")))

# Using variables
username = input("What is your name? ")
length = len(username)
print(length)


"""
Task 2 – Coding Challenge (Variable Swapping)

We have 2 variables:
glass1 contains milk
glass2 contains juice

Write 3 lines of code to switch the contents of the variables.
You are NOT allowed to type the words "milk" or "juice".
You must use variables only.
"""

# --- Task 2 Problem (Starter Code) ---
glass1 = "milk"
glass2 = "juice"

# --- Task 2 Solution ---

swap = glass1
glass1 = glass2
glass2 = swap

"""
Lesson Extension: Variable Naming Rules

Rules:
1. Variable names must be descriptive.
2. No spaces between words.
3. Cannot start with numbers.
4. Cannot use Python keywords (e.g., print, input).
5. Keep names simple and clear.
"""

# --- Valid Variable Naming Example ---
name = "Angela"
length_of_name = len(name)
print(length_of_name)

# --- Invalid Examples (Commented) ---
# 1name = "Angela"       # Cannot start with a number
# my name = "Angela"     # Cannot contain spaces
# print = "Angela"       # Cannot use reserved keyword