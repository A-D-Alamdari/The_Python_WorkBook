"""
Exercise 168: Recursive Square Root

    Exercise 71 explored how iteration can be used to compute the square root of a
    number. In that exercise a better approximation of the square rootwas generated with
    each additional iteration of a loop. In this exercise you will use the same approxi-
    mation strategy, but you will use recursion instead of iteration.
    Create a square root function that takes two parameters. The first parameter, n, will
    be the number for which the square root is being computed. The second parameter,
    guess, will be the current guess for the square root. The guess parameter should have
    a default value of 1.0. Do not provide a default value for the first parameter.
    Your square root function will be recursive. The base case occurs when guess2 is
    within 10−12 of n. In this case your function should return guess because it is close
    enough to the square root of n. Otherwise your function should return the result of
    calling itself recursively with n as the first parameter and
    (guess+ (n/guess))/ 2 as the second parameter.
    Write a main program that demonstrate your square root function by computing
    the square root of several different values. When you call your square root function
    from the main program you should only pass one parameter to it so that the default
    value for guess is used.
"""


def square_root(n, guess=1.0):
    if abs(guess**2 - n) < 1e-12:
        return guess
    else:
        new_guess = (guess + (n / guess)) / 2
        return square_root(n, new_guess)


num = float(input("Enter a number: "))

result = square_root(num)

print("The square root of", num, "is:", result)
