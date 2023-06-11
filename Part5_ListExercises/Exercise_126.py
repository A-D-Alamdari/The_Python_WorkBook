"""
Exercise 126:Generate All Sublists of a List

    Using the definition of a sublist from Exercise 125, write a function that returns a list
    containing every possible sublist of a list. For example, the sublists of [1, 2, 3]
    are [], [1], [2], [3], [1, 2], [2, 3] and [1, 2, 3]. Note that your function
    will always return a list containing at least the empty list because the empty list
    is a sublist of every list. Include a main program that demonstrate your function by
    displaying all of the sublists of several different lists.
"""


def generate_sublists(lst):
    if len(lst) == 0:
        return [[]]  # Return a list containing the empty list

    first = lst[0]
    remaining = lst[1:]

    sublists = generate_sublists(remaining)

    new_sublists = []

    for sublist in sublists:
        new_sublists.append(sublist)  # Append the sublist as it is
        new_sublists.append([first] + sublist)  # Append the sublist with the first element

    return new_sublists


def main():
    lists = [[], [1], [1, 2], [1, 2, 3], ['a', 'b', 'c']]

    for lst in lists:
        sublists = generate_sublists(lst)
        print(f"Sublists of {lst}:")
        for sublist in sublists:
            print(sublist)
        print()


if __name__ == '__main__':
    main()
