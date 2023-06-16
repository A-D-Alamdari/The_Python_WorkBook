"""
Exercise 158: Spell Checker

    A spell checker can be a helpful tool for people who struggle to spell words correctly.
    In this exercise, you will write a program that reads a file and displays all of thewords
    in it that are misspelled. Misspelled words will be identified by checking each word
    in the file against a list of known words. Any words in the user’s file that do not
    appear in the list of known words will be reported as spelling mistakes.
    The user will provide the name of the file to check for spelling mistakes as a
    command line parameter. Your program should display an appropriate error message
    if the command line parameter is missing. An error message should also be displayed
    if your program is unable to open the user’s file. Use your solution to Exercise 111
    when creating your solution to this exercise so that words followed by a comma,
    period or other punctuation mark are not reported as spelling mistakes. Ignore the
    capitalization of the words when checking their spelling.

    Hint: While you could load all of the English words from the words data set
    into a list, searching a list is slow if you use Python’s in operator. It is much
    faster to check if a key is present in a dictionary, or if a value is present in a
    set. If you use a dictionary, the words will be the keys. The values can be the
    integer 0 (or any other value) because the values will never be used.
"""

import sys
import string


def load_known_words(filename):
    known_words = set()

    with open(filename, 'r') as file:
        for line in file:
            word = line.strip().lower()
            known_words.add(word)

    return known_words


def check_spelling(filename, known_words):
    misspelled_words = set()

    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()

            for word in words:
                # Remove punctuation marks from the word
                word = word.strip(string.punctuation).lower()

                # Check if the word is in the known_words set
                if word not in known_words:
                    misspelled_words.add(word)

    return misspelled_words


# Check if the filename is provided as a command line argument
if len(sys.argv) < 2:
    print("Error: Please provide a filename as a command line argument.")
    sys.exit(1)

filename = sys.argv[1]  # Get the filename from the command line argument

# Load the known words from the words data set (Exercise 111)
known_words = load_known_words("words.txt")  # Replace with the actual filename

# Check the spelling of words in the given file
misspelled_words = check_spelling(filename, known_words)

# Display the misspelled words
if len(misspelled_words) == 0:
    print("No misspelled words found.")
else:
    print("Misspelled words:")
    for word in misspelled_words:
        print(word)
