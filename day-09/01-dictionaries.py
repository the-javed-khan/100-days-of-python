"""
Day 09 - Part 01
Lesson: Dictionaries in Python

Objective:
Understand how dictionaries store data using key-value pairs.
Learn how to create, retrieve, update, and loop through dictionaries.
Apply the concept to a grading program exercise.
"""

# =========================
# --- Lesson Practice ---
# =========================

# Creating a dictionary
colours = {
    "apple": "red",
    "pear": "green",
    "banana": "yellow"
}

# Retrieving a value using a key
print(colours["pear"])  # Output: green


# =========================
# --- Creating an Empty Dictionary ---
# =========================

my_empty_dictionary = {}

print(my_empty_dictionary)


# =========================
# --- Adding a New Item ---
# =========================

colours["peach"] = "pink"

print(colours)


# =========================
# --- Updating Existing Value ---
# =========================

colours["apple"] = "green"

print(colours)


# =========================
# --- Looping Through Keys ---
# =========================

for key in colours:
    print(key)


# =========================
# --- Looping Through Values ---
# =========================

for key in colours:
    print(colours[key])


# ==================================================
# --- Exercise: Grading Program ---
# ==================================================

"""
You have access to a database of student_scores.

Write a program that converts student exam scores into grades.

Scoring Criteria:
91 - 100 → Outstanding
81 - 90  → Exceeds Expectations
71 - 80  → Acceptable
70 or lower → Fail

Create a new dictionary called student_grades where:
Keys = student names
Values = grade description
"""

# --- Given Dictionary ---
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


# =======================
# --- Solution ---
# =======================

student_grades = {}

for student in student_scores:
    score = student_scores[student]

    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


print(student_grades)