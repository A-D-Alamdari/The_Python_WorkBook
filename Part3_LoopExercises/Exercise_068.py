"""
Exercise 68: Parity Bits

    A parity bit is a simple mechanism for detecting errors in data transmitted over an
    unreliable connection such as a telephone line. The basic idea is that an additional bit
    is transmitted after each group of 8 bits so that a single bit error in the transmission
    can be detected.
    Parity bits can be computed for either even parity or odd parity. If even parity
    is selected then the parity bit that is transmitted is chosen so that the total number
    of one bits transmitted (8 bits of data plus the parity bit) is even. When odd parity
    is selected the parity bit is chosen so that the total number of one bits transmitted
    is odd.
    Write a program that computes the parity bit for groups of 8 bits entered by the
    user using even parity. Your program should read strings containing 8 bits until the
    user enters a blank line. After each string is entered by the user your program should
    display a clear message indicating whether the parity bit should be 0 or 1. Display
    an appropriate error message if the user enters something other than 8 bits.
    Hint: You should read the input from the user as a string. Then you can use
    the count method to help you determine the number of zeros and ones in the
    string. Information about the count method is available online.
"""

while True:
    # Read 8 bits from the user
    bits = input("Enter 8 bits (or leave blank to finish): ")

    # Check if the user entered a blank line
    if bits == "":
        break

    # Check if the input contains exactly 8 bits
    if len(bits) != 8:
        print("Error: Enter exactly 8 bits. Try again.")
        continue

    # Count the number of ones in the input
    num_ones = bits.count('1')

    # Determine the parity bit
    parity_bit = '0' if num_ones % 2 == 0 else '1'

    # Display the parity bit
    print("Parity bit should be:", parity_bit)

