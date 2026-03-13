"""
Day 08 - Part 01
Lesson: Functions with Inputs

Objective:
Understand how functions accept inputs using parameters
and how arguments passed during function calls affect behaviour.
Also practice using functions with simple mathematical calculations.

Exercise: Life in Weeks
Inspired by Tim Urban's article "Your Life in Weeks", this exercise calculates
how many weeks a person has left if they live until 90 years old.

The function takes the current age as input and prints how many weeks remain.

Example:
Input: 56
Output: You have 1768 weeks left.
"""

# =========================
# --- Lesson Theory Practice ---
# =========================

# Simple function without inputs
def greet():
    print("Hello!")
    print("How are you?")
    print("Welcome to Python functions!")

greet()


# Function with input parameter
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}?")

greet_with_name("Angela")


# =========================
# --- Lesson Application ---
# =========================

"""
Exercise: Life in Weeks

Create a function called life_in_weeks() that calculates
how many weeks a person has left if they live until 90 years old.

The function takes the current age as input and prints:

You have x weeks left.

Where x is the calculated number of weeks remaining.
"""

def life_in_weeks(age):
    total_years = 90
    years_left = total_years - age
    weeks_left = years_left * 52
    print(f"You have {weeks_left} weeks left.")

# Call the function with a hard coded value
life_in_weeks(56)