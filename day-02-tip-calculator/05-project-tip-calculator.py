"""
Day 02 - Part 05
Project: Tip Calculator

Project Objective:
Build a tip calculator that:
1. Asks for the total bill.
2. Asks what percentage tip to give (10, 12, 15, etc.).
3. Asks how many people to split the bill between.
4. Calculates how much each person should pay.
5. Formats the result to 2 decimal places.
"""

# =========================
# --- Project Requirements ---
# =========================
# If the bill was $150.00, split between 5 people, with 12% tip:
#
# (150.00 / 5) * 1.12 = 33.6
# After formatting to 2 decimal places = 33.60


# =========================
# --- Starter Code (Given) ---
# =========================

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


# =========================
# --- Your Solution ---
# =========================

each_person = bill * (1 + tip / 100) / people

# Formatting to 2 decimal places
final_amount = round(each_person, 2)

print(f"Each person should pay: {final_amount}")