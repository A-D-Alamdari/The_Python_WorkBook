"""
Exercise 37:Name that Shape

    Write a program that determines the name of a shape from its number of sides. Read
    the number of sides from the user and then report the appropriate name as part of
    a meaningful message. Your program should support shapes with anywhere from 3
    up to (and including) 10 sides. If a number of sides outside of this range is entered
    then your program should display an appropriate error message.
"""

# Get the user input
n_sides = int(input("Enter the number of sides: "))

# Determines the shape
name = ""

if n_sides == 3:
    name = "Triangle"
elif n_sides == 4:
    name = "Quadrilateral"
elif n_sides == 5:
    name = "Pentagon"
elif n_sides == 6:
    name = "Hexagon"
elif n_sides == 7:
    name = "Heptagon"
elif n_sides == 8:
    name = "Octagon"
elif n_sides == 9:
    name = "Nonagon"
elif n_sides == 10:
    name = "Decagon"

# display the error or result
if name == "":
    print("Invalid input!")
else:
    print(f"That is a {name}.")
