"""
Day 08 - Part 02
Lesson: Positional vs Keyword Arguments (Multiple Inputs)

Objective:
Understand how functions can accept multiple inputs.
Learn the difference between positional arguments and keyword arguments.

Exercise:
Create a function greet_with(name, location) that prints:

Hello <name>
What is it like in <location>?

Then call the function using:
1. Positional arguments
2. Keyword arguments
"""

# =========================
# --- Lesson Theory Practice ---
# =========================

# Function with multiple inputs
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


# Calling using positional arguments
greet_with("Angela", "London")


# Example demonstrating positional order
def my_function(a, b):
    print(a)
    print(b)

my_function(2, 1)


# =========================
# --- Lesson Application ---
# =========================

"""
Calling the function using keyword arguments
This allows specifying which value belongs to which parameter.
"""

greet_with(location="London", name="Angela")