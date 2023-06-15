"""
Exercise 147:Words that Occur Most

    Write a program that displays the word (or words) that occur most frequently in a
    file. Your program should begin by reading the name of the file from the user. Then
    it should find the word(s) by splitting each line in the file at each space. Finally,
    any leading or trailing punctuation marks should be removed from each word. In
    addition, your program should ignore capitalization. As a result, apple, apple!,
    Apple and ApPlE should all be treated as the same word. You will probably find
    your solution to Exercise 111 helpful when completing this problem.
"""

import string

filename = input("Enter the name of the file: ")

try:
    with open(filename, "r") as file:
        content = file.read().lower()

    # Remove leading and trailing punctuation marks
    content = content.translate(str.maketrans("", "", string.punctuation))

    words = content.split()

    word_freq = {}
    max_freq = 0
    most_frequent_words = []

    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
        if word_freq[word] > max_freq:
            max_freq = word_freq[word]
            most_frequent_words = [word]
        elif word_freq[word] == max_freq:
            most_frequent_words.append(word)

    print("Most frequent word(s):")
    for word in most_frequent_words:
        print(word)

except FileNotFoundError:
    print("The file does not exist!")
except IOError:
    print("An error occurred while accessing the file!")
