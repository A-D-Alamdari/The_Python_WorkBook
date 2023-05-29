"""
Exercise 16:Area and Volume

    Write a program that begins by reading a radius, r , from the user. The program will
    continue by computing and displaying the area of a circle with radius r and the
    volume of a sphere with radius r . Use the pi constant in the math module in your
    calculations.
    Hint: The area of a circle is computed using the formula area = pi * r ^ 2. The
    volume of a sphere is computed using the formula volume = 4/3 * pi * r ^3
"""

# We need to import math library
import math

# Get input from the user
r = float(input("Enter the radius r: "))

# compute the area of a circle with radius r
area_circle = math.pi * math.pow(r, 2)

# compute the volume of a sphere
volume_sphere = (4 / 3) * math.pi * math.pow(r, 3)

# Display the result
print(f"The area of a circle with radius {r} is: %.3f." % area_circle)
print(f"The volume of a sphere with radius {r} is: %.3f." % volume_sphere)
