"""
Exercise 60: Roulette Payouts

    Aroulette wheel has 38 spaces on it. Of these spaces, 18 are black, 18 are red, and two
    are green. The green spaces are numbered 0 and 00. The red spaces are numbered 1,
    3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36. The remaining integers
    between 1 and 36 are used to number the black spaces.
    Many different bets can be placed in roulette.We will only consider the following
    subset of them in this exercise:

        • Single number (1 to 36, 0, or 00)
        • Red versus Black
        • Odd versus Even (Note that 0 and 00 do not pay out for even)
        • 1 to 18 versus 19 to 36

    Write a program that simulates a spin of a roulette wheel by using Python’s random
    number generator. Display the number that was selected and all of the bets that must
    be payed. For example, if 13 is selected then your program should display:

        The spin resulted in 13...
        Pay 13
        Pay Black
        Pay Odd
        Pay 1 to 18

    If the simulation results in 0 or 00 then your program should display Pay 0 or
    Pay 00 without any further output.
"""

# We need to import random library
import random

# Simulate spinning the wheel, using 37 to represent 00
value = random.randrange(0, 38)
if value == 37:
    print("Th spin resulted in 00...")
else:
    print("The spin resulted in %d..." % value)

# display the payout for a single number
if value == 37:
    print("Pay 00")
else:
    print(f"Pay {value}")

# display the color payout
# The first line in the condition checks for 1, 3, 5, 7, 9
# The second line in the condition checks for 12, 14, 16, 18
# The third line in the condition checks for 19, 21, 23, 25, 27
# The fourth line in the condition checks for 30, 32, 34, 36

if value % 2 == 1 and 1 <= value <= 9 or \
        value % 2 == 0 and 12 <= value <= 18 or \
        value % 2 == 1 and 19 <= value <= 27 or \
        value % 2 == 0 and 30 <= value <= 36:
    print("Pay RED.")
elif value == 0 or value == 37:
    pass        # When a statement is required but is no work to be performed, we use "pass" keyword.
else:
    print("Pay BLACK.")

# Display the odd vs. even payout
if 1 <= value <= 36:
    if value % 2 == 1:
        print("Pay ODD.")
    else:
        print("Pay EVEN")

# Display the lower number vs. upper number payout
if 1 <= value <= 18:
    print("Pay 1 to 18.")
elif 19 <= value <= 36:
    print("Pay 19 to 36")
