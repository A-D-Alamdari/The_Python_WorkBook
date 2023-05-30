"""
Exercise 22:Area of a Triangle (Again)

    In the previous exercise you created a program that computed the area of a triangle
    when the length of its base and its height were known. It is also possible to compute
    the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3
    be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
    can be calculated using the following formula:
                    area = sqrt[s × (s − s1) × (s − s2) × (s − s3)]
    Develop a program that reads the lengths of the sides of a triangle from the user and
    displays its area.
"""

# We need to import math library
import math

# Get data from the user
s1 = float(input("Enter the side 1 of triangle: "))
s2 = float(input("Enter the side 2 of triangle: "))
s3 = float(input("Enter the side 3 of triangle: "))

# Compute the area
s = (s1 + s2 + s3) / 2
area = math.sqrt((s * (s - s1) * (s - s2) * (s - s3)))

# Display the result
print(f"The area of the triangle with side lengths {s1}, {s2}, and {s3} is %.2f." % area)
