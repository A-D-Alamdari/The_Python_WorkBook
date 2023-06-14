"""
Exercise 172: Element Sequences

    Another game that some people play with the names of chemical elements involves
    constructing a sequence of elements where each element in the sequence begins with
    the last letter of its predecessor. For example, if a sequence begins with Hydrogen,
    then the next element must be an element that begins with N, such as Nickel. The
    element following Nickel must begin with L, such as Lithium. The element sequence
    that is constructed can not contain any duplicates.
    Write a program that reads the name of an element from the user. Your program
    should use a recursive function to find the longest sequence of elements that begins
    with the entered element. Then it should display the sequence. Ensure that your
    program responds in a reasonable way if the user does not enter a valid element name.
    Hint: It may take your program up to two minutes to find the longest sequence
    for some elements. As a result, you might want to use elements like Molyb-
    denum and Magnesium as your first test cases. Each has a longest sequence
    that is only 8 elements long which your program should find in a fraction of a
    second.
"""


from sys import *

ELEMENTS_FNAME = "elements.txt"


# Find the longest sequence of words, beginning with start, where each word
# begins with the last letter of its predecessor
def longest_sequence(start, words):
    # Base case: If start is empty then the list of words is empty
    if start == "":
        return []

    # Find the best (longest) list of words by checking each possible word that could
    # appear next in the sequence
    best = []
    last_letter = start[len(start) - 1].lower()
    for i in range(0, len(words)):
        first_letter = words[i][0].lower()
        if first_letter == last_letter:
            candidate = longest_sequence(words[i], words[0: i] + words[i + 1: len(words)])
            if len(candidate) > len(best):
                best = candidate

    return [start] + best


def load_names():
    names = []

    info = open(ELEMENTS_FNAME, "r")

    for line in info:
        line = line.rstrip()
        parts = line.split(",")
        names.append(parts[2])
    info.close()
    return names


def main():
    names = load_names()

    start = input("Enter the name of an element: ")
    start = start.capitalize()

    names.remove(start)

    sequence = longest_sequence(start, names)

    print("A longest sequence that starts with", start, "is:")
    for element in sequence:
        print(" ", element)


main()
