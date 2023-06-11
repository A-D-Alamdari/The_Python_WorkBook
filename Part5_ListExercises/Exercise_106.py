"""
Exercise 106:Remove Outliers

    When analysing data collected as part of a science experiment it may be desirable
    to remove the most extreme values before performing other calculations. Write a
    function that takes a list of values and an non-negative integer, n, as its parameters.
    The function should create a new copy of the list with the n largest elements and the
    n smallest elements removed. Then it should return the new copy of the list as the
    function’s only result. The order of the elements in the returned list does not have to
    match the order of the elements in the original list.
    Write a main program that demonstrates your function. Your function should read
    a list of numbers from the user and remove the two largest and two smallest values
    from it. Display the list with the outliers removed, followed by the original list. Your
    program should generate an appropriate error message if the user enters less than 4
    values.
"""


def remove_extreme_values(data, n):
    if len(data) < 4:
        raise ValueError("The list must contain at least 4 values.")

    sorted_data = sorted(data)
    return sorted_data[n:-n]


def main():
    try:
        values = input("Enter a list of numbers (space-separated): ").split()
        values = [float(x) for x in values]

        outliers_removed = remove_extreme_values(values, 2)

        print("List with outliers removed:", outliers_removed)
        print("Original list:", values)

    except ValueError as e:
        print("Error:", str(e))


if __name__ == '__main__':
    main()


