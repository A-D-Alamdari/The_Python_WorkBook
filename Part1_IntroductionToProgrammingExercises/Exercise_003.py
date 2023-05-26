"""
Exercise 3:Area of a Room

    Write a program that asks the user to enter the width and length of a room. Once
    the values have been read, your program should compute and display the area of the
    room. The length and the width will be entered as floating point numbers. Include
    units in your prompt and output message; either feet or meters, depending on which
    unit you are more comfortable working with.
"""

# Read the input values from the user
# input() method, get the inputs as String format, for converting to floating-point number
# we need to use float() function
length = float(input("Please enter the length of the room in feet: "))
width = float(input("Please enter the width of the room in feet: "))

# The area of a room is calculated by "area = length x width"
# In Python, the multiplication is performed using the "*" operator
area = length * width

# Displaying the results:

# Method 1
print("The area of the room is", area, "square feet.")

# Method 2
print(f"The area of the room is {area} square feet.")

# Method 3
print("The area of the room is {} square feet.".format(area))
