"""
Exercise 140: Play Bingo

    In this exercise you will write a program that simulates a game of Bingo for a single
    card. Begin by generating a list of all of the valid Bingo calls (B1 through O75). Once
    the list has been created you can randomize the order of its elements by calling the
    shuffle function in therandom module. Then your program should consume calls
    out of the list, crossing out numbers on the card, until the card contains a crossed out
    line (horizontal, vertical or diagonal). Simulate 1,000 games and report the minimum,
    maximum and average number of calls that must be made before the card wins. Import
    your solutions to Exercises 138 and 139 when completing this exercise.
"""

import random
from statistics import mean


def create_bingo_card():
    card = {
        'B': random.sample(range(1, 16), 5),
        'I': random.sample(range(16, 31), 5),
        'N': random.sample(range(31, 46), 5),
        'G': random.sample(range(46, 61), 5),
        'O': random.sample(range(61, 76), 5)
    }
    return card


def display_bingo_card(card):
    for letter, numbers in card.items():
        print(f"{letter}: {numbers}")


def check_winning_card(card):
    for row in card.values():
        if sum(row) == 0:
            return True

    for i in range(5):
        if card['B'][i] + card['I'][i] + card['N'][i] + card['G'][i] + card['O'][i] == 0:
            return True

    if card['B'][0] + card['I'][1] + card['N'][2] + card['G'][3] + card['O'][4] == 0:
        return True
    if card['B'][4] + card['I'][3] + card['N'][2] + card['G'][1] + card['O'][0] == 0:
        return True

    return False


def simulate_bingo_game():
    calls = random.sample(range(1, 76), 75)  # Generate a list of all valid Bingo calls
    random.shuffle(calls)  # Randomize the order of the calls

    card = create_bingo_card()
    display_bingo_card(card)

    num_calls = 0
    while not check_winning_card(card):
        call = calls.pop(0)  # Consume the next call
        num_calls += 1

        # Mark the called number as 0 in the card
        for numbers in card.values():
            if call in numbers:
                numbers[numbers.index(call)] = 0

    print("Bingo! Winning Card:")
    display_bingo_card(card)

    return num_calls


# Simulate 1,000 games and track the minimum, maximum, and average number of calls
num_games = 1000
total_calls = 0
min_calls = float('inf')
max_calls = 0

for _ in range(num_games):
    calls = simulate_bingo_game()
    total_calls += calls
    min_calls = min(min_calls, calls)
    max_calls = max(max_calls, calls)

avg_calls = total_calls / num_games

print("\nSimulation Results:")
print(f"Minimum number of calls: {min_calls}")
print(f"Maximum number of calls: {max_calls}")
print(f"Average number of calls: {avg_calls}")
