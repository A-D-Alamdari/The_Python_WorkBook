"""
Exercise 5: Bottle Deposits

    In many jurisdictions a small deposit is added to drink containers to encourage people
    to recycle them. In one particular jurisdiction, drink containers holding one liter or
    less have a $0.10 deposit, and drink containers holding more than one liter have a
    $0.25 deposit.

    Write a program that reads the number of containers of each size from the user.
    Your program should continue by computing and displaying the refund that will be
    received for returning those containers. Format the output so that it includes a dollar
    sign and always displays exactly two decimal places.
"""

# In this exercise, we have two constants, one for containers equal or less than 1 liter
# and the other for the containers holding more than one liter
LESS_DEPOSIT = 0.10
MORE_DEPOSIT = 0.25

# Get the input from user
less_than_one = float(input("How many containers 1 liter or less do you have? "))
more_than_one = float(input("How many containers more than 1 liter do you have? "))

# Compute the refunds
refund_less = less_than_one * LESS_DEPOSIT
refund_more = more_than_one * MORE_DEPOSIT

total_refund = refund_less + refund_more

# You can compute these in one line, but in future you may need just one of them, and
# computing separately is wise choice, and in this way it is simple to read.
# refund = less_than_one * LESS_DEPOSIT + more_than_one * MORE_DEPOSIT

# Display the result
print("Your total refund will be $%.2f" % total_refund)

# The %.2f format specifier indicates that a value should be formatted as a floating point
# number with 2 digits to the right of the decimal.

