"""
Exercise 46: Season from Month and Day

    The year is divided into four seasons: spring, summer, fall and winter. While the
    exact dates that the seasons change vary a little bit from year to year because of the
    way that the calendar is constructed, we will use the following dates for this exercise:

                        Season          First day
                        -----------------------------
                        Spring          March 20
                        Summer          June 21
                        Fall            September 22
                        Winter          December 21

    Create a program that reads a month and day from the user. The user will enter
    the name of the month as a string, followed by the day within the month as an
    integer. Then your program should display the season associated with the date that
    was entered.
"""

# Get the input from the user
month = input("Enter the name of the month: ").lower()
day = int(input("Enter the day number: "))
season = None

# Determine the season
if month == "january" or month == "february":
    season = "Winter"
elif month == "march":
    if day < 20:
        season = "Winter"
    else:
        season = "Spring"
elif month == "april" or month == "may":
    season = "Spring"
elif month == "June":
    if day < 21:
        season = "Spring"
    else:
        season = "Summer"
elif month == "july" or month == "august":
    season = "Summer"
elif month == "september":
    if day < 22:
        season = "Summer"
    else:
        season = "Fall"
elif month == "october" or month == "november":
    season = "Fall"
elif month == "december":
    if day < 21:
        season = "Fall"
    else:
        season = "Winter"


# Display the result
print(month.capitalize(), day, "is in", season)

