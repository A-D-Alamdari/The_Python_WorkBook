"""
Exercise 10:Arithmetic

    Create a program that reads two integers, a and b, from the user.Your program should
    compute and display:
        • The sum of a and b
        • The difference when b is subtracted from a
        • The product of a and b
        • The quotient when a is divided by b
        • The remainder when a is divided by b
        • The result of log10 a
        • The result of aˆb

    Hint: You will probably find the log10 function in the math module helpful
    for computing the second last item in the list.
"""
# Since we want to compute log10 a, we need to import it from MATH library
from math import log10

# Reading two integers from the user
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Compute
sums = a + b
difference = a - b
product = a * b
quotient = a / b
remainder = a % b
log_10 = log10(a)
a_b = a ** b

# Display the results
print(f"{a} + {b} is {sums}.")
print(f"{a} - {b} is {difference}.")
print(f"{a} * {b} is {product}.")
print(f"{a} / {b} is {quotient}.")
print(f"{a} % {b} is {remainder}.")
print(f"The base 10 logarithm of {a} is {log_10}.")
print(f"{a} ^ {b} is {a_b}.")
