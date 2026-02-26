"""
Day 04 - Part 04
Lesson: IndexError and Nested Lists

Objective:
Understand how to use len() to prevent IndexError
and learn how nested (2D) lists work.
"""

# =========================
# --- Lesson Theory Practice ---
# =========================

states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
    "Virginia", "New York", "North Carolina", "Rhode Island",
    "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana",
    "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
    "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
    "Iowa", "Wisconsin", "California", "Minnesota", "Oregon",
    "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
    "North Dakota", "South Dakota", "Montana", "Washington",
    "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico",
    "Arizona", "Alaska", "Hawaii"
]

# IndexError example (out of range)
# print(states_of_america[len(states_of_america)])

# Correct way to access last element
print(states_of_america[len(states_of_america) - 1])

# Another IndexError example
fruits = ["Cherry", "Apple", "Pear"]
# print(fruits[3])

# Corrected
print(fruits[2])


# =========================
# --- Nested Lists ---
# =========================

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)


# =========================
# --- Quiz Section ---
# =========================

"""
Quiz – Question 1:

Given:
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]

Which line of code will give you "Apples"?

Options:
A) fruits[3]
B) fruits[4]
C) fruits.Apples()
D) fruits[-5]
E) fruits[-4]

Correct Answer: D

Explanation:
Index 2 gives "Apples".
Using negative indexing, fruits[-5] also refers to index 2.
"""


"""
Quiz – Question 2:

Given:

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)

Options:
A) ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Lemons"]
B) ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Lemons"]
C) ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Melons", "Lemons"]

Correct Answer: C

Explanation:
fruits[-1] replaces the last element ("Pears") with "Melons".
append() adds "Lemons" at the end.
"""


"""
Quiz – Question 3:

Given:

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])

Options:
A) "Spinach"
B) "Strawberries"
C) "Kale"
D) ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
E) "Nectarines"

Correct Answer: C

Explanation:
dirty_dozen[1] → vegetables list
dirty_dozen[1][1] → second element of vegetables → "Kale"
"""