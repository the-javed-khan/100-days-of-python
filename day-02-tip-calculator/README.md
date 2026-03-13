# Day 02 – Data Types & Type Conversion

---------------------------------------------------------------------------

## Task 01 – Data Types & Indexing

### Description
Learn about primitive data types in Python:
- String
- Integer
- Float
- Boolean
Also understand string indexing (subscript).

### What I Fixed / Learned in Practice
- Strings are enclosed in quotes.
- Indexing starts at 0.
- Negative indexing accesses characters from the end.
- Spaces count as characters in indexing.
- "123" is a string, but 123 is an integer.
- Underscores in numbers improve readability but don’t change the data type.
- Decimal numbers are floats.
- "False" (with quotes) is a string, not a Boolean.
- Booleans must be written without quotes: True, False.

---------------------------------------------------------------------------

## Task 02 – TypeError, type(), and Type Conversion

### Description
Understand why TypeError occurs and how to fix it.
Learn how to check data types and convert between them.

### What I Fixed / Learned in Practice
- `len()` only works on strings (not integers).
- Passing an integer to `len()` causes TypeError.
- `type()` shows the data type of any value.
- `input()` always returns a string.
- `len()` returns an integer.
- You cannot concatenate string + integer directly.
- Use `str()` to convert integer to string.
- Python does not automatically convert data types during concatenation.

---------------------------------------------------------------------------

## Part 03 – Mathematical Operations & BMI

### What I Fixed / Learned in Practice
- `/` always returns a float.
- `**` is the exponent operator.
- PEMDAS controls operation order.
- Parentheses override default precedence.
- Translating a real-world formula into code requires correct operator placement.
- Division result type affects final output.

---------------------------------------------------------------------------

## Part 04 – Number Manipulation & f-Strings

### What I Fixed / Learned in Practice
- `int()` floors (truncates) decimals.
- `round()` performs mathematical rounding.
- `round(x, n)` controls precision.
- `+=`, `-=`, `*=`, `/=` modify variables in place.
- `/` vs `//` behave differently.
- f-strings automatically handle type conversion.
- f-strings are cleaner than string + str(variable).
- Mixing string + int without conversion causes TypeError.

---------------------------------------------------------------------------

## Part 05 – Tip Calculator Project

### What I Fixed / Learned in Practice
- Converted user input using float() and int().
- Used percentage calculation: 1 + tip/100.
- Applied operator precedence correctly.
- Used round() for formatting.
- Used f-string formatting with :.2f.
- Understood why financial output must be formatted.