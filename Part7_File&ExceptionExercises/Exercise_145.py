"""
Exercise 145: Find the LongestWord in a File

    In this exercise you will create a Python program that identifies the longest word(s)
    in a file. Your program should output an appropriate message that includes the length
    of the longest word, along with all of the words of that length that occurred in the
    file. Treat any group of non-white space characters as a word, even if it includes
    numbers or punctuation marks.
"""

filename = input("Enter the name of the file: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        words = content.split()

    longest_length = 0
    longest_words = []

    for word in words:
        word_length = len(word)
        if word_length > longest_length:
            longest_length = word_length
            longest_words = [word]
        elif word_length == longest_length:
            longest_words.append(word)

    print(f"The longest word(s) have a length of {longest_length}:")
    for longest_word in longest_words:
        print(longest_word)

except FileNotFoundError:
    print("The file does not exist!")
except IOError:
    print("An error occurred while accessing the file!")
