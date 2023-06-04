"""
Exercise 57: Is it a Leap Year?

    Most years have 365 days. However, the time required for the Earth to orbit the Sun
    is actually slightly more than that. As a result, an extra day, February 29, is included
    in some years to correct for this difference. Such years are referred to as leap years.
    The rules for determining whether or not a year is a leap year follow:

        • Any year that is divisible by 400 is a leap year.
        • Of the remaining years, any year that is divisible by 100 is not a leap year.
        • Of the remaining years, any year that is divisible by 4 is a leap year.
        • All other years are not leap years.

    Write a program that reads a year from the user and displays a message indicating
    whether or not it is a leap year.
"""

# Get the input from the user
year = int(input("Enter a year: "))

is_leap = False

# Determine if it is a leap year or not
if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = False
elif year % 4 == 0:
    is_leap = True
else:
    is_leap = False

# Display the result
if is_leap:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is NOT a leap year!")
