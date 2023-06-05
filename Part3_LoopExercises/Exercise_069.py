"""
Exercise 69: Approximate pi

    The value of pi can be approximated by the following infinite series:

    pi = 3 ± 4 / (2 x 3 x) - 4 / (4 x 5 x 6) + 4 / (8 6 x 7 x 8) - ...

    Write a program that displays 15 approximations of pi. The first approximation
    should make use of only the first term from the infinite series. Each additional approximation
    displayed by your program should include one more term in the series, making
    it a better approximation of pi than any of the approximations displayed previously.
"""

# import math library
import math

# Define save required values
approximations = 15
pi = 3.0
sign = 1

# Calculate
for i in range(1, approximations + 1):
    denominator = (2 * i) * (2 * i + 1) * (2 * i + 2)
    term = 4 / denominator
    pi += sign * term
    sign *= -1

    print(f"Approximation {i}: {pi}")

# Compare with math.pi
print("Actual value of pi:", math.pi)


