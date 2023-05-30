"""
Exercise 39: Sound Levels

    The following table lists the sound level in decibels for several common noises.

                    Noise               Decibel level (dB)
                    Jackhammer          130
                    Gas lawnmower       106
                    Alarm clock         70
                    Quiet room          40

    Write a program that reads a sound level in decibels from the user. If the user
    enters a decibel level that matches one of the noises in the table then your program
    should display a message containing only that noise. If the user enters a number
    of decibels between the noises listed then your program should display a message
    indicating which noises the level is between. Ensure that your program also generates
    reasonable output for a value smaller than the quietest noise in the table, and for a
    value larger than the loudest noise in the table.
"""

# Get the user input
decibels = float(input("Enter the sound level in decibels: "))


if decibels > 130:
    print("The sound level is higher than the loudest noise Jackhammer.")
elif decibels == 130:
    print("The sound level matches the noise: Jackhammer")
elif 106 < decibels < 130:
    print("The noise is between Jackhammer noise and Gas lawnmower.")
elif decibels == 106:
    print("The sound level matches the noise: Gas lawnmower.")
elif 70 < decibels < 106:
    print("The noise is between Gas lawnmower noise and Alarm clock.")
elif decibels == 70:
    print("The sound level matches the noise: Alarm clock.")
elif 40 < decibels < 70:
    print("The noise is between Quiet room noise and Alarm clock.")
elif decibels == 40:
    print("The sound level matches the noise: Quiet room.")
else:
    print("The sound level is lower than the quietest noise Quiet room.")

