"""
Day 03 - Part 01
Lesson: Condition Check (if / else)

Objective:
Learn how to use conditional statements to control program flow
based on True / False conditions.
"""

# =========================
# --- Lesson Theory Practice ---
# =========================

# Basic if statement
if 5 > 2:
    print("yes")


# if / else example
if False:
    print("This will never run")
else:
    print("This is real life")


"""
Key Concepts Covered:

1. if statement:
   if <condition>:
       <execute if True>

2. else statement:
   Executes when the if condition is False.

3. Indentation:
   Python uses indentation to define code blocks.
   Indented lines belong to the parent condition.

4. Comparator Operators:
   >   Greater than
   <   Less than
   >=  Greater than or equal to
   <=  Less than or equal to
   ==  Equal to
   !=  Not equal to
"""

# =========================
# --- Lesson Application ---
# =========================

"""
Exercise:

Write a program that:
- Asks the user for their height
- If height >= 120 → allow ride
- Otherwise → deny access
"""

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride")
else:
    print("You can not ride")


