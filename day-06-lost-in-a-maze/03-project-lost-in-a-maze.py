"""
Day 06 - Final Project
Project: Lost in a Maze

Objective:
Use while loop and if/elif/else logic
to help Reeborg escape a maze.

Strategy:
Follow the right wall:
- If right is clear → turn right and move
- Else if front is clear → move forward
- Else → turn left

Instructor Note:
Revisit this problem after completing Day 15
to improve logic structure and elegance.
"""

# ==================================================
# --- Helper Function ---
# ==================================================

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# ==================================================
# --- Maze Logic (Right-Hand Rule) ---
# ==================================================

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()