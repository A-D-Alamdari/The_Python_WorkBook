"""
Exercise 136:Anagrams Again

    The notion of anagrams can be extended to multiple words. For example, “William
    Shakespeare” and “I am a weakish speller” are anagrams when capitalization and
    spacing are ignored.
    Extend your program from Exercise 135 so that it is able to check if two phrases
    are anagrams. Your program should ignore capitalization, punctuation marks and
    spacing when making the determination.
"""

import string


def check_anagrams(phrase1, phrase2):
    # Remove punctuation and convert to lowercase
    phrase1 = phrase1.translate(str.maketrans("", "", string.punctuation)).lower()
    phrase2 = phrase2.translate(str.maketrans("", "", string.punctuation)).lower()

    # Remove whitespace
    phrase1 = phrase1.replace(" ", "")
    phrase2 = phrase2.replace(" ", "")

    # Create dictionaries to count the occurrence of each letter
    count1 = {}
    count2 = {}

    # Count the occurrence of each letter in phrase1
    for letter in phrase1:
        count1[letter] = count1.get(letter, 0) + 1

    # Count the occurrence of each letter in phrase2
    for letter in phrase2:
        count2[letter] = count2.get(letter, 0) + 1

    # Check if the dictionaries are equal
    return count1 == count2


# Example usage
phrase1 = input("Enter the first phrase: ")
phrase2 = input("Enter the second phrase: ")
if check_anagrams(phrase1, phrase2):
    print("The phrases are anagrams.")
else:
    print("The phrases are not anagrams.")
