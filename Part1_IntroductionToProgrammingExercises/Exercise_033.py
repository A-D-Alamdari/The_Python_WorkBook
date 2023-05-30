"""
Exercise 33: Day Old Bread

    A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
    percent. Write a program that begins by reading the number of loaves of day old
    bread being purchased from the user. Then your program should display the regular
    price for the bread, the discount because it is a day old, and the total price. All of the
    values should be displayed using two decimal places, and the decimal points in all
    of the numbers should be aligned when reasonable values are entered by the user.
"""

# Define constants
PRICE_PER_BREAD = 3.49
DISCOUNT_RATE = 0.6

# Get the user input
num = int(input("Enter the number of leaves of day old bread being purchased: "))

# Calculation
regular_price = num * PRICE_PER_BREAD
discount_price = regular_price * (1 - DISCOUNT_RATE)

# Display the result
print("The regular price is %5.2f." % regular_price)
print("The discounted price is %5.2f." % discount_price)
