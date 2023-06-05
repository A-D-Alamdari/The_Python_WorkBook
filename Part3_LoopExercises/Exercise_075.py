"""
Exercise 75: Greatest Common Divisor

    The greatest common divisor of two positive integers, n and m, is the largest number,
    d, which divides evenly into both n and m. There are several algorithms that can be
    used to solve this problem, including:

        Initialize d to the smaller of m and n.
        While d does not evenly divide m or d does not evenly divide n do
            Decrease the value of d by 1
        Report d as the greatest common divisor of n and m

    Write a program that reads two positive integers from the user and uses this algorithm
    to determine and report their greatest common divisor.
"""

# Get user inputs
n = int(input("Enter a positive integer: "))
m = int(input("Enter a positive integer: "))

# Initialize a variable to the smallest of n and m
d = min(m, n)

# Use a while-loop to find the greatest common divisor of n and m
while m % d != 0 or m % d != 0:
    d = d - 1

# Display the result
print(f"The greatest common divisor of {n} and {m} is: {d}")
