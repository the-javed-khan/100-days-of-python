"""
Day 04 - Part 03
Lesson: Banker Roulette

Objective:
Use random indexing to select a random
item from a list.
"""

# =========================
# --- Problem Statement ---
# =========================

"""
Figure out how to pick a random name from the list of friends.
"""

# =========================
# --- Starter Data ---
# =========================

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# =========================
# --- Final Solution ---
# =========================

rand_int = random.randint(0, 4)
print(friends[rand_int])

#--------------------------------------------------------------#
## Better approach:
random.randint(0, len(friends) - 1)

##Why?
## If list size changes, your code still works.

##Even cleaner:
print(random.choice(friends))

#That is the most Pythonic way.