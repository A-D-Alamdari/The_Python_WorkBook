"""
Exercise 153:A Book with No“e”…

    The novel “Gadsby” is over 50,000 words in length. While 50,000 words isn’t nor-
    mally remarkable for a novel, it is in this case because none of the words in the book
    use the letter “e”. This is particularly noteworthy when one considers that “e” is the
    most common letter in English.
    Write a program that reads a list of words from a file and determines what pro-
    portion of the words use each letter of the alphabet. Display the result for all 26
    letters. Include an additional message identifying the letter that is used in the small-
    est proportion of the words. Your program should ignore any punctuation marks and
    it should treat uppercase and lowercase letters as equivalent.
"""

import string


def count_letter_proportions(file_name):
    letter_counts = {letter: 0 for letter in string.ascii_lowercase}
    total_words = 0

    with open(file_name, "r") as file:
        for line in file:
            line = line.strip().lower()
            words = line.split()

            for word in words:
                # Remove punctuation marks
                word = word.translate(str.maketrans("", "", string.punctuation))

                # Count each letter occurrence
                for letter in word:
                    if letter.isalpha():
                        letter_counts[letter] += 1
                        total_words += 1

    letter_proportions = {letter: count / total_words for letter, count in letter_counts.items()}

    return letter_proportions


# Read the file and count letter proportions
file_name = "words.txt"  # Replace with the actual file path
proportions = count_letter_proportions(file_name)

# Find the letter used in the smallest proportion of words
smallest_proportion_letter = min(proportions, key=proportions.get)

# Display the proportions for all letters
for letter in string.ascii_lowercase:
    print(f"{letter}: {proportions[letter]:.4f}")

# Display the letter used in the smallest proportion of words
print("Letter used in the smallest proportion of words:", smallest_proportion_letter)
