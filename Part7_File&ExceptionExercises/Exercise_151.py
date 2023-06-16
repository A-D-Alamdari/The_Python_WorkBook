"""
Exercise 151:TwoWord Random Password

    While generating a password by selecting random characters generally gives a rela-
    tively secure password, it also generally gives a password that is difficult to memorize.
    As an alternative, some systems construct a password by taking two English words
    and concatenating them. While this password isn’t as secure, it is much easier to
    memorize.
    Write a program that reads a file containing a list of words, randomly selects two
    of them, and concatenates them to produce a new password. When producing the
    password ensure that the total length is between 8 and 10 characters, and that each
    word used is at least three letters long. Capitalize each word in the password so that
    the user can easily see where one word ends and the next one begins. Display the
    password for the user.
"""

import random


def generate_password(word_list):
    while True:
        word1 = random.choice(word_list).strip()
        word2 = random.choice(word_list).strip()
        password = word1.capitalize() + word2.capitalize()

        if 8 <= len(password) <= 10 and len(word1) >= 3 and len(word2) >= 3:
            return password


# Read the list of words from a file
word_file = "words.txt"  # Replace with the actual file path
with open(word_file, "r") as file:
    words = file.readlines()

# Generate the password
password = generate_password(words)

# Display the password to the user
print("Generated Password:", password)
