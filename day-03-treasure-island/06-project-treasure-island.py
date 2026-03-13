"""
Day 03 - Part 06
Project: Treasure Island

Objective:
Build a simple text-based adventure game using
nested if/elif/else statements and logical flow control.
"""

# =========================
# --- Problem Description ---
# =========================

"""
Your goal today is to build a "Choose your own adventure game".
Using what you have learnt in the lessons today you will be
building a very simple version of this type of text game.

Use the flow chart to create the game logic.

You can use the lower() function to turn any string into all lower case.
"""

# =========================
# --- Project Code ---
# =========================

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input(
    "You're at a crossroad. Where do you want to go? Type 'left' or 'right': "
).lower()

if direction == "left":
    action = input(
        "You've come to a lake. There is an island in the middle of the lake. "
        "Type 'wait' to wait for a boat. Type 'swim' to swim across: "
    ).lower()

    if action == "wait":
        door = input(
            "You arrive at the island unharmed. There is a house with 3 doors. "
            "One red, one yellow and one blue. Which colour do you choose? "
        ).lower()

        if door == "yellow":
            print("You found the treasure! You Win!")
        elif door == "red":
            print("It's a room full of fire. Game Over.")
        elif door == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")

    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")