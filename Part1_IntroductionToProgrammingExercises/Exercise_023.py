"""
Exercise 23:Area of a Regular Polygon

    A polygon is regular if its sides are all the same length and the angles between all of
    the adjacent sides are equal. The area of a regular polygon can be computed using
    the following formula, where s is the length of a side and n is the number of sides:

                    area = (n x s ^ 2) / (4 x tan(pi / n)

    Write a program that reads s and n from the user and then displays the area of a
    regular polygon constructed from these values.
"""

# We need to import the math library
import math

# Get data from the user
side_length = float(input("Enter the side length of the regular polygon: "))
num_side = int(input("Enter the number of sides of the regular polygon: "))

# Compute the area
area = (num_side * math.pow(side_length, 2)) / (4 * math.tan(math.pi / num_side))

# Display the result
print(f"The area of a regular polygon with side length {side_length} and {num_side} sides is %.2f." % area)
