"""
Exercise 21:Area of a Triangle

    The area of a triangle can be computed using the following formula, where b is the
    length of the base of the triangle, and h is its height:
                                area = (b × h) / 2

    Write a program that allows the user to enter values for b and h. The program
    should then compute and display the area of a triangle with base length b and height h.
"""

# Get input from the user
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Compute the area
area = (base * height) / 2

# Display the result
print("The area of the triangle is %.2f." % area)
