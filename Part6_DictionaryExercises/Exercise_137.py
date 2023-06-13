"""
Exercise 137: Scrabble™ Score

    In the game of Scrabble™, each letter has points associated with it. The total score
    of a word is the sum of the scores of its letters. More common letters are worth fewer
    points while less common letters are worth more points. The points associated with
    each letter are shown below:

            One point       A, E, I, L, N, O, R, S, T and U
            Two points      D and G
            Three points    B, C, M and P
            Four points     F, H, V, W and Y
            Five points     K
            Eight points    J and X
            Ten points      Q and Z

    Write a program that computes and displays the Scrabble™ score for a word.
    Create a dictionary that maps from letters to point values. Then use the dictionary to
    compute the score.
    A Scrabble™ board includes some squares that multiply the value of a letter
    or the value of an entire word. We will ignore these squares in this exercise.
"""


def calculate_scrabble_score(word):
    letter_values = {
        "A": 1, "E": 1, "I": 1, "L": 1, "N": 1, "O": 1, "R": 1, "S": 1, "T": 1, "U": 1,
        "D": 2, "G": 2,
        "B": 3, "C": 3, "M": 3, "P": 3,
        "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
        "K": 5,
        "J": 8, "X": 8,
        "Q": 10, "Z": 10
    }

    score = 0

    # Calculate the score for each letter in the word
    for letter in word.upper():
        score += letter_values.get(letter, 0)

    return score


# Example usage
word = input("Enter a word: ")
score = calculate_scrabble_score(word)
print("Scrabble score:", score)
