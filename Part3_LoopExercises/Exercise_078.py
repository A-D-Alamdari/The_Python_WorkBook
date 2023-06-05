"""
Exercise 78: Decimal to Binary

    Write a program that converts a decimal (base 10) number to binary (base 2). Read the
    decimal number from the user as an integer and then use the division algorithm shown
    below to perform the conversion. When the algorithm completes, result contains the
    binary representation of the number. Display the result, along with an appropriate
    message.

        Let result be an empty string
        Let q represent the number to convert
        repeat
            Set r equal to the remainder when q is divided by 2
            Convert r to a string and add it to the beginning of result
            Divide q by 2, discarding any remainder, and store the result back into q
        until q is 0
"""

##
# The algorithm provided for question is expressed using a repeat-until loop.
# However, this structure isn't available in Python. As a result, the algorithm has to
# be adjusted so that it generates the same result using a "while" loop. This is achieved
# by duplicating the loop body and placing it ahead of the "while" loop.

# Define base as constant
NEW_BASE = 2

# Get the number from to user to convert it
num = int(input("Enter a non-negative integer: "))

# Generate the binary representation of entered number
result = ""
q = num

# Perform the body of the loop once
r = q % NEW_BASE
result = str(r) + result
q = q // NEW_BASE

# Keep on looping until q == 0
while q > 0:
    r = q % NEW_BASE
    result = str(r) + result
    q = q // NEW_BASE

# display the result
print(f"{num} in Decimal is {result} in Binary.")

