"""
Exercise 81: Compute the Hypotenuse

    Write a function that takes the lengths of the two shorter sides of a right triangle as
    its parameters. Return the hypotenuse of the triangle, computed using Pythagorean
    theorem, as the function’s result. Include a main program that reads the lengths of
    the shorter sides of a right triangle from the user, uses your function to compute the
    length of the hypotenuse, and displays the result.
"""


# Define the function

# Compute the Hypotenuse of a right triangle
# @param One of the smallest side of the triangle
# @param The second smallest side of the triangle
# @return The Hypotenuse of the triangle
def hypotenuse(side_1, side_2):
    side_3 = (side_1 ** 2 + side_2 ** 2) ** (1 / 2)
    return side_3


# Get user input
side_1 = float(input("Enter the side 1 of the right triangle: "))
side_2 = float(input("Enter the side 2 of the right triangle: "))

# Compute the Hypotenuse
side_3 = hypotenuse(side_1, side_2)

# Display the result
print("The Hypotenuse of a right triangle with sides %0.1f and %.1f is equal to %.1f." % (side_1, side_2, side_3))
