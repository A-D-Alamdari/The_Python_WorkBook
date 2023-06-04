"""
Exercise 53: Assessing Employees

    At a particular company, employees are rated at the end of each year. The rating scale
    begins at 0.0, with higher values indicating better performance and resulting in larger
    raises. The value awarded to an employee is either 0.0, 0.4, or 0.6 or more. Values
    between 0.0 and 0.4, and between 0.4 and 0.6 are never used. The meaning associated
    with each rating is shown in the following table. The amount of an employee’s raise
    is $2400.00 multiplied by their rating.

                Rating          Meaning
                ----------------------------------------
                0.0             Unacceptable performance
                0.4             Acceptable performance
                0.6 or more     Meritorious performance

    Write a program that reads a rating from the user and indicates whether the perfor-
    mance was unacceptable, acceptable or meritorious. The amount of the employee’s
    raise should also be reported. Your program
"""

# Report whether an employee's performance is unacceptable, acceptable
# or meritorious based on the rating entered by the user

# Define some constants
RAISE_FACTOR = 2400.00
UNACCEPTABLE = 0
ACCEPTABLE = 0.4
MERITORIOUS = 0.6

# Read the rating from the user
rating = float(input("Enter the rating: "))

performance = None
# Classifying the performance
if rating == UNACCEPTABLE:
    performance = "Unacceptable"
elif rating == ACCEPTABLE:
    performance = "Acceptable"
elif rating >= MERITORIOUS:
    performance = "Meritorious"
else:
    performance = ""


# Report the result
if performance == "":
    print("Invalid Input!")
else:
    print("Based on the entered rating, the performance is %s." % performance)
    print("You will receive a raise of $%.2f." % (rating * RAISE_FACTOR))
