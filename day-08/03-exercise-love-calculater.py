"""
Day 08 - Part 03
Lesson: Love Calculator

Objective:
Practice functions with multiple inputs and string manipulation
by calculating a compatibility score based on letter counts.
"""

# =========================
# --- Lesson Theory Practice ---
# =========================

# String methods used:
# .lower()
# .count()


# =========================
# --- Lesson Application ---
# =========================

def calculate_love_score(name1, name2):
    names = (name1 + name2).lower()

    true_count = (
        names.count("t") +
        names.count("r") +
        names.count("u") +
        names.count("e")
    )

    love_count = (
        names.count("l") +
        names.count("o") +
        names.count("v") +
        names.count("e")
    )

    final_score = str(true_count) + str(love_count)

    print(final_score)

calculate_love_score("Kanye West", "Kim Kardashian")