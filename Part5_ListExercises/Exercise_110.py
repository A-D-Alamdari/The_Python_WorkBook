"""
Exercise 110: Perfect Numbers

    An integer, n, is said to be perfect when the sum of all of the proper divisors of n is
    equal to n. For example, 28 is a perfect number because its proper divisors are 1, 2,
    4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28.
    Write a function that determines whether or not a positive integer is perfect. Your
    function will take one parameter. If that parameter is a perfect number then your function
    will return true. Otherwise it will return false. In addition, write a main program
    that uses your function to identify and display all of the perfect numbers between 1
    and 10,000. Import your solution to Exercise 109 when completing this task.
"""
LIMIT = 10000


# Determine whether a number is perfect.
# A number is perfect if the sum of its proper divisors is equal to the number itself.
# @param n : The number to check for perfection.
# @return : True if the number is perfect, False otherwise.
def is_perfect_number(n):
    # Find the proper divisors and calculate their sum
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)

    # Check if the sum of proper divisors is equal to n
    if divisors_sum == n:
        return True
    else:
        return False


# Define the main function
def main():
    print(f"The perfect numbers between 1 and {LIMIT} are:")
    for i in range(1, 10001):
        if is_perfect_number(i):
            print(i)


# Call the main function
main()
