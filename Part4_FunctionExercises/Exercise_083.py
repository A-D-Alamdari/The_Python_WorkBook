"""
Exercise 83: Shipping Calculator

    An online retailer provides express shipping for many of its items at a rate of $10.95
    for the first item, and $2.95 for each subsequent item. Write a function that takes the
    number of items in the order as its only parameter. Return the shipping charge for
    the order as the function’s result. Include a main program that reads the number of
    items purchased from the user and displays the shipping charge.
"""

# Define constants
FIRST_ORDER = 10.95
SUBSEQUENT_ORDER = 2.95


# Function that calculate the shipping price
# @param item: Number of items in the order
# @return The total shipment fee
def shipment_calculator(item):
    return FIRST_ORDER + SUBSEQUENT_ORDER * (item - 1)


# Get user input
num_items = int(input("Enter the number of items in your order: "))

# Calculate the fee
shipment_fee = shipment_calculator(num_items)

# Display the result
print("The shipment fee for %d items is $%.2f." % (num_items, shipment_fee))
