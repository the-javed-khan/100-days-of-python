"""
Day 03 - Part 02
Lesson: Modulo Operator (%)

Objective:
Understand how the modulo operator works and
use it with conditional logic to determine if a number is odd or even.
"""

# =========================
# --- Lesson Theory Practice ---
# =========================

# Modulo gives remainder after division

print(6 % 2)  # 0
print(6 % 5)  # 1
print(6 % 4)  # 2


"""
PAUSE 1:

What is 10 % 3?
"""

print(10 % 3)  # 1


"""
Explanation:
10 divided by 3 = 3 remainder 1
So the output is 1.
"""


# =========================
# --- Lesson Application ---
# =========================

"""
PAUSE 2 – Check Odd or Even

Write code to:
- Take user input
- Convert it to int
- Use modulo to check if divisible by 2
- Print "Even" if remainder is 0
- Otherwise print "Odd"

Hint:
1. Use input()
2. Convert to int()
3. Store in variable
4. Use number % 2
5. Use if/else
"""

# --- Starter Code ---
# number = input("Enter a number: ")
# number = int(number)

# --- Final Solution ---
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")