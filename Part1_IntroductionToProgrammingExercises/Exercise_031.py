"""
Exercise 31:Sum of the Digits in an Integer

    Develop a program that reads a four-digit integer from the user and displays the sum
    of the digits in the number. For example, if the user enters 3141 then your program
    should display 3+1+4+1=9.
"""

# Get input from the user
num = input("Enter a four-digit integer: ")

# The input method, get the user input as a String, which is an iterable object
# we can iterate over entered string and get each value in specified index
# and cast it to integer, then sum them as follows:

sums = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])

# display the result to the user
print(f"The sum of digits of the {num} is: {sums}.")

