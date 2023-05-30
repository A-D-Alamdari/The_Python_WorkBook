"""
Exercise 38:Month Name to Number of Days

    The length of a month varies from 28 to 31 days. In this exercise you will create
    a program that reads the name of a month from the user as a string. Then your
    program should display the number of days in that month. Display “28 or 29 days”
    for February so that leap years are addressed.
"""

# Get the user input
month = input("Enter the name of a month: ")
month = month.capitalize()

# Classify and display the output
if month in ["April", "June", "September", "November"]:
    print(f"The number of days in {month} is 31.")
elif month == "February":
    print(f"The number of days in {month} is 28 or 29.")
else:
    print(f"The number of days in {month} is 30.")
