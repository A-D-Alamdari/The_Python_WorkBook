"""
Exercise 7:Sum of the First n Positive Integers

    Write a program that reads a positive integer, n, from the user and then displays the
    sum of all the integers from 1 to n. The sum of the first n positive integers can be
    computed using the formula:
                            sum = (n)(n + 1)/2
"""

# Get a positive integer from the user
number = int(input("Enter a positive number: "))

# we suppose that the user enter a valid positive number
# Compute the sum
sums = number * (number + 1) / 2

# Displaying the result
print(f"The sum of the first {number} positive integers is: {sums}")
