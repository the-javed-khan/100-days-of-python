"""
Day 06 - Part 01
Lesson: Functions & Indentation

Objective:
Understand how to define and call functions,
use proper indentation, and apply functions
to reduce repeated code.
"""

# ==================================================
# --- Lesson Theory Summary ---
# ==================================================

"""
A function is a named block of reusable code.

Defining a Function:
def function_name():
    # indented block

Calling a Function:
function_name()

Important:
- Defining a function does NOT execute it.
- The function must be called.
- Indentation defines what belongs to the function.
"""


# ==================================================
# --- Hurdle Challenge (Reeborg's World) ---
# ==================================================

"""
Goal:
Use functions and loops to help Reeborg jump
over multiple hurdles without repeating code.
"""


# --- Helper Function ---

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# --- Main Function ---

# def pass_hurdle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()


# --- Repeat Hurdle Passing ---

# for ph in range(6):
#     pass_hurdle()


# ==================================================
# --- Quiz Section ---
# ==================================================

"""
Quiz – Question 1:

Which version of code will produce an Indentation Error?

Correct Answer:

def my_function():
print("Hello")

Explanation:
After defining a function using `def`, Python expects
an indented block. If the next line is not indented,
an IndentationError is raised.
"""


"""
Quiz – Question 2:

Which version of code will output "This will run"?

Correct Answer:

def my_function():
    print("This will run")

my_function()

Explanation:
Defining a function does NOT execute it.
The function must be explicitly called.
Only when my_function() is called will the code run.
"""


"""
Quiz – Question 3:

In which version of code will you see "This will run" printed?

Correct Answer:

def my_function():
    a = 3
    if a > 2:
        print("This will run")

my_function()

Explanation:
- The variable must be inside the function block.
- The if statement must be indented correctly.
- The print statement must be indented inside the if block.
- The function must be called.

Proper indentation defines execution hierarchy.
"""