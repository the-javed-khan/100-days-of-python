"""
Day 02 - Part 03
Lesson: Mathematical Operations

Objective:
Learn to use mathematical operators in Python:
+, -, *, /, //, %, **
Understand operator precedence (PEMDAS).
"""

# =========================
# --- Lesson Practice ---
# =========================

print("My age: " + str(12))

# Basic Operations
print(123 + 456)   # Addition
print(100 - 50)    # Subtraction
print(6 * 3)       # Multiplication
print(10 / 5)      # Division (returns float)
print(10 // 3)     # Floor Division (returns integer)
print(10 % 3)      # Modulo (returns remainder)
print(2 ** 3)      # Exponentiation (2 to the power of 3)

# ====================================================================================
# --- PEMDAS --- Parebtheses, Exponents, Multiplication/Division, Addition/Subtraction 
# ====================================================================================

print(3 * 3 + 3 / 3 - 3)          # Output: 7
print(3 * (3 + 3) / 3 - 3)        # Output: 3


# =========================
# --- Exercise: BMI Calculator ---
# =========================

"""
BMI Calculator
The body mass index (BMI) is calculated as:
bmi = weight / (height ** 2)
Convert this formula into code.
"""

# --- Starter Code ---
height = 1.65
weight = 84

# --- Solution ---
bmi = weight / (height ** 2)

print(bmi)