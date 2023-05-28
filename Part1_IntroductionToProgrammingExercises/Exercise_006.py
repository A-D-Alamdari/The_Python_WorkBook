"""
Exercise 6:Tax and Tip

    The program that you create for this exercise will begin by reading the cost of a meal
    ordered at a restaurant from the user. Then your program will compute the tax and
    tip for the meal. Use your local tax rate when computing the amount of tax owing.
    Compute the tip as 18 percent of the meal amount (without the tax). The output from
    your program should include the tax amount, the tip amount, and the grand total for
    the meal including both the tax and the tip. Format the output so that all of the values
    are displayed using two decimal places.
"""

# In this question we have two constant values as follows
TAX_RATE = 0.08     # The Tax rate in Turkey is 8%
TIP_RATE = 0.18

# We need to read the cost of the meal from the user
cost = float(input("Enter the cost of the meal: "))

# compute the tax and tip amount
tax = cost * TAX_RATE
tip = cost * TIP_RATE
total_cost = cost + tax + tip

# Displaying the results
print("The tax is $%.2f and the tip is $%.2f, making the total $%.2f." % (tax, tip, total_cost))

