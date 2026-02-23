"""
Day 02 - Part 02
Lesson: TypeError, Type Checking, Type Conversion

Objective:
- Understand TypeError caused by using the wrong data type (e.g., len(12345)).
- Use type() to check the data type of values/variables.
- Use type conversion functions: str(), int(), float().
"""

# =========================
# --- Lesson Code ---
# =========================

# TypeError example (commented to avoid crashing the file)
# len(12345)  # TypeError: object of type 'int' has no len()

# Correct usage of len() with a string
len("Hello")

# Type checking examples
print(type("Hello"))
print(type(123))
print(type(3.1416))
print(type(True))


"""
Task:

PAUSE 1:
Fix the len() function so it has no more warnings or errors.

PAUSE 2:
Write out 4 type checks to print all 4 data types:
<class 'str'> <class 'int'> <class 'float'> <class 'bool'>

PAUSE 3:
Make this line of code run without errors:
print("Number of letters in your name: " + len(input("Enter your name")))
"""

# =========================
# --- Task Problem (Starter Code) ---
# =========================

# PAUSE 1 (problem example)
# len(12345)

# PAUSE 2 (starter - write the type checks)
# print(type("abc"))
# print(type(123))
# print(type(3.1416))
# print(type(True))

# PAUSE 3 (problem line)
# print("Number of letters in your name: " + len(input("Enter your name")))


# =========================
# --- Task Solution ---
# =========================

# PAUSE 1 solution
len("Hello")

# PAUSE 2 solution
print(type("Hello"))
print(type(123))
print(type(3.1416))
print(type(True))

# PAUSE 3 solution
print("Number of letters in your name: " + str(len(input("Enter your name"))))