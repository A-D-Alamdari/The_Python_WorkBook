"""
Exercise 165: Greatest Common Divisor

    Euclid was a Greek mathematician who lived approximately 2,300 years ago. His
    algorithm for computing the greatest common divisor of two positive integers, a and
    b, is both efficient and recursive. It is outlined below:

        If b is 0 then
            Return a
        Else
            Set c equal to the remainder when a is divided by b
            Return the greatest common divisor of b and c

    Write a program that implements Euclid’s algorithm and uses it to determine the
    greatest common divisor of two integers entered by the user.
"""


def euclidean_gcd(a, b):
    if b == 0:
        return a
    else:
        c = a % b
        return euclidean_gcd(b, c)


num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

gcd = euclidean_gcd(num1, num2)

print("The greatest common divisor of", num1, "and", num2, "is:", gcd)
