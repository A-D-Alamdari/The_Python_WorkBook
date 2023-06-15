"""
Exercise 146: Letter Frequencies

    One technique that can be used to help break some simple forms of encryption is
    frequency analysis. This analysis examines the encrypted text to determine which
    characters are most common. Then it tries to map the most common letters in Eng-
    lish, such as E and T, to the most commonly occurring characters in the encrypted
    text.
    Write a program that initiates this process by determining and displaying the
    frequencies of all letters in a file. Ignore spaces, punctuation marks, and numbers as
    you perform this analysis. Your program should be case insensitive, treating a and
    A as equivalent. The user will provide the file name as a command line parameter.
    Your program should display a meaningful error message if the user provides the
    wrong number of command line parameters, or if the program is unable to open the
    file indicated by the user.
"""

import sys
import string

if len(sys.argv) != 2:
    print("You must provide the file name as a command line parameter!")
    quit()

try:
    filename = sys.argv[1]
    with open(filename, "r") as file:
        content = file.read().lower()

    letter_freq = {}
    for char in content:
        if char.isalpha():
            letter_freq[char] = letter_freq.get(char, 0) + 1

    print("Letter frequencies:")
    for letter in string.ascii_lowercase:
        if letter in letter_freq:
            print(f"{letter}: {letter_freq[letter]}")
        else:
            print(f"{letter}: 0")

except FileNotFoundError:
    print("The file requested does not exist!")
except IOError:
    print("An error occurred while accessing the file!")
