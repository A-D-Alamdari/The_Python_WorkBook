"""
Exercise 9: Compound Interest

    Pretend that you have just opened a new savings account that earns 4 percent interest
    per year. The interest that you earn is paid at the end of the year, and is added
    to the balance of the savings account. Write a program that begins by reading the
    amount of money deposited into the account from the user. Then your program should
    compute and display the amount in the savings account after 1, 2, and 3 years. Display
    each amount so that it is rounded to 2 decimal places.
"""

# We have a constant value
INTEREST_RATE = 0.04

# Get the amount of deposited money from the user
money = float(input("Enter the amount of money that you want to deposit: "))

# Calculate the first year amount
first_year = money * (1 + INTEREST_RATE)

# Calculate the second year amount
second_year = first_year * (1 + INTEREST_RATE)

# Calculate the third year amount
third_year = second_year * (1 + INTEREST_RATE)

# Display the values which is rounded to 2 decimal point
print("At the end of the first year: $%.2f." % first_year)
print("At the end of the second year: $%.2f." % second_year)
print("At the end of the third year: $%.2f." % third_year)
