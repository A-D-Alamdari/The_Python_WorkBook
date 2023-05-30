"""
Exercise 40:Name that Triangle

    A triangle can be classified based on the lengths of its sides as equilateral, isosceles
    or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
    triangle has two sides that are the same length, and a third side that is a different
    length. If all of the sides have different lengths then the triangle is scalene.
    Write a program that reads the lengths of 3 sides of a triangle from the user.
    Display a message indicating the type of the triangle.
"""

# Read the inputs from user
side_1 = float(input("Enter the length of side 1: "))
side_2 = float(input("Enter the length of side 2: "))
side_3 = float(input("Enter the length of side 3: "))

# Determine the name of the triangle
if side_1 == side_2 and side_2 == side_3:
    name = "Equilateral"
elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
    name = "Isosceles"
else:
    name = "Scalene"

# Display the result
print(f"Triangle with side lengths {side_1}, {side_2}, and {side_3} is a {name} triangle.")
