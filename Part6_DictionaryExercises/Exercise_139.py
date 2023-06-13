"""
Exercise 139: Checking for a Winning Card

    A winning Bingo card contains a line of 5 numbers that have all been called. Players
    normally mark the numbers that have been called by crossing them out or marking
    them with a Bingo dauber. In our implementation we will mark that a number has
    been called by replacing it with a 0 in the Bingo card dictionary.
    Write a function that takes a dictionary representing a Bingo card as its only
    parameter. If the card contains a line of five zeros (vertical, horizontal or diagonal)
    then your function should return True, indicating that the card has won. Otherwise
    the function should return False.
    Create a main program that demonstrates your function by creating several Bingo
    cards, displaying them, and indicating whether or not they contain a winning line.
    You should demonstrate your function with at least one card with a horizontal line,
    at least one card with a vertical line, at least one card with a diagonal line, and at
    least one card that has some numbers crossed out but does not contain a winning line.
    You will probably want to import your solution to Exercise 138 when completing
    this exercise.
    Hint: Because there are no negative numbers on a Bingo card, finding a line
    of 5 zeros is the same problem as finding a line of 5 entries that sum to zero.
    You may find the summation problem easier to solve.
"""


def check_winning_card(card):
    # Check horizontal lines
    for row in card.values():
        if sum(row) == 0:
            return True

    # Check vertical lines
    for i in range(5):
        if card['B'][i] + card['I'][i] + card['N'][i] + card['G'][i] + card['O'][i] == 0:
            return True

    # Check diagonal lines
    if card['B'][0] + card['I'][1] + card['N'][2] + card['G'][3] + card['O'][4] == 0:
        return True
    if card['B'][4] + card['I'][3] + card['N'][2] + card['G'][1] + card['O'][0] == 0:
        return True

    return False


# Example usage
card1 = {
    'B': [1, 2, 3, 4, 0],
    'I': [0, 6, 7, 8, 9],
    'N': [10, 11, 0, 13, 14],
    'G': [0, 16, 17, 18, 19],
    'O': [20, 21, 22, 0, 24]
}

card2 = {
    'B': [1, 2, 0, 4, 5],
    'I': [0, 7, 8, 9, 10],
    'N': [11, 0, 13, 14, 15],
    'G': [16, 17, 0, 19, 20],
    'O': [21, 22, 23, 0, 25]
}

print("Card 1:")
for row in card1.values():
    print(row)

print("Is Card 1 a winning card?", check_winning_card(card1))

print()

print("Card 2:")
for row in card2.values():
    print(row)

print("Is Card 2 a winning card?", check_winning_card(card2))
