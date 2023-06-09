"""
Exercise 71: Square Root

    Write a program that implements Newton’smethod to compute and display the square
    root of a number entered by the user. The algorithm for Newton’s method follows:

        Read x from the user
        Initialize guess to x/2
        While guess is not good enough do
            Update guess to be the average of guess and x/guess

    When this algorithm completes, guess contains an approximation of the square
    root. The quality of the approximation depends on how you define “good enough”.
    In the author’s solution, guess was considered good enough when the absolute value
    of the difference between guess * guess and x was less than or equal to 10ˆ−12.
"""

x = float(input("Enter a number: "))
guess = x / 2

while abs(guess * guess - x) > 1e-12:
    guess = (guess + x / guess) / 2

print("Square root:", guess)
