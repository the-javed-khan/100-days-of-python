"""
Day 01 - Part 05
Mini Project: Band Name Generator

Project Objective:
Create a program that:
1. Greets the user.
2. Asks for the city they grew up in.
3. Asks for the name of a pet.
4. Combines both inputs to generate a band name.
"""

# --- Project Requirements (As Given) ---
# 1. Create a greeting for your program.
# 2. Ask the user for the city that they grew up in and store it in a variable.
# 3. Ask the user for the name of a pet and store it in a variable.
# 4. Combine the name of their city and pet and show them their band name.

# --- Final Solution ---

print("Welcome to the Band Name Generator!")

city_name = input("What is the name of the city you grew up in?\n")
pet_name = input("What is your pet's name?\n")

print("Your band name could be: " + city_name + " " + pet_name)