"""
Exercise 121: Count the Elements

    Python’s standard library includes a method named count that determines how
    many times a specific value occurs in a list. In this exercise, you will create a new
    function named countRange which determines and returns the number of elements
    within a list that are greater than or equal to some minimum value and less than some
    maximum value. Your function will take three parameters: the list, the minimum
    value and the maximum value. It will return an integer result greater than or equal to
    0. Include a main program that demonstrates your function for several different lists,
    minimum values and maximum values. Ensure that your program works correctly
    for both lists of integers and lists of floating point numbers.
"""


def count_range(lst, min_val, max_val):
    count = 0
    for item in lst:
        if min_val <= item < max_val:
            count += 1
    return count


def main():
    # Example usage
    integer_list = [1, 5, 3, 7, 2, 4, 6]
    float_list = [1.5, 3.7, 2.2, 4.9, 2.5, 3.1, 4.3]

    min_val = 2
    max_val = 5

    integer_count = count_range(integer_list, min_val, max_val)
    float_count = count_range(float_list, min_val, max_val)

    print("Number of integers within the range:", integer_count)
    print("Number of floats within the range:", float_count)


main()
