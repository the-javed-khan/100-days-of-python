"""
Day 09 - Part 02
Lesson: Nested Data Structures (Lists & Dictionaries)

Objective:
Understand how to nest lists inside dictionaries,
lists inside lists, and dictionaries inside dictionaries.
Learn how to access deeply nested values.
"""

# =========================
# --- Lesson Practice (Your Code) ---
# =========================

# --- Nested List inside Dictionary ---
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])  # Lille


# --- Nested List inside List ---
nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])  # D


# --- Nested Dictionary inside Dictionary ---
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])  # Stuttgart


# =========================
# --- Quiz Section ---
# =========================

"""
Question 1:

Which line of code will change the starting_dictionary to the final_dictionary?

starting_dictionary = {
    "a": 9,
    "b": 8,
}

final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

Options:

1)
final_dictionary = starting_dictionary.append({"c": 7})

2)
final_dictionary = starting_dictionary += {"c": 7}

3)
final_dictionary = starting_dictionary["c"]: 7

4)
final_dictionary = starting_dictionary["c"] = 7

5)
starting_dictionary["c"] = 7
final_dictionary = starting_dictionary

Correct Answer:
Option 5

Explanation:
Dictionaries are updated using key assignment:
dict[key] = value
"""


"""
Question 2:

Which line of code will produce an error?

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

Options:

1)
dict["c"] = [1, 2, 3]

2)
for key in dict:
    dict[key] += 1

3)
dict[1] = 4

4)
print(dict[1])

Correct Answer:
Option 4

Explanation:
Dictionaries use keys, not index positions.
Accessing dict[1] raises a KeyError.
"""


"""
Question 3:

Which line of code will print "Steak"?

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

Options:

1)
print(order["main"][2])

2)
print(order["dessert" - 1][2][0])

3)
print(order[main][2][0])

4)
print(order["main"][2][0])

5)
print(order["main"][1][0])

Correct Answer:
Option 4

Explanation:
order["main"] → dictionary
[2] → ["Steak"]
[0] → "Steak"
"""