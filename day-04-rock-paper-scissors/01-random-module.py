"""
Day 04 - Part 01
Lesson: Random Module & Pseudorandom Number Generators

Objective:
Understand how to generate random numbers in Python
using the random module.
"""

# =========================
# --- Lesson Theory Practice ---
# =========================

import random

# Random whole number between 1 and 10 (inclusive)
# rand_number = random.randint(1, 10)
# print(rand_number)

# Accessing variable from custom module
# print(my_module.name)

# Random float between 0.0 and 1.0 (not inclusive of 1.0)
# rand_num_0_to_1 = random.random() * 10
# print(rand_num_0_to_1)

# Random float between 1 and 10
# random_float = random.uniform(1, 10)
# print(random_float)


# =========================
# --- Lesson Application ---
# =========================

"""
PAUSE 1 – Heads or Tails

Create a coin flip program.
It should randomly print "Heads" or "Tails"
every time it is run.
"""

# --- Final Solution ---

random_1_or_2 = random.randint(1, 2)

if random_1_or_2 == 1:
    print("Heads")
else:
    print("Tails")