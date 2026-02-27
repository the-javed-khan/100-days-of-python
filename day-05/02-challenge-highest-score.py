"""
Day 05 - Part 02
Challenge: Highest Score

Objective:
Recreate the functionality of Python's max() function
using loops and conditionals.
"""

# =========================
# --- Problem Statement ---
# =========================

"""
You are given a list of exam scores, and you have to print out
the highest score from the list of student_scores.

Complete this challenge WITHOUT using max().

Example:
8 65 89 86 55 91 64 89

Output:
91
"""

# =========================
# --- Starter Data ---
# =========================

student_scores = [150, 142, 185, 120, 171, 184, 149,
                  24, 59, 68, 199, 78, 65, 89, 86,
                  55, 91, 64, 89]

# =========================
# --- Final Solution ---
# =========================

highest = student_scores[0]

for score in student_scores:
    if highest < score:
        highest = score

print(f"Highest is: {highest}")