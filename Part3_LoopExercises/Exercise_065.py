"""
Exercise 65: Compute the Perimeter of a Polygon

    Write a program that computes the perimeter of a polygon. Begin by reading the x
    and y values for the first point on the perimeter of the polygon from the user. Then
    continue reading pairs of x and y values until the user enters a blank line for the
    x-coordinate. Each time you read an additional coordinate you should compute the
    distance to the previous point and add it to the perimeter. When a blank line is entered
    for the x-coordinate your program should add the distance from the last point back
    to the first point to the perimeter. Then it should display the total perimeter. Sample
    input and output is shown below, with user input shown in bold:

        Enter the x part of the coordinate: 0
        Enter the y part of the coordinate: 0
        Enter the x part of the coordinate: (blank to quit): 1
        Enter the y part of the coordinate: 0
        Enter the x part of the coordinate: (blank to quit): 0
        Enter the y part of the coordinate: 1
        Enter the x part of the coordinate: (blank to quit):
        The perimeter of that polygon is 3.414213562373095
"""

# Compute the perimeter of a polygon.
# The user will enter a blank line for the x-coordinate to indicate that all the points have been entered.

# We need to import math library
import math

# Initialize a variable to store the perimeter
perimeter = 0

# Get the coordinate of the first point from the user
first_x = float(input("Enter the X part of the coordinates: "))
first_y = float(input("Enter the Y part of the coordinates: "))

# Provide initial values for prev_x and prev_y
prev_x = first_x
prev_y = first_y

# Read the remaining coordinates
# Since we do not know when the user wants to quit, we need to use while loop
line = input("Enter the X part of the coordinate (blank to quit): ")
while line != "":
    # Cast the x part to a floating point number and add it to the perimeter
    x = float(line)
    y = float(input("Enter the y part of the coordinate: "))

    # Compute the distance to the previous point and add it to the perimeter
    dist = math.sqrt((prev_x - x) ** 2 + (prev_y - y) ** 2)
    perimeter += dist

    # Set up prev_x and prev_y for the next iteration
    prev_x = x
    prev_y = y

    # Read the X part of the next coordinate
    line = input("Enter the X part of the coordinate (blank to quit): ")

# Compute the distance from the last point to the first point and add it to the perimeter
dist = math.sqrt((first_x - x) ** 2 + (first_y - y) ** 2)
perimeter += dist

# Display the result
print(f"The perimeter of the polygon is: {perimeter}.")
