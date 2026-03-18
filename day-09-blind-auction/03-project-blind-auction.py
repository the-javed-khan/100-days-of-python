"""
Day 09 - Part 03
Project: Blind Auction

Project Objective:
Build a blind auction program that:
1. Collects each bidder's name and bid.
2. Stores all bids in a dictionary.
3. Repeats until no more bidders remain.
4. Clears the screen between bidders.
5. Finds and prints the highest bidder.
"""

# =========================
# --- Project Requirements ---
# =========================

# 1. Ask the user for input
# 2. Save data into dictionary {name: price}
# 3. Check whether new bids need to be added
# 4. Compare bids in dictionary and find the winner

from art import logo

print(logo)


# =========================
# --- Solution ---
# =========================

def find_highest_bidder(all_bids):
    highest_bid = 0
    winner = ""

    for bidder in all_bids:
        bid_amount = all_bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
should_continue = True

while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if more_bidders == "yes":
        print("\n" * 25)
    else:
        should_continue = False
        find_highest_bidder(bids)