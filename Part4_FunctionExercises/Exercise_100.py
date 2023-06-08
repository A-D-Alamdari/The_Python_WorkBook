"""
Exercise 100: Days in aMonth

    Write a function that determines how many days there are in a particular month. Your
    function will take two parameters: The month as an integer between 1 and 12, and
    the year as a four digit integer. Ensure that your function reports the correct number
    of days in February for leap years. Include a main program that reads a month and
    year from the user and displays the number of days in that month. You may find your
    solution to Exercise 57 helpful when solving this problem.
"""


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def get_days_in_month(month, year):
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def main():
    month = int(input("Enter the month (1-12): "))
    year = int(input("Enter the year (YYYY): "))

    days = get_days_in_month(month, year)
    print("Number of days:", days)


if __name__ == "__main__":
    main()
