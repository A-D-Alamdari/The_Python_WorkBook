"""
Exercise 77: Binary to Decimal

    Write a program that converts a binary (base 2) number to decimal (base 10). Your
    program should begin by reading the binary number from the user as a string. Then
    it should compute the equivalent decimal number by processing each digit in the
    binary number. Finally, your program should display the equivalent decimal number
    with an appropriate message.
"""

binary = input("Enter a binary number: ")
decimal = 0

for digit in binary:
    decimal = decimal * 2 + int(digit)

print(f"The decimal equivalent of {binary} is {decimal}.")

