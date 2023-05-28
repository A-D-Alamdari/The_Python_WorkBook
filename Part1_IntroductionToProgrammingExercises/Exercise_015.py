"""
Exercise 15: Distance Units

    In this exercise, you will create a program that begins by reading a measurement
    in feet from the user. Then your program should display the equivalent distance in
    inches, yards and miles. Use the Internet to look up the necessary conversion factors
    if you don’t have them memorized.
"""
INCH_PER_FEET = 12
YARDS_PER_FEET = 1.0 / 3.0
MILES_PER_FEET = 1.0 / 5280

# Get the user inputs
distance = int(input("Enter your measurement in feet: "))

d_in_yards = distance * YARDS_PER_FEET
d_in_miles = distance * MILES_PER_FEET

print("Your measurement is %.4f yards or %.4f miles." % (d_in_yards, d_in_miles))

