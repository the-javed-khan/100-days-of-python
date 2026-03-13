"""
Day 05 - Part 01
Lesson: For Loops

Objective:
Understand how to use for loops to iterate over lists
and how indentation controls execution flow.
"""

# =========================
# --- Lesson Theory Practice ---
# =========================

fruits = ["Apple", "Peach", "Pear"]

# Basic loop
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")


# =========================
# --- Indentation Behavior ---
# =========================

# Example 1: Both lines inside loop
for fruit in fruits:
    print(fruit)
    print("Hello")


# Example 2: Second line outside loop
for fruit in fruits:
    print(fruit)
print("Hello")