"""
Exercise 34: Even or Odd?

    Write a program that reads an integer from the user. Then your program should
    display a message indicating whether the integer is even or odd.
"""

# Get input from the user
num = int(input("Enter an integer: "))

# Check Odd vs. Even
if num % 2 == 0:        # If a number is divisible by 2 it is Even, otherwise it is Odd
    print(f"The {num} is an Even number.")
else:
    print(f"The {num} is an Odd number.")
