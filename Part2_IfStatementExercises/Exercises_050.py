"""
Exercise 50: Roots of a Quadratic Function

    A uni-variate quadratic function has the form f (x) = ax2 + bx + c, where a, b and
    c are constants, and a is non-zero. The roots of a quadratic function can be found
    by finding the values of x that satisfy the quadratic equation ax2 + bx + c = 0. A
    quadratic function may have 0, 1 or 2 real roots. These roots can be computed using
    the quadratic formula, shown below:

                    root = (−b ± sqrt(bˆ2 - 4 x a x c)) / 2 x a

    The portion of the expression under the square root sign is called the discriminant.
    If the discriminant is negative then the quadratic equation does not have any real roots.
    If the discriminant is 0, then the equation has one real root. Otherwise the equation
    has two real roots, and the expression must be evaluated twice, once using a plus
    sign, and once using a minus sign, when computing the numerator.
    Write a program that computes the real roots of a quadratic function.Your program
    should begin by prompting the user for the values of a, b and c. Then it should display
    a message indicating the number of real roots, along with the values of the real roots
    (if any).
"""
# import the math library
import math

# Get input from the user
a = float(input("Enter the coefficient of xˆ2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant value: "))

# Calculate the roots
delta = b ** 2 - 4 * a * c

if delta <= 0:
    print(f"{a}*(xˆ2) + {b}*x + {c} has not any real root!")
else:
    root1 = (-1 * b + math.sqrt(delta)) / (2 * a)
    root2 = (-1 * b - math.sqrt(delta)) / (2 * a)
    print(f"{a}*(xˆ2) + {b}*x + {c} has two roots which are: {root1} and {root2}.")


