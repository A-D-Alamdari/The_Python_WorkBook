"""
Exercise 35: Dog Years

    It is commonly said that one human year is equivalent to 7 dog years. However this
    simple conversion fails to recognize that dogs reach adulthood in approximately two
    years. As a result, some people believe that it is better to count each of the first two
    human years as 10.5 dog years, and then count each additional human year as 4 dog
    years.

    Write a program that implements the conversion from human years to dog years
    described in the previous paragraph. Ensure that your program works correctly for
    conversions of less than two human years and for conversions of two or more human
    years. Your program should display an appropriate error message if the user enters
    a negative number.
"""

# Conversion factors
FIRST_TWO_YEARS_FACTOR = 10.5
ADDITIONAL_YEARS_FACTOR = 4

# Read human years from the user
human_years = float(input("Enter the number of human years: "))

# Check for negative input
if human_years < 0:
    print("Error: Number of human years cannot be negative.")
else:
    # Calculate dog years based on the conversion rules
    if human_years <= 2:
        dog_years = human_years * FIRST_TWO_YEARS_FACTOR
    else:
        additional_years = human_years - 2
        dog_years = (2 * FIRST_TWO_YEARS_FACTOR) + (additional_years * ADDITIONAL_YEARS_FACTOR)

    # Display the converted dog years
    print("Equivalent dog years:", dog_years)
