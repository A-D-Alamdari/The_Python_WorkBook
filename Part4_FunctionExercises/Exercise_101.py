"""
Exercise 101: Reduce a Fraction to Lowest Terms

    Write a function that takes two positive integers that represent the numerator and
    denominator of a fraction as its only two parameters. The body of the function
    should reduce the fraction to lowest terms and then return both the numerator and
    denominator of the reduced fraction as its result. For example, if the parameters
    passed to the function are 6 and 63 then the function should return 2 and 21. Include
    a main program that allows the user to enter a numerator and denominator. Then
    your program should display the reduced fraction.
    Hint: In Exercise 75 you wrote a program for computing the greatest common
    divisor of two positive integers.You may find that code useful when completing
    this exercise.
"""


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def reduce_fraction(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    reduced_numerator = numerator // common_divisor
    reduced_denominator = denominator // common_divisor
    return reduced_numerator, reduced_denominator


def main():
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    reduced_numerator, reduced_denominator = reduce_fraction(numerator, denominator)
    print("Reduced fraction:", reduced_numerator, "/", reduced_denominator)


if __name__ == "__main__":
    main()
