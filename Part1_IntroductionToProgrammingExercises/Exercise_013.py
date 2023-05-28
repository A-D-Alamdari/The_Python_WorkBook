"""
Exercise 13:Making Change

    Consider the software that runs on a self-checkout machine. One task that it must be
    able to perform is to determine how much change to provide when the shopper pays
    for a purchase with cash.
    Write a program that begins by reading a number of cents from the user as an
    integer. Then your program should compute and display the denominations of the
    coins that should be used to give that amount of change to the shopper. The change
    should be given using as few coins as possible. Assume that the machine is loaded
    with pennies, nickels, dimes, quarters, loonies and toonies.

    A one dollar coin was introduced in Canada in 1987. It is referred to as a
    loonie because one side of the coin has a loon (a type of bird) on it. The two
    dollar coin, referred to as a toonie, was introduced 9 years later. It’s name is
    derived from the combination of the number two and the name of the loonie.
"""

# We have several constants values in this example
CENTS_PER_TOONIE = 200
CENTS_PER_LOONIE = 100
CENTS_PER_QUARTER = 25
CENTS_PER_DIME = 10
CENTS_PER_NICKEL = 5

# Get number of cents from the user
num_cents = int(input("Enter the number of cents: "))

# For calculating the answer of this exercise we need do our calculation in several steps

# Step 1: Determine the number of TOONIES by performing an integer division by 200.
# In python integer division is done by "//" operator
num_toonie = num_cents // CENTS_PER_TOONIE
num_cents = num_cents % CENTS_PER_TOONIE    # After getting the number of TOONIES, how much of cents remains

# Step 2:
num_loonie = num_cents // CENTS_PER_LOONIE
num_cents = num_cents % CENTS_PER_LOONIE

# Step 3:
num_quarters = num_cents // CENTS_PER_QUARTER
num_cents = num_cents % CENTS_PER_QUARTER

# Step 4:
num_dimes = num_cents // CENTS_PER_DIME
num_cents = num_cents % CENTS_PER_DIME

# Step 5:
num_nickles = num_cents // CENTS_PER_NICKEL
num_cents = num_cents % CENTS_PER_NICKEL

num_pennies = num_cents

# Displaying the results
print(f"* {num_toonie} Tonnies")
print(f"* {num_loonie} Lonnies")
print(f"* {num_quarters} Quarters")
print(f"* {num_dimes} Dime")
print(f"* {num_nickles} Nickles")
print(f"* {num_pennies} Pennies")

