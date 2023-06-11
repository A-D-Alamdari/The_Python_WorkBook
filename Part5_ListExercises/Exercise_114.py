"""
Exercise 114: Random Lottery Numbers

    In order to win the top prize in a particular lottery, one must match all 6 numbers
    on his or her ticket to the 6 numbers between 1 and 49 that are drawn by the lottery
    organizer. Write a program that generates a random selection of 6 numbers for a
    lottery ticket. Ensure that the 6 numbers selected do not contain any duplicates.
    Display the numbers in ascending order.
"""

# We need to import random library
import random

# Using constant makes it easy to reconfigure our program for other lotteries
MIN_NUM = 1
MAX_NUM = 49
NUM_NUMS = 6

# Keep a list of the numbers for the ticket
ticket_nums = []

# Generates NUM_NUMS random but distinct numbers
for i in range(NUM_NUMS):
    # Create a number that isn't already on the ticket
    rand = random.randrange(MIN_NUM, MAX_NUM + 1)
    while rand in ticket_nums:
        rand = random.randrange(MIN_NUM, MAX_NUM + 1)

    # Add the distinct number to the ticket
    ticket_nums.append(rand)

# Sort the numbers in ascending order
ticket_nums.sort()

# Display the result
print("Your numbers are: ", end="")
for n in ticket_nums:
    print(n, end=" ")
print()
