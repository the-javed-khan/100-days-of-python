"""
Day 06 - Part 02, 03 & 04
Lesson: While Loops & Hurdle Challenges

Objective:
Understand condition-based repetition using while loops
and apply it to increasingly dynamic hurdle environments.
"""

# ==================================================
# --- While Loop Concept ---
# ==================================================

"""
A while loop repeats code as long as a condition is True.

Syntax:

while condition:
    # indented block

Key Difference:
- for loop → used when repetition count is known.
- while loop → used when repetition depends on a condition.

Execution continues until the condition becomes False.
"""


# ==================================================
# --- Helper Function ---
# ==================================================

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# ==================================================
# --- Challenge 1: Hurdle (Unknown Count) ---
# ==================================================

#Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

"""
Instead of repeating a fixed number of times,
repeat until the goal is reached.
"""

# def pass_basic_hurdle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#     pass_basic_hurdle()


# ==================================================
# --- Challenge 2: Dynamic Hurdles ---
# ==================================================
#Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

"""
Hurdle positions change.
We must check before acting.
"""

# def pass_dynamic_hurdle():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         pass_dynamic_hurdle()


# ==================================================
# --- Challenge 3: Variable Height Hurdles ---
# ==================================================
#Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

"""
Hurdle height and position change.
Requires nested while loops.
"""

# def pass_variable_hurdle():
#     turn_left()

#     # climb up
#     while wall_on_right():
#         move()

#     # cross top
#     turn_right()
#     move()
#     turn_right()

#     # descend
#     while front_is_clear():
#         move()

#     turn_left()

# while not at_goal():
#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         pass_variable_hurdle()