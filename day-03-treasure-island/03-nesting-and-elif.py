"""
Day 03 - Part 03
Lesson: Nesting and Elif

Objective:
Understand nested if statements and use elif
to create clean multi-branch decision logic.
"""

# =========================
# --- Lesson Theory Practice ---
# =========================

"""
Example: Rollercoaster with age-based pricing
"""

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))

    if age <= 12:
        print("Please pay $12")
    elif age <= 18:
        print("Please pay $18")
    else:
        print("Please pay $25")
else:
    print("Sorry you have to grow taller before you can ride.")


"""
Key Concepts Covered:

1. Nested if:
   An if statement inside another if block.

2. elif:
   Used when checking multiple conditions in sequence.

3. Order matters:
   Conditions are evaluated top to bottom.

4. Cleaner logic:
   Use elif instead of multiple independent if statements
   when conditions are mutually exclusive.
"""

# =========================
# --- Lesson Application ---
# =========================

"""
Exercise: BMI Calculator with Interpretations

If bmi < 18.5 → print "underweight"
If 18.5 <= bmi < 25 → print "normal weight"
If bmi >= 25 → print "overweight"
"""

# --- Starter Code (Given) ---
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# --- Final Solution ---
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")