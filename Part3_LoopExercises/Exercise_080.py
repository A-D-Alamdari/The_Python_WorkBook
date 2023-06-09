"""
Exercise 80: Coin Flip Simulation

    What’s the minimum number of times you have to flip a coin before you can have
    three consecutive flips that result in the same outcome (either all three are heads or
    all three are tails)? What’s the maximum number of flips that might be needed? How
    many flips are needed on average? In this exercise we will explore these questions
    by creating a program that simulates several series of coin flips.
    Create a program that uses Python’s random number generator to simulate flipping
    a coin several times. The simulated coin should be fair, meaning that the probability
    of heads is equal to the probability of tails. Your program should flip simulated
    coins until either 3 consecutive heads of 3 consecutive tails occur. Display an H each
    time the outcome is heads, and a T each time the outcome is tails, with all of the
    outcomes shown on the same line. Then display the number of flips needed to reach
    3 consecutive flips with the same outcome. When your program is run it should
    perform the simulation 10 times and report the average number of flips needed.
    Sample output is shown below:
"""

import random

num_simulations = 10
total_flips = 0

for _ in range(num_simulations):
    flips = 0
    consecutive_flips = 0
    last_flip = None

    while consecutive_flips < 3:
        flip = random.choice(['H', 'T'])
        flips += 1

        if flip == last_flip:
            consecutive_flips += 1
        else:
            consecutive_flips = 1

        last_flip = flip
        print(flip, end=' ')

    print(f" ({flips} flips)")
    total_flips += flips

average_flips = total_flips / num_simulations
print(f"On average, {average_flips} flips were needed.")
