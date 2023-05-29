"""
Exercise 18:Volume of a Cylinder

    The volume of a cylinder can be computed by multiplying the area of its circular
    base by its height. Write a program that reads the radius of the cylinder, along with
    its height, from the user and computes its volume. Display the result rounded to one
    decimal place.
"""
# We need to import math library
import math

# Get data from the user
r = float(input("Enter the radius of the cylinder: "))
h = float(input("Enter the height of the cylinder: "))

# Compute the volume of the cylinder
area = math.pi * (r ** 2)
volume = area * h

# display the result
print(f"The volume of a cylinder with radius {r} and height {h} is equals to %.3f." % volume)
