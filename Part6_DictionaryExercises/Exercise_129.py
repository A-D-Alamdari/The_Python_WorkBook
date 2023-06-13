"""
Exercise 129:Two Dice Simulation

    In this exercise you will simulate 1,000 rolls of two dice. Begin by writing a func-
    tion that simulates rolling a pair of six-sided dice. Your function will not take any
    parameters. It will return the total that was rolled on two dice as its only result.
    Write a main program that uses your function to simulate rolling two six-sided
    dice 1,000 times. As your program runs, it should count the number of times that each
    total occurs. Then it should display a table that summarizes this data. Express the
    frequency for each total as a percentage of the total number of rolls. Your program
    should also display the percentage expected by probability theory for each total.
    Sample output is shown below.
"""

import random


def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)


def simulate_rolls():
    totals = [0] * 11

    for _ in range(1000):
        total = roll_dice()
        totals[total - 2] += 1

    return totals


def display_results(totals):
    print("Total     Simulated %     Expected %")
    print("------    ------------    -----------")

    for i in range(2, 13):
        simulated_percent = (totals[i - 2] / 1000) * 100
        expected_percent = (6 - abs(7 - i)) / 36 * 100
        print(f"{i:6}   {simulated_percent:12.2f}%   {expected_percent:11.2f}%")


# Simulate 1,000 rolls of two dice
totals = simulate_rolls()

# Display the results
display_results(totals)
