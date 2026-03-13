"""
Day 03 - Part 05
Lesson: Logical Operators

Objective:
Learn how to combine multiple conditions using
and, or, and not operators.
"""

# =========================
# --- Lesson Theory ---
# =========================

"""
Logical Operators:

and  → Both conditions must be True
or   → At least one condition must be True
not  → Reverses the condition
"""

# Example demonstrations

print(True and True)    # True
print(True and False)   # False
print(False or True)    # True
print(not True)         # False


# =========================
# --- Lesson Application ---
# =========================

"""
Update rollercoaster program so that people age 45 to 55 (inclusive)
ride for free.
"""

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    if 45 <= age <= 55:
        print(f"You can ride for free. Your bill is ${bill}")
    elif age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N: ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
    

# =========================
# --- Quiz Section ---
# =========================

"""
Quiz – Question 1:

What will the following code evaluate to?

not 5 == 5

Options:
A) True
B) False

Correct Answer: B) False

Explanation:
5 == 5 → True
not True → False
"""


"""
Quiz – Question 2:

What will the following code evaluate to?

False or True or False

Options:
A) True
B) False
C) Syntax Error

Correct Answer: A) True

Explanation:
The or operator returns True if at least one value is True.
"""


"""
Quiz – Question 3:

What will the following code print?

a = 5
b = 7

if a >= b and a != b:
    print("A")
elif not a >= b and a != b:
    print("B")
else:
    print("C")

Options:
A) A
B) B
C) C

Correct Answer: B) B

Explanation:
a >= b → False
a != b → True
First condition → False
Second condition → True
So it prints "B"
"""