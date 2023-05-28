"""
Exercise 14: Height Units

    Many people think about their height in feet and inches, even in some countries that
    primarily use the metric system. Write a program that reads a number of feet from
    the user, followed by a number of inches. Once these values are read, your program
    should compute and display the equivalent number of centimeters.

    Hint: One foot is 12 inches. One inch is 2.54 centimeters.
"""
# In this example we have 2 constants
IN_PER_FEET = 12
CM_PER_IN = 2.54

# Getting user input
print("Enter your height:")
feet = int(input("  Number of feet: "))
inches = int(input("  Number of inches: "))

height_in_inches = feet * IN_PER_FEET + inches
height_in_cm = height_in_inches * CM_PER_IN

# Display the result
print(f"Your height in centimeters is {height_in_cm} cm.")
