"""
Exercise 103: Magic Dates

    A magic date is a date where the day multiplied by the month is equal to the two digit
    year. For example, June 10, 1960 is am agic date because June is the sixth month, and
    6 times 10 is 60, which is equal to the two digit year. Write a function that determines
    whether or not a date is a magic date. Use your function to create a main program
    that finds and displays all of the magic dates in the 20th century. You will probably
    find your solution to Exercise 100 helpful when completing this exercise.
"""
import datetime


def is_magic_date(date):
    day, month, year = date.day, date.month, date.year % 100
    return day * month == year


def main():
    # Iterate over the dates in the 20th century (1901-2000)
    for year in range(1901, 2001):
        for month in range(1, 13):
            for day in range(1, 32):
                try:
                    date = datetime.date(year, month, day)
                    if is_magic_date(date):
                        print(date.strftime("%B %d, %Y"))
                except ValueError:
                    # Skip invalid dates (e.g., February 30)
                    continue


if __name__ == "__main__":
    main()
