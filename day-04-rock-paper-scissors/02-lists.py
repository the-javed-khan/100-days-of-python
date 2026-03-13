"""
Day 04 - Part 02
Lesson: Lists

Objective:
Understand how to create, access, modify,
and add items to Python lists.
"""

# =========================
# --- Lesson Theory Practice ---
# =========================

# Creating a list
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

# Accessing items (index starts from 0)
print(states_of_america[0])

# =========================
# --- Negative Index ---
# =========================

fruits = ["Cherry", "Apple", "Pear"]
print(fruits[-2])

# =========================
# --- Modifying Items ---
# =========================

fruits[0] = "Banana"
print(fruits)

# =========================
# --- Adding Items ---
# =========================

fruits.append("Orange")
print(fruits)