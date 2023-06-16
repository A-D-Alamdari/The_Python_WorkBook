"""
Exercise 159: RepeatedWords

    Spelling mistakes are only one of many different kinds of errors that might appear in
    a writtenwork. Another error that is common for some writers is a repeatedword. For
    example, an author might inadvertently duplicate a word, as shown in the following
    sentence:

                At least one value must be entered
                entered in order to compute the average.

    Some word processors will detect this error and identify it when a spelling or grammar
    check is performed.
    In this exercise you will write a program that detects repeated words in a text file.
    When a repeated word is found your program should display a message that contains
    the line number and the repeated word. Ensure that your program correctly handles
    the case where the same word appears at the end of one line and the beginning of the
    following line, as shown in the previous example. The name of the file to examine will
    be provided as the program’s only command line parameter. Display an appropriate
    error message if the user fails to provide a command line parameter, or if an error
    occurs while processing the file.
"""


import sys


def find_repeated_words(filename):
    repeated_words = []

    with open(filename, 'r') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            words = line.strip().split()

            for j in range(len(words) - 1):
                if words[j] == words[j + 1]:
                    repeated_words.append((i + 1, words[j]))

    return repeated_words


# Check if the filename is provided as a command line argument
if len(sys.argv) < 2:
    print("Error: Please provide a filename as a command line argument.")
    sys.exit(1)

filename = sys.argv[1]  # Get the filename from the command line argument

try:
    repeated_words = find_repeated_words(filename)

    if len(repeated_words) == 0:
        print("No repeated words found.")
    else:
        print("Repeated words:")
        for line_number, word in repeated_words:
            print(f"Line {line_number}: {word}")

except IOError:
    print(f"Error: Unable to open file '{filename}'.")

