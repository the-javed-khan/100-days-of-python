"""
Day 02 - Part 01
Lesson: Data Types

Objective:
Learn about primitive data types in Python:
1. Strings
2. Integers
3. Floats
4. Booleans
Understand string indexing (subscript).
"""

# =========================
# --- Lesson Practice ---
# =========================

# --- String & Subscript ---
print("Hello"[4])     # Access character at index 4
print("Hello"[-1])    # Negative indexing (last character)


# --- String Numbers (Still Strings) ---
print("123" + "345")  # Concatenation, not addition


# --- Integers ---
print(123 + 345)      # Integer addition


# --- Large Numbers with Underscore ---
print(123_456_789)    # Underscore improves readability


# --- Float ---
print(3.1416)


# --- Boolean ---
print(True)
print(False)


# =========================
# --- Quiz Section ---
# =========================

"""
Quiz – Question 1:

Which statement below is incorrect?

A) 932 is an Integer
B) "False" is a Boolean
C) 857.25 is a Float
D) "523" is a String
"""

# Correct Answer: B

"""
Explanation:
"False" (with quotes) is a String.
Booleans must not have quotes:
True
False
"""


"""
Quiz – Question 2:

What is the data type of the mystery variable?

mystery = 734_529.678

A) Integer
B) String
C) Qurtle
D) Float
"""

# Correct Answer: D (Float)

"""
Explanation:
734_529.678 contains a decimal point → it is a Float.
The underscore (_) only improves readability.
It does NOT affect the data type.
"""


"""
Quiz – Question 3:

street_name = "Abbey Road"
print(street_name[4] + street_name[7])

What will this print?
"""

# Correct Answer: "yo"

"""
Explanation:

A  b  b  e  y     R  o  a  d
0  1  2  3  4  5  6  7  8  9

street_name[4] → 'y'
street_name[7] → 'o'

'y' + 'o' = "yo"

Indexing starts at 0.
Spaces count as characters.
"""