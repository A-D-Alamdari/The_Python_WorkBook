"""
Exercise 125: Does a List contain a Sublist?

    A sublist is a list that makes up part of a larger list. A sublist may be a list containing
    a single element, multiple elements, or even no elements at all. For example, [1],
    [2], [3] and [4] are all sublists of [1, 2, 3, 4]. The list [2, 3] is also a
    sublist of [1, 2, 3, 4], but [2, 4] is not a sublist [1, 2, 3, 4] because
    the elements 2 and 4 are not adjacent in the longer list. The empty list is a sublist of
    any list. As a result, [] is a sublist of [1, 2, 3, 4]. A list is a sublist of itself,
    meaning that [1, 2, 3, 4] is also a sublist of [1, 2, 3, 4].
    In this exercise you will create a function, isSublist, that determines whether
    or not one list is a sublist of another. Your function should take two lists, larger
    and smaller, as its only parameters. It should return True if and only if smaller
    is a sublist of larger. Write a main program that demonstrates your function.
"""


def is_sublist(larger, smaller):
    if not smaller:  # Empty list is a sublist of any list
        return True

    if len(smaller) > len(larger):  # Smaller list cannot be a sublist if it's larger than the larger list
        return False

    for i in range(len(larger) - len(smaller) + 1):
        if larger[i:i+len(smaller)] == smaller:  # Check if the sublist matches the smaller list
            return True

    return False  # Smaller list not found as a sublist in the larger list


def main():
    larger = input("Enter the larger list, separated by commas: ").split(',')
    smaller = input("Enter the smaller list, separated by commas: ").split(',')

    result = is_sublist(larger, smaller)
    print(f"The smaller list is a sublist of the larger list: {result}")


if __name__ == '__main__':
    main()
