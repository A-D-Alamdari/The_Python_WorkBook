"""
Exercise 120: Is a List already in Sorted Order?

    Write a function that determines whether or not a list of values is in sorted order
    (either ascending or descending). The function should return True if the list is
    already sorted. Otherwise it should return False. Write a main program that reads
    a list of numbers from the user and then uses your function to report whether or not
    the list is sorted.

    Make sure you consider these questions when completing this exercise: Is a
    list that is empty in sorted order? What about a list containing one element?
"""


def is_sorted(lst):
    if len(lst) <= 1:  # Empty list or list with one element is considered sorted
        return True

    if lst == sorted(lst) or lst == sorted(lst, reverse=True):
        return True

    return False


def main():
    numbers = input("Enter a list of numbers (space-separated): ").split()
    numbers = [int(num) for num in numbers]

    if is_sorted(numbers):
        print("The list is sorted.")
    else:
        print("The list is not sorted.")


main()
