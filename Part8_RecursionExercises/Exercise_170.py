"""
Exercise 170: Possible Change

    Create a program that determines whether or not it is possible to construct a particular
    total using a specific number of coins. For example, it is possible to have a total of
    $1.00 using four coins if they are all quarters. However, there is no way to have a
    total of $1.00 using 5 coins. Yet it is possible to have $1.00 using 6 coins by using
    3 quarters, 2 dimes and a nickel. Similarly, a total of $1.25 can be formed using 5
    coins or 8 coins, but a total of $1.25 can not be formed using 4, 6 or 7 coins.
    Your program should read both the dollar amount and the number of coins from
    the user. It should display a clear message indicating whether or not the entered dollar
    amount can be formed using the number of coins indicated. Assume the existence of
    quarters, dimes, nickels and pennies when completing this problem. Your solution
    must use recursion. It can not contain any loops.
"""


def is_possible_total(total, num_coins):
    # Base cases
    if total == 0 and num_coins == 0:
        return True
    if total != 0 and num_coins == 0:
        return False

    # Recursive cases
    if total >= 25:  # Check if a quarter can be used
        if is_possible_total(total - 25, num_coins - 1):
            return True
    if total >= 10:  # Check if a dime can be used
        if is_possible_total(total - 10, num_coins - 1):
            return True
    if total >= 5:  # Check if a nickel can be used
        if is_possible_total(total - 5, num_coins - 1):
            return True
    if total >= 1:  # Check if a penny can be used
        if is_possible_total(total - 1, num_coins - 1):
            return True

    return False


total_amount = 100  # $1.00
num_coins = 4
result = is_possible_total(total_amount, num_coins)

if result:
    print("It is possible to form a total of $%.2f using %d coins." % (total_amount / 100, num_coins))
else:
    print("It is not possible to form a total of $%.2f using %d coins." % (total_amount / 100, num_coins))
