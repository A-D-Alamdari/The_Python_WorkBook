"""
Exercise 32: Sort 3 Integers

    Create a program that reads three integers from the user and displays them in sorted
    order (from smallest to largest). Use the min and max functions to find the smallest
    and largest values. The middle value can be found by computing the sum of all three
    values, and then subtracting the minimum value and the maximum value.
"""

# Get user inputs
num_1 = int(input("Enter the first integer: "))
num_2 = int(input("Enter the second integer: "))
num_3 = int(input("Enter the third integer: "))

max_num = max(num_1, num_2, num_3)
min_num = min(num_1, num_2, num_3)

sums = num_1 + num_2 + num_3

mid_num = sums - (max_num + min_num)

# Display the result
print(f"The numbers in sorted order are: \n\t{min_num} < {mid_num} < {max_num}")
