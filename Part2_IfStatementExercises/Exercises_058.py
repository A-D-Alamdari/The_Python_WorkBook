"""
Exercise 58: Next Day

    Write a program that reads a date from the user and computes its immediate successor.
    For example, if the user enters values that represent 2013-11-18 then your program
    should display a message indicating that the day immediately after 2013-11-18 is
    2013-11-19. If the user enters values that represent 2013-11-30 then the program
    should indicate that the next day is 2013-12-01. If the user enters values that represent
    2013-12-31 then the program should indicate that the next day is 2014-01-01. The
    date will be entered in numeric form with three separate input statements; one for
    the year, one for the month, and one for the day. Ensure that your program works
    correctly for leap years.
"""


def is_leap_year(year):
    """
    Check if a year is a leap year.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def compute_successor_date(year, month, day):
    """
    Compute the immediate successor date of the given date.
    """
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_in_month[2] = 29

    # Increment the day
    day += 1

    if day > days_in_month[month]:
        day = 1
        month += 1

        if month > 12:
            month = 1
            year += 1

    return year, month, day


# User inputs
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

# Compute the successor date
successor_year, successor_month, successor_day = compute_successor_date(year, month, day)

# Display the result
successor_date = f"{successor_year}-{successor_month:02d}-{successor_day:02d}"
print(f"The day immediately after {year}-{month:02d}-{day:02d} is {successor_date}.")
