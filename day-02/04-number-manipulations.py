"""
Day 02 - Part 04
Lesson: Number Manipulation & f-Strings

Objective:
- Floor numbers using int()
- Round numbers using round()
- Use assignment operators (+=, -=, *=, /=)
- Use f-strings for formatting
- Understand why some operations return float and cause TypeError
"""

# =========================
# --- Lesson Practice ---
# =========================

# Flooring a Number (removes decimals)
print(int(3.738492))  # 3

# Rounding a Number
print(round(3.738492))     # 4
print(round(3.14159))      # 3
print(round(3.14159, 2))   # 3.14

# Assignment Operators
score = 0
score += 1
score *= 2
print(score)

# f-Strings
age = 12
print(f"I am {age} years old")


# =========================
# --- Quiz Section (Full Questions + Options) ---
# =========================

"""
Quiz – Question 1:
You are a computer. What will this line of code print?

print(6 + 4 / 2 - (1 * 2))

Options:
A) 3
B) 6.0
C) 8.0
D) 5

Correct Answer: B) 6.0

Explanation:
(1 * 2) = 2
4 / 2 = 2.0  (division returns float)
6 + 2.0 - 2 = 6.0
"""


"""
Quiz – Question 2:
What is the data type of the result of the variable 'a' in the following line of code?

a = int("5") / int(2.7)

Options:
A) int
B) float
C) str
D) bool

Correct Answer: B) float

Explanation:
int("5") -> 5
int(2.7) -> 2  (int() floors/truncates, does not round)
5 / 2 = 2.5 and / always returns float
"""


"""
Quiz – Question 3:
Which of these lines of code will give you an error?

Options:

A)
name = input("What is your name?")
print(f"Hello, {name}")

B)
name = input("What is your name?")
print("Hello, " + name)

C)
age = 12
print(f"You are {age} years old")

D)
age = 12
print("You are " + age + " years old")

Correct Answer: D)

Explanation:
age is an int, so "You are " + age causes a TypeError (string + int).
Fix with:
print("You are " + str(age) + " years old")
or:
print(f"You are {age} years old")
"""