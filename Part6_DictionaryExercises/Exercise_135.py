"""
Exercise 135:Anagrams

    Two words are anagrams if they contain all of the same letters, but in a different
    order. For example, “evil” and “live” are anagrams because each contains one e, one
    i, one l, and one v. Create a program that reads two strings from the user, determines
    whether or not they are anagrams, and reports the result.
"""


def check_anagrams(word1, word2):
    # Convert the words to lowercase and remove whitespace
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")

    # Check if the lengths of the words are different
    if len(word1) != len(word2):
        return False

    # Create dictionaries to count the occurrence of each letter
    count1 = {}
    count2 = {}

    # Count the occurrence of each letter in word1
    for letter in word1:
        count1[letter] = count1.get(letter, 0) + 1

    # Count the occurrence of each letter in word2
    for letter in word2:
        count2[letter] = count2.get(letter, 0) + 1

    # Check if the dictionaries are equal
    return count1 == count2


# Example usage
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
if check_anagrams(word1, word2):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")
