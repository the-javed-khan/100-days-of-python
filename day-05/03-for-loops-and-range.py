"""
Day 05 - Part 03
Challenge: The Gauss Challenge

Objective:
Use range() and a for loop to calculate
the total sum of numbers from 1 to 100.
"""

# =========================
# --- Problem Statement ---
# =========================

"""
Work out the total of the numbers between 1 and 100,
inclusive of both 1 and 100.
"""

# =========================
# --- Final Solution ---
# =========================

total = 0

for value in range(1, 101):
    total += value

print(total)